# Công thức an sao và kiểm đầu vào (C§)

> Tham chiếu của `QUY-TAC-LUAN-GIAI-TU-VI.md`. `scripts/kiem-tra-la-so.py` cài đặt đúng các công thức trong file này. Sửa công thức thì sửa cả hai, rồi chạy lại script trên mọi lá số trong `data/`.

## 1. Kiểm đầu vào

Script tự làm các mục 1.2, 1.4 (giờ ranh, giờ Tý), 1.5 và 1.6. AI chỉ cần đọc mục "Đầu vào" trong output của script.

- **1.1 Dữ liệu cần đủ:** ngày sinh dương lịch, giờ sinh (giờ và phút), nơi sinh hoặc múi giờ, giới tính dùng khi lập lá số, năm xem.
- **1.2 Lịch** `[Đã kiểm]`. Dùng âm lịch Việt Nam (UTC+7). Âm lịch Việt Nam và Trung Quốc có năm lệch ngày, thậm chí lệch cả tháng (Tết 1985: Việt Nam 21/01, Trung Quốc 20/02). Script đổi dương lịch sang âm lịch bằng thuật toán Hồ Ngọc Đức, đã thử đúng trên 7 ngày, gồm tháng nhuận năm 2020 và 2023.
- **1.3 Ranh năm.** Năm tử vi đổi vào mồng 1 Tết âm lịch, không phải ngày 1/1 dương lịch và không phải tiết Lập Xuân (Lập Xuân là ranh năm của Bát Tự).
- **1.4 Giờ sinh.**

  | Canh | Giờ đồng hồ | Canh | Giờ đồng hồ |
  |---|---|---|---|
  | Tý | 23:00–00:59 | Ngọ | 11:00–12:59 |
  | Sửu | 01:00–02:59 | Mùi | 13:00–14:59 |
  | Dần | 03:00–04:59 | Thân | 15:00–16:59 |
  | Mão | 05:00–06:59 | Dậu | 17:00–18:59 |
  | Thìn | 07:00–08:59 | Tuất | 19:00–20:59 |
  | Tỵ | 09:00–10:59 | Hợi | 21:00–22:59 |

  - **Giờ ranh:** giờ sinh cách mốc chuyển canh không quá 15 phút `[Quy ước]`, hoặc là giờ khai tròn (09:00, 11:00…). Script tự in lá số của canh lân cận kèm danh sách sao lõi thay đổi. Giờ đổi làm Mệnh đổi, Mệnh đổi có thể làm cục đổi, cục đổi làm **cả 14 chính tinh** có thể dời chỗ.
  - **Chỉ biết canh, không biết phút:** chạy với `--gio <canh>`. Không kiểm được giờ ranh, nên mọi kết luận phụ thuộc giờ bị hạ một bậc (Q§4.2c).
  - **Giờ Tý đêm (23:00–23:59):** các phái khác nhau ở chỗ có tính sang ngày hôm sau hay không. Nếu hai cách cho Tử Vi ở hai vị trí khác nhau thì lập cả hai lá số.
  - **Giờ mặt trời thực:** phần lớn phần mềm Việt Nam dùng giờ đồng hồ. Một số phái hiệu chỉnh theo kinh độ (Hà Nội cộng khoảng 3,4 phút, TP.HCM cộng khoảng 6,8 phút so với kinh tuyến 105°Đ). Nếu hiệu chỉnh làm đổi canh thì báo và lập hai lá số.
- **1.5 Múi giờ lịch sử** `[Đã kiểm với tzdb]`. Script tra múi giờ pháp định lúc sinh theo tzdb `Asia/Ho_Chi_Minh`. Cơ sở dữ liệu này theo lịch sử Sài Gòn: UTC+8 trong giai đoạn trước 1975. Người sinh ở miền Bắc trước 1976 phải tra riêng. Giờ khai sinh theo UTC+8 thì quy đổi về UTC+7 trước khi tra canh, và ghi rõ phép quy đổi.
- **1.6 Tháng nhuận.** Có hai quy ước: an như tháng chính liền trước, hoặc chia đôi (ngày 1–15 tính tháng trước, từ ngày 16 tính tháng sau). Script in lá số theo quy ước chia đôi khi nó khác quy ước còn lại.
- **1.7 Tuổi** dùng tuổi âm: `năm xem − năm sinh âm + 1`.
- **1.8** Ghi kết quả kiểm thành một dòng trong khối Kiểm định của report.

