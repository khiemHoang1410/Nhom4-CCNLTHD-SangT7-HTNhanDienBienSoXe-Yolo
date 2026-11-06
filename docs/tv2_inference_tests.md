# Báo Cáo Kỹ Thuật Kiểm Thử Tiền Xử Lý Ảnh & Suy Luận YOLO (Chương 9)

- **Người thực hiện:** Phạm Văn Nhật (Thành viên 2 - MSSV: 3122410275)
- **Mã nguồn kiểm thử:** `tests/test_preprocessing.py`, `tests/test_inference_smoke.py`
- **Mục tiêu:** Kiểm chứng tính ổn định của pipeline tiền xử lý ảnh và suy luận mô hình nhận diện biển số xe.

---

## 1. Danh Mục Các Ca Kiểm Thử (Unit Tests)
1. **`test_decode_image_roundtrip`**: Kiểm tra giải mã mảng byte thành ảnh BGR chuẩn không suy hao.
2. **`test_crop_plate_without_padding`**: Kiểm tra thuật toán cắt bounding box theo tọa độ chuẩn xác.
3. **`test_crop_plate_with_padding_clamps_to_bounds`**: Kiểm tra mở rộng biên cắt (padding) và cơ chế kẹp giới hạn khung hình an toàn.
4. **`test_preprocess_plate_is_gray_upscaled_and_not_binary`**: Kiểm chứng đầu ra tiền xử lý giữ nguyên thang độ xám (Grayscale), phóng đại 2x và không bị nhị phân hóa gắt.
5. **`test_is_two_line_aspect_ratio_heuristic`**: Kiểm tra nhận diện hình học biển số 1 dòng và biển số 2 dòng dựa trên tỉ lệ W/H.
6. **`test_split_two_lines_splits_horizontally`**: Kiểm tra phân chia ngang cho biển số xe máy 2 dòng.
7. **`test_deskew_plate_handles_blank_image`**: Kiểm tra thuật toán nắn thẳng góc nghiêng biển số (Deskew).

---

## 2. Kết Quả Xác Minh Tự Động (CI Runner)
- Trạng thái kiểm thử: **Passed 100%**.
- Tích hợp liên tục: Đảm bảo không phát sinh lỗi hồi quy khi tích hợp vào nhánh chính `main`.
