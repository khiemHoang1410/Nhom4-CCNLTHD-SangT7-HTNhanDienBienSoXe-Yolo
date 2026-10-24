FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    EASYOCR_MODULE_PATH=/opt/easyocr

WORKDIR /app

# System libraries required by OpenCV / EasyOCR.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-docker.txt .
RUN python -m pip install --no-cache-dir --only-binary=:all: \
        --index-url https://pypi.org/simple -r requirements-docker.txt \
    && python -m pip check

COPY be/ ./be/
COPY src/ ./src/
COPY weights/best.pt ./weights/best.pt
COPY assets/samples/ ./assets/samples/
COPY .env.example ./.env.example

# Named volume in Compose; no private host OCR cache or build-time downloads.
RUN mkdir -p /opt/easyocr/model /opt/easyocr/user_network

EXPOSE 8000

CMD ["uvicorn", "be.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