## 2. Quy ước tính

- Chỉ số địa chi (đếm từ 0): Tý 0, Sửu 1, Dần 2, Mão 3, Thìn 4, Tỵ 5, Ngọ 6, Mùi 7, Thân 8, Dậu 9, Tuất 10, Hợi 11. Mọi phép tính lấy mod 12. "Thuận" là tăng chỉ số, "nghịch" là giảm. Trường `position` trong `.data.json` bằng chỉ số cộng 1.
- Ký hiệu: `m` = tháng âm; `d` = ngày âm; `h` = chỉ số canh giờ; `y` = chỉ số chi năm sinh; `c` = chỉ số can năm sinh (Giáp 0 … Quý 9); `n` = số cục.
- Can và chi của năm âm: `c = (năm + 6) mod 10`, `y = (năm + 8) mod 12`.
- **Chiều vận:** can năm dương (Giáp, Bính, Mậu, Canh, Nhâm) với nam, hoặc can năm âm với nữ, đi **thuận**; âm nam và dương nữ đi **nghịch**. Chiều vận dùng cho đại hạn, Tràng Sinh, vòng Bác Sĩ, Hỏa–Linh. Tiểu hạn đi theo giới (C§6.3).

## 3. Bảng công thức

Cột "Đã đối chiếu" ghi trường hợp đã khớp với dữ liệu phần mềm. Hai lá số trong repo đều sinh năm **Canh Thìn, tháng 11** (Huy: nam, giờ Tỵ, ngày 17; Hường: nữ, canh Dậu, ngày 2). Vì vậy phần lớn các dòng mới chỉ được kiểm ở đúng trường hợp đó; các trường hợp khác là `[Chưa đối chiếu]`. Xem C§9.

