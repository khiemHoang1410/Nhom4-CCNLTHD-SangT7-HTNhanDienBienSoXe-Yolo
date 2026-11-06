# Ma Trận Kiểm Thử Tự Động Toàn Diện Hệ Thống ALPR

- **Tác giả đề xuất:** Phạm Văn Nhật (TV2 - MSSV: 3122410275)
- **Người phê duyệt & Merge:** Phạm Hữu Nghĩa (TV1 - Merge Lead)
- **Tổng số ca kiểm thử:** 164 unit/integration test cases (CI/CD GitHub Actions)

---

## 1. Phân Loại Ca Kiểm Thử

| Phân hệ | Tệp kiểm thử | Số ca test | Trạng thái CI | Mô tả chi tiết |
|---|---|---|---|---|
| **Đường dẫn & Cấu hình** | `tests/test_paths.py` | 4 | Passed | Kiểm tra đường dẫn dữ liệu tương đối, loại trừ hardcode ổ đĩa Windows (D:/) |
| **Tiền xử lý ảnh (OpenCV)** | `tests/test_preprocessing.py` | 7 | Passed | Decode byte ảnh, cắt bounding box, padding viền, CLAHE grayscale, kiểm tra tỉ lệ |
| **Hậu xử lý & Định dạng OCR** | `tests/test_postprocessing.py` | 73 | Passed | Phân tách 2 dòng, bảng hoán vị ký tự gây nhầm lẫn (B/8, 0/O, 1/I), chuẩn hóa biển số VN |
| **Orchestration Dịch vụ** | `tests/test_service.py` | 7 | Passed | Stub detector + OCR, bảo toàn kiểu dữ liệu confidence, xử lý không phát hiện biển |
| **Hợp đồng API & Mã lỗi** | `tests/test_api.py` | 4 | Passed | Endpoint `/detect`, kiểm thử tích hợp multipart/form-data, xử lý lỗi an toàn |
| **Bảo mật Upload & Middleware** | `tests/test_upload_security.py` | 64 | Passed | Ràng buộc kích thước file, kiểm tra magic bytes JPEG/PNG/WEBP, chống tấn công cạn kiệt bộ nhớ |
| **Quản lý Concurrency & Worker** | `tests/test_inference_admission.py` | 4 | Passed | Ràng buộc 1 worker cho môi trường demo CPU, kiểm soát admission guard |
| **Smoke Test Đầu Cuối** | `tests/test_inference_smoke.py` | 1 | Skipped/Passed | Kiểm thử toàn trình YOLO + EasyOCR khi có trọng số |

---

## 2. Kết Quả Kiểm Thử Tự Động (GitHub Actions)
- Môi trường: Ubuntu-latest / Python 3.10
- Thời gian thực thi: ~2.5s
- Kết quả: **163 passed, 1 skipped (100% pass)**
