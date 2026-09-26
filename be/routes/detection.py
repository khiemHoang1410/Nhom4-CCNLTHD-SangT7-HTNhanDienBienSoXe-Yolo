"""``/detect`` endpoint."""

from fastapi import APIRouter, File, HTTPException, Request, UploadFile

from ..inference_admission import admission_for, wait_for_worker
from ..services.detection_service import DetectionService
from ..upload_security import (
    UploadValidationError, read_upload, validate_image_header, validate_decoded_image,
)
from src.inference.preprocessing import decode_image

router = APIRouter()

# Single long-lived service; model weights are loaded lazily on first request.
_service = DetectionService()


def _process_upload(contents, service):
    """The R01 synchronous validation/decode/pipeline, executed off the loop."""
    validate_image_header(contents)
    try:
        image = decode_image(contents)
    except Exception:
        raise UploadValidationError(400, "Invalid image") from None
    validate_decoded_image(image)
    return service.detect_image(image)


@router.post("/detect")
async def detect_and_ocr(request: Request, file: UploadFile = File(...)):
    """Reject busy requests before reading; keep running work admitted on cancel."""
    admission = admission_for(request.app)
    lease = admission.try_acquire()
    if lease is None:
        raise HTTPException(503, "Inference busy; try again later")
    future = None
    try:
        contents = await read_upload(file)
        future = admission.submit(lease, _process_upload, contents, _service)
        return await wait_for_worker(future)
    except UploadValidationError as exc:
        raise HTTPException(exc.status_code, exc.detail) from None
    finally:
        if future is None:
            # Read failure/cancellation or failed submit: no worker owns it yet.
            lease.release()


__all__ = ["router"]