| Hạng mục | Công thức | Đã đối chiếu |
|---|---|---|
| Mệnh / Thân | `m + 1 − h` / `m + 1 + h`. Thân luôn rơi vào Mệnh, Phúc Đức, Quan Lộc, Thiên Di, Tài Bạch hoặc Phu Thê | 2 lá số |
| 12 cung | Từ Mệnh đi thuận: Mệnh, Phụ Mẫu, Phúc Đức, Điền Trạch, Quan Lộc, Nô Bộc, Thiên Di, Tật Ách, Tài Bạch, Tử Tức, Phu Thê, Huynh Đệ | 2 lá số |
| Can cung | Can của cung Dần theo can năm: Giáp/Kỷ → Bính; Ất/Canh → Mậu; Bính/Tân → Canh; Đinh/Nhâm → Nhâm; Mậu/Quý → Giáp. Can tăng dần từ Dần tới Hợi; Tý và Sửu trùng can với Dần và Mão | Can Canh |
| Cục | Nạp âm của can–chi cung Mệnh (C§5): Thủy 2, Mộc 3, Kim 4, Thổ 5, Hỏa 6 | Mộc 3, Thổ 5 |
| Tử Vi | `q = ⌈d / n⌉`, `r = q·n − d`, `g = q + 1`. r chẵn: `g + r`; r lẻ: `g − r` | Nhánh r lẻ (2 lá số); nhánh r chẵn chưa đối chiếu |
| Chòm Tử Vi | Thiên Cơ TV−1, Thái Dương TV−3, Vũ Khúc TV−4, Thiên Đồng TV−5, Liêm Trinh TV−8 | 2 lá số |
| Thiên Phủ và chòm | Thiên Phủ `4 − TV`; Thái Âm TP+1, Tham Lang TP+2, Cự Môn TP+3, Thiên Tướng TP+4, Thiên Lương TP+5, Thất Sát TP+6, Phá Quân TP+10 | 2 lá số |
| Lộc Tồn / Kình / Đà | Lộc Tồn: Giáp Dần; Ất Mão; Bính, Mậu Tỵ; Đinh, Kỷ Ngọ; Canh Thân; Tân Dậu; Nhâm Hợi; Quý Tý. Kình LT+1, Đà LT−1 | Can Canh |
| Văn Xương / Văn Khúc | `10 − h` / `4 + h` | Giờ Tỵ, Dậu |
| Tả Phù / Hữu Bật | `m + 3` / `11 − m` | Tháng 11 |
| Địa Kiếp / Địa Không | `11 + h` / `11 − h` | Giờ Tỵ, Dậu |
| Hỏa / Linh — điểm khởi | Dần Ngọ Tuất: Sửu / Mão; Thân Tý Thìn: Dần / Tuất; Tỵ Dậu Sửu: Mão / Tuất; Hợi Mão Mùi: Dậu / Tuất | Nhóm Thân Tý Thìn |
| Hỏa / Linh — chiều | Chiều vận thuận: Hỏa = khởi + h, Linh = khởi − h. Chiều vận nghịch: Hỏa = khởi − h, Linh = khởi + h | Cả hai chiều |
| Thiên Khôi / Thiên Việt | Giáp, Mậu: Sửu/Mùi; Ất, Kỷ: Tý/Thân; Bính, Đinh: Hợi/Dậu; Nhâm, Quý: Mão/Tỵ; Tân: Ngọ/Dần; Canh: Ngọ/Dần (sách Việt; sách Trung Hoa: Sửu/Mùi) | Can Canh |
| Thiên Mã / Đào Hoa | Mã: Dần Ngọ Tuất → Thân; Thân Tý Thìn → Dần; Tỵ Dậu Sửu → Hợi; Hợi Mão Mùi → Tỵ. Đào Hoa: Thân Tý Thìn → Dậu; Dần Ngọ Tuất → Mão; Tỵ Dậu Sửu → Ngọ; Hợi Mão Mùi → Tý | Nhóm Thân Tý Thìn |
| Hoa Cái / Kiếp Sát | Hoa Cái: Thân Tý Thìn → Thìn; Tỵ Dậu Sửu → Sửu; Dần Ngọ Tuất → Tuất; Hợi Mão Mùi → Mùi. Kiếp Sát: Thân Tý Thìn → Tỵ; Tỵ Dậu Sửu → Dần; Dần Ngọ Tuất → Hợi; Hợi Mão Mùi → Thân | Nhóm Thân Tý Thìn |
| Hồng Loan / Thiên Hỷ | `3 − y` / Hồng Loan + 6 | Năm Thìn |
| Cô Thần / Quả Tú | Hợi Tý Sửu: Dần/Tuất; Dần Mão Thìn: Tỵ/Sửu; Tỵ Ngọ Mùi: Thân/Thìn; Thân Dậu Tuất: Hợi/Mùi | Nhóm Dần Mão Thìn |
| Thiên Hình / Thiên Riêu (= Thiên Y) | `m + 8` / `m` | Tháng 11 |
| Thiên Khốc / Thiên Hư | `6 − y` / `6 + y` | Năm Thìn |
| Long Trì / Phượng Các (= Giải Thần) | `4 + y` / `10 − y` | Năm Thìn |
| Thiên Không / Nguyệt Đức / Thiên Đức | `y + 1` / `5 + y` / `9 + y` | Năm Thìn |
| Phá Toái | Tý Ngọ Mão Dậu → Tỵ; Dần Thân Tỵ Hợi → Dậu; Thìn Tuất Sửu Mùi → Sửu | Năm Thìn |
| Thiên Giải / Địa Giải | `m + 7` / `m + 6` | Tháng 11 |
| Tam Thai / Bát Tọa | Tả Phù + (d − 1) / Hữu Bật − (d − 1) | Ngày 2, 17 |
| Ân Quang / Thiên Quý | Văn Xương + (d − 2) / Văn Khúc − (d − 2) | Ngày 2, 17 |
| Thai Phụ / Phong Cáo | Văn Khúc + 2 / Văn Khúc − 2 | 2 lá số |
| Thiên Tài / Thiên Thọ | Mệnh + y / Thân + y | 2 lá số |
| Quốc Ấn / Đường Phù | LT + 8 / LT − 7 | Can Canh, cả hai chiều vận |
| Đẩu Quân (sao gốc) | `y − (m − 1) + h` | 2 lá số |
| Thiên La / Địa Võng; Thiên Thương / Thiên Sứ | Thìn / Tuất; Nô Bộc / Tật Ách | 2 lá số |
| Tuần | `s = y − c`; Tuần tại `s − 2` và `s − 1` | Canh Thìn |
| Triệt | Giáp, Kỷ: Thân Dậu; Ất, Canh: Ngọ Mùi; Bính, Tân: Thìn Tỵ; Đinh, Nhâm: Dần Mão; Mậu, Quý: Tý Sửu | Can Canh |
| Tràng Sinh | Khởi: Thủy 2 và Thổ 5 tại Thân; Mộc 3 tại Hợi; Kim 4 tại Tỵ; Hỏa 6 tại Dần. Đi theo chiều vận: Tràng Sinh, Mộc Dục, Quan Đới, Lâm Quan, Đế Vượng, Suy, Bệnh, Tử, Mộ, Tuyệt, Thai, Dưỡng | Mộc 3 thuận, Thổ 5 nghịch |
| Vòng Thái Tuế | Từ chi năm sinh đi thuận: Thái Tuế, Thiếu Dương, Tang Môn, Thiếu Âm, Quan Phù, Tử Phù, Tuế Phá, Long Đức, Bạch Hổ, Phúc Đức, Điếu Khách, Trực Phù | Năm Thìn |
| Vòng Bác Sĩ | Từ Lộc Tồn đi theo chiều vận: Bác Sĩ, Lực Sĩ, Thanh Long, Tiểu Hao, Tướng Quân, Tấu Thư, Phi Liêm, Hỷ Thần, Bệnh Phù, Đại Hao, Phục Binh, Quan Phủ | Cả hai chiều |
| Mệnh chủ | Theo chi cung Mệnh: Tý Tham Lang; Sửu, Hợi Cự Môn; Dần, Tuất Lộc Tồn; Mão, Dậu Văn Khúc; Thìn, Thân Liêm Trinh; Tỵ, Mùi Vũ Khúc; Ngọ Phá Quân | Chưa đối chiếu (phần mềm sai, D§3) |
| Thân chủ | Theo chi năm sinh: Tý, Ngọ Hỏa Tinh; Sửu, Mùi Thiên Tướng; Dần, Thân Thiên Lương; Mão, Dậu Thiên Đồng; Thìn, Tuất Văn Xương; Tỵ, Hợi Thiên Cơ | Chưa đối chiếu |

