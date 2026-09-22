# Dữ liệu lá số (D§)

> Tham chiếu của `QUY-TAC-LUAN-GIAI-TU-VI.md`. Không sửa file dữ liệu nguồn.

## 1. Cấu trúc

- `data/<người>/`: dữ liệu lá số của từng người. `rp/`: report.
- `data/hoang/`
  - `tuvi-hoang-pham-huy-2026.json`: JSON gốc từ API.
  - `tuvi-hoang-pham-huy-2026.data.json`: bản làm sạch (schema 1.0.0), do `scripts/clean-tuvi-data.ps1` tạo (cần PowerShell; máy hiện tại chưa cài).
  - `tuvi-hoang-pham-huy-2026.md`: bảng tóm tắt.
  - `HUONG-DAN-VIET-REPORT-TUNG-CUNG.md`: hướng dẫn định dạng report từng cung.
- `data/huong/la-so-huong-2000-11-27.md`: text trích từ DOM trang aituvi.com, không có JSON. Chạy script bằng `--duong-lich 2000-11-27 --gio Dậu --gioi nu`.

## 2. Ý nghĩa trường trong `.data.json`

| Trường | Ý nghĩa | Trạng thái |
|---|---|---|
| `position` | Chỉ số địa chi cộng 1 (Tý = 1) | Đã kiểm |
| `cycles.majorAge` | Tuổi âm bắt đầu đại hạn tại cung | Script kiểm |
| `cycles.annualBranch` | **Nhãn tiểu hạn:** năm mang chi này thì tiểu hạn đóng tại cung. **Không phải** "chi xung" (S#10) | Script kiểm |
| `cycles.monthlyIndex` | Tháng âm có nguyệt hạn tại cung trong năm xem của file, theo phép Việt (khởi từ cung tiểu hạn) | Script kiểm |
| `stars[].dignity` | Độ sáng theo bảng của phần mềm | Không kiểm được (C§8) |
| `stars[].nature` | Nhãn Cát/Hung/Trung tính của phần mềm | **Không dùng làm bằng chứng** |
| `restrictions.tuan` / `.triet` | Tuần / Triệt | Script kiểm |
| `reading.generatedDate` | Ngày tạo file | **Không phải mốc hạn** |

Với JSON gốc: bỏ phần tử `cungSo: 0`. `has_luangiai: false` chỉ có nghĩa API không kèm bài luận viết sẵn, không phải thiếu dữ liệu lá số.

## 3. Dữ liệu đã biết là sai

- **Mệnh chủ/Thân chủ trên aituvi.** Với Hường, aituvi hiển thị Phá Quân / Hỏa Tinh. Bộ này không khớp chi cung Mệnh (Mão → Văn Khúc), cũng không khớp chi năm sinh (Thìn → Mệnh chủ Liêm Trinh, Thân chủ Văn Xương); nó trùng đúng với chi Ngọ, tức năm xem 2026. Không dùng; script tự tính.
- **Sao Đẩu Quân trong lá số gốc** được phần mềm an từ chi năm sinh. Nguyệt hạn năm xem xem ở output script.

## 4. Ghi chú từng người

| Người | Tình trạng |
|---|---|
| Hoàng Phạm Huy | Giờ sinh 10:20 đã xác minh: canh Tỵ, cách mốc gần nhất 40 phút. Script khớp 104 sao, không lệch; majorAge, annualBranch, monthlyIndex, Tuần/Triệt khớp cả 12 cung. Chưa kiểm nghiệm ngược |
| Hường | Chỉ biết canh Dậu (aituvi nhập theo khoảng 17h–18h59), không có phút, nên không kiểm được giờ ranh (Q§4.2c). Script khớp 103 sao với text aituvi. Mệnh chủ/Thân chủ trên aituvi sai (D§3). Chưa kiểm nghiệm ngược |