Script chưa tính các sao: Thiên Quan, Thiên Phúc, Thiên Trù, Lưu Hà, Văn Tinh (chưa có công thức đã kiểm).

## 4. Tứ Hóa

Lá số gốc dùng can năm sinh; lưu niên dùng can năm xem; đại hạn (tùy phái) dùng can của cung đại hạn.

| Can | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|---|---|---|---|---|
| Giáp | Liêm Trinh | Phá Quân | Vũ Khúc | Thái Dương |
| Ất | Thiên Cơ | Thiên Lương | Tử Vi | Thái Âm |
| Bính | Thiên Đồng | Thiên Cơ | Văn Xương | Liêm Trinh |
| Đinh | Thái Âm | Thiên Đồng | Thiên Cơ | Cự Môn |
| Mậu | Tham Lang | Thái Âm | Hữu Bật | Thiên Cơ |
| Kỷ | Vũ Khúc | Tham Lang | Thiên Lương | Văn Khúc |
| Canh | Thái Dương | Vũ Khúc | Thái Âm\* | Thiên Đồng\* |
| Tân | Cự Môn | Thái Dương | Văn Khúc | Văn Xương |
| Nhâm | Thiên Lương | Tử Vi | Tả Phù\* | Vũ Khúc |
| Quý | Phá Quân | Cự Môn | Thái Âm | Tham Lang |

- Chỉ dòng Canh đã đối chiếu với dữ liệu. Các dòng khác `[Chưa đối chiếu]`.
- \* Khác biệt phái: với can Canh, có sách đổi chỗ Khoa và Kỵ, có sách cho Thiên Phủ hóa Khoa; với can Nhâm, có sách cho Thiên Phủ hóa Khoa (L§7).

## 5. Nạp âm

Dùng để tính cục (nạp âm cung Mệnh) và bản mệnh (nạp âm năm sinh). Đã đối chiếu: Bạch Lạp Kim, Dương Liễu Mộc, Thành Đầu Thổ.

| Can chi | Nạp âm | Can chi | Nạp âm | Can chi | Nạp âm |
|---|---|---|---|---|---|
| Giáp Tý, Ất Sửu | Hải Trung **Kim** | Giáp Thân, Ất Dậu | Tuyền Trung **Thủy** | Giáp Thìn, Ất Tỵ | Phú Đăng **Hỏa** |
| Bính Dần, Đinh Mão | Lư Trung **Hỏa** | Bính Tuất, Đinh Hợi | Ốc Thượng **Thổ** | Bính Ngọ, Đinh Mùi | Thiên Hà **Thủy** |
| Mậu Thìn, Kỷ Tỵ | Đại Lâm **Mộc** | Mậu Tý, Kỷ Sửu | Tích Lịch **Hỏa** | Mậu Thân, Kỷ Dậu | Đại Trạch **Thổ** |
| Canh Ngọ, Tân Mùi | Lộ Bàng **Thổ** | Canh Dần, Tân Mão | Tùng Bách **Mộc** | Canh Tuất, Tân Hợi | Thoa Xuyến **Kim** |
| Nhâm Thân, Quý Dậu | Kiếm Phong **Kim** | Nhâm Thìn, Quý Tỵ | Trường Lưu **Thủy** | Nhâm Tý, Quý Sửu | Tang Đố **Mộc** |
| Giáp Tuất, Ất Hợi | Sơn Đầu **Hỏa** | Giáp Ngọ, Ất Mùi | Sa Trung **Kim** | Giáp Dần, Ất Mão | Đại Khê **Thủy** |
| Bính Tý, Đinh Sửu | Giản Hạ **Thủy** | Bính Thân, Đinh Dậu | Sơn Hạ **Hỏa** | Bính Thìn, Đinh Tỵ | Sa Trung **Thổ** |
| Mậu Dần, Kỷ Mão | Thành Đầu **Thổ** | Mậu Tuất, Kỷ Hợi | Bình Địa **Mộc** | Mậu Ngọ, Kỷ Mùi | Thiên Thượng **Hỏa** |
| Canh Thìn, Tân Tỵ | Bạch Lạp **Kim** | Canh Tý, Tân Sửu | Bích Thượng **Thổ** | Canh Thân, Tân Dậu | Thạch Lựu **Mộc** |
| Nhâm Ngọ, Quý Mùi | Dương Liễu **Mộc** | Nhâm Dần, Quý Mão | Kim Bạch **Kim** | Nhâm Tuất, Quý Hợi | Đại Hải **Thủy** |

## 6. Công thức hạn

- **6.1 Đại hạn** `[Đã kiểm: Mộc 3 thuận, Thổ 5 nghịch]`. Khởi tại Mệnh ở tuổi âm bằng số cục, mỗi cung 10 năm, đi theo chiều vận.
- **6.2 Đại hạn cung chức.** Coi cung đại hạn là Mệnh, rồi đi thuận địa bàn: Phụ Mẫu +1, Phúc Đức +2, Điền Trạch +3, Quan Lộc +4, Nô Bộc +5, Thiên Di +6, Tật Ách +7, Tài Bạch +8, Tử Tức +9, Phu Thê +10, Huynh Đệ +11.
- **6.3 Tiểu hạn** `[Đã kiểm: nhóm Thân Tý Thìn, nam và nữ]`. Chi năm sinh được ghi tại cung khởi:
  - tuổi Dần Ngọ Tuất khởi tại Thìn; Thân Tý Thìn tại Tuất; Tỵ Dậu Sửu tại Mùi; Hợi Mão Mùi tại Sửu;
  - **nam đi thuận, nữ đi nghịch** (theo giới, không theo âm dương của can);
  - năm tuổi âm A: tiểu hạn đóng tại `khởi ± (A − 1)`.
- **6.4 Lưu niên.**
  - Lưu Thái Tuế (TT) đóng tại cung mang chi năm xem. Lưu Tang Môn TT+2, lưu Tuế Phá TT+6, lưu Bạch Hổ TT+8.
  - Lưu Lộc Tồn, Kình, Đà theo can năm xem (bảng C§3); lưu Thiên Mã theo chi năm xem.
  - Lưu Tứ Hóa theo can năm xem (C§4).
- **6.5 Nguyệt hạn** `[Đã kiểm phép Việt: tháng Giêng trên 2 lá số]`.
  - Phép Việt: từ cung tiểu hạn đi nghịch `m − 1` bước, rồi đi thuận `h` bước, được cung tháng Giêng; các tháng sau đi thuận.
  - Phép Trung Hoa (Đẩu Quân lưu niên): cách tính giống hệt nhưng khởi từ cung lưu Thái Tuế.
- **6.6 Tứ Hóa đại hạn** (tùy phái): theo can của cung đại hạn.

## 7. Khi kết quả tính lại lệch với file

- Lệch ở sao lõi (Mệnh, Thân, cục, 14 chính tinh, Tứ Hóa, Lộc Tồn, lục sát, lục cát, Tuần, Triệt): dừng lại, báo người dùng. Nguyên nhân thường gặp là giờ, ngày, tháng nhuận hoặc phái.
- Lệch do khác biệt phái đã biết (L§7): ghi rõ, luận theo dữ liệu nhưng đánh dấu những kết luận phụ thuộc điểm đó.
- Không sửa file JSON nguồn.

## 8. Độ sáng Miếu–Vượng–Đắc–Bình–Hãm

- Độ sáng không có công thức; script lấy theo file và không kiểm.
- Bảng giữa các sách khác nhau, rõ nhất ở Văn Xương, Văn Khúc và ở việc có dùng mức "Bình hòa" hay không.
- Kết luận quan trọng dựa vào độ sáng thì ghi độ chắc dữ liệu là "Theo phần mềm", và hạ một bậc theo Q§4.2b.

## 9. Phạm vi đối chiếu và việc còn thiếu

Để kiểm hết bảng C§3–C§5 cần thêm 8–10 lá số từ phần mềm, phủ các trường hợp sau:
- đủ 10 can: Tứ Hóa, Lộc Tồn, Khôi Việt, Triệt, can cung;
- đủ 4 nhóm tuổi: Hỏa Linh, Mã, Đào Hoa, Hoa Cái, Kiếp Sát, Cô Quả, tiểu hạn;
- âm nam và âm nữ;
- các tháng khác tháng 11;
- nhánh r chẵn của công thức Tử Vi;
- Thủy 2, Kim 4, Hỏa 6 cục;
- một ca tháng nhuận và một ca giờ Tý đêm.

Mỗi lá số mới: làm sạch bằng `scripts/clean-tuvi-data.ps1` (cần PowerShell), chạy `kiem-tra-la-so.py`, rồi cập nhật cột "Đã đối chiếu".
