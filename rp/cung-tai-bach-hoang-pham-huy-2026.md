# Luận Cung Tài Bạch và tam phương tứ chính — Hoàng Phạm Huy

## Phạm vi

- **Người, dữ liệu:** Hoàng Phạm Huy, nam, sinh 12/12/2000 lúc 10:20. Nguồn: `data/hoang/tuvi-hoang-pham-huy-2026.data.json`.
- **Cung xét:** Tài Bạch tại Kỷ Mão. Tam hợp: Mệnh (Quý Mùi), Quan Lộc (Đinh Hợi). Xung chiếu: Phúc Đức (Ất Dậu). Giáp: Dần, Thìn. Liên quan thêm theo L§2: Điền Trạch (Bính Tuất).
- **Phạm vi hành vi:** cách tạo nguồn thu, định giá công sức, chi tiêu và giữ tiền. Report không dự đoán giàu nghèo, số tiền, nghề hay năm cụ thể.
- **Lớp:** chỉ luận lá số gốc. Câu hỏi không có yếu tố thời gian nên không luận hạn (Q§0.3). Dữ kiện để luận sau, **chưa luận**: đại hạn 23–32 tuổi âm đóng ở Phúc Đức (Dậu), là cung xung chiếu Tài Bạch, nên theo L§6.4 lớp đại hạn hiện tại có kích hoạt Tài Bạch; đại hạn cung chức Tài Bạch ở Tỵ; Tứ Hóa đại hạn can Ất (tùy phái) cho Thiên Lương hóa Quyền ngay tại Mão.
- **Giới hạn chung:** Tử vi không phải phương pháp khoa học đã được kiểm chứng. Report mô tả xu hướng theo quy tắc của tử vi đẩu số, không phải lời khuyên tài chính. Không dùng report này làm căn cứ duy nhất cho quyết định đầu tư, vay, cho vay hay đổi việc (Q§6).

## 0. Kiểm định

- **Input:** 12/12/2000, 10:20, UTC+7 → âm lịch 17/11 năm Canh Thìn, canh Tỵ. Cách mốc chuyển canh gần nhất 40 phút, không phải giờ ranh. Giờ sinh đã được xác minh (D§4).
- **Script** `kiem-tra-la-so.py --nam-xem 2026 --cung "Tài Bạch"`: khớp 104 sao, lệch 0. `majorAge`, `annualBranch`, `monthlyIndex`, Tuần, Triệt, tên cung khớp cả 12 cung. Không có dòng ❌.
- **Hai dòng ⚠️** đều là khác biệt phái của can Canh: Tứ Hóa và Khôi–Việt. Đã thử phái còn lại trong từng kết luận (mục 11). Khôi–Việt theo sách Trung Hoa (Sửu/Mùi) chỉ thêm Thiên Việt vào Mệnh, không đổi kết luận nào.
- **Phái đang dùng:** Tam hợp phái. Tứ Hóa can Canh: Thái Dương hóa Lộc, Vũ Khúc hóa Quyền, Thái Âm hóa Khoa, Thiên Đồng hóa Kỵ. Khôi–Việt: Ngọ/Dần (sách Việt). Hỏa–Linh theo chiều vận; với dương nam, hai phái cho cùng vị trí.
- **Độ sáng** lấy theo bảng của phần mềm, script không kiểm (C§8). Chỗ nào dùng độ sáng đều ghi "theo phần mềm".
- **Không dùng:** nhãn `nature`; Mệnh chủ/Thân chủ của phần mềm (script tính: Mệnh chủ Vũ Khúc, Thân chủ Văn Xương); Thiên Quan và Văn Tinh ở Quan Lộc (script chưa có công thức để kiểm); `generatedDate`.
- **Tần suất nền:** số trong ngoặc là tỉ lệ lá số ngẫu nhiên có cùng đặc điểm tại cung Tài Bạch. Đặc điểm script đã in thì lấy số của script (10.000 lá số, seed 0). Đặc điểm script không in (Nhật Lương đồng cung, Kình Dương xung chiếu, số sát tinh trong tam phương…) được tính thêm trên 20.000 lá số bằng chính hàm sinh lá số ngẫu nhiên của script (seed 0).
- Nghĩa sao theo hiểu biết chung của AI, chưa đối chiếu sách.
- Chưa hiệu chỉnh bằng sự kiện thực tế.

## 1. Kết luận nhanh về Cung Tài Bạch

**Cấu trúc.** Tài Bạch sáng và sạch tại bản cung; lực làm khó đến từ bên ngoài bản cung.

- **H1:** Thái Dương và Thiên Lương đồng cung tọa thủ, cả hai Vượng (theo phần mềm). Bộ Nhật Lương đồng cung tại Tài Bạch gặp ở 1,4% lá số.
- **H2:** Hóa Lộc (Thái Dương) tọa thủ (8%), không bị Không, Kiếp, Kỵ phá. Hóa Khoa (Thái Âm) chiếu từ Quan Lộc; điểm này đổi theo phái. Không có Lộc Tồn, Hóa Quyền, Hóa Kỵ trong tam phương tứ chính.
- **H2:** Bản cung không có Tuần, Triệt. Triệt ở Mệnh (tam hợp), Tuần ở Phúc Đức (xung chiếu). Phúc Đức vô chính diệu, mượn chính bộ Nhật Lương của Tài Bạch.
- **H3:** Không có sát tinh tọa thủ. Ba sát tinh ở tam phương: Kình Dương (Hãm) xung chiếu từ Phúc Đức; Đà La (Đắc) và Hỏa Tinh (Hãm) từ Mệnh. Lục cát chỉ có Văn Khúc (Hãm) xung chiếu.
- Không có cách có tên đủ điều kiện cho Tài Bạch (mục 5).

**Kết luận.**

| Mã | Nhận định | Mức |
|---|---|---|
| TAI-01 | Hệ thống nghiêng về nguồn thu đi qua vị trí, uy tín và chuyên môn được công khai, hơn là qua giao dịch chênh lệch hay đầu cơ; nhưng một căn cứ (Hóa Khoa) đổi theo phái | Trung bình |
| TAI-02 | Có xu hướng tiền đi ra theo vai trò che chở và thể diện (đứng ra trả, cho, gánh cho người khác) nhiều hơn là được giữ lại riêng | Trung bình |
| TAI-03 | Có xu hướng các biến động tiền lớn xảy ra theo từng quyết định nhanh khi bị kích (cạnh tranh, bị thúc), hơn là tích hoặc hao dần | Trung bình |
| TAI-04 | Có xu hướng khi thu nhập đổi, nguyên nhân nằm ở quyết định của chính mình nhiều hơn là do nguồn thu bị cắt ngang từ bên ngoài | Trung bình |

## 2. Dữ liệu trực tiếp

### 2.1. Bản cung

| Mục | Dữ liệu |
|---|---|
| Vị trí | Tài Bạch tại Kỷ Mão, hành cung Mộc |
| Chính tinh | Thái Dương (Vượng, hành Hỏa), Thiên Lương (Vượng, hành Thổ) |
| Tứ Hóa tọa thủ | Hóa Lộc (trên Thái Dương) |
| Lục sát, lục cát | Không có |
| Sao khác | Hỷ Thần (vòng Bác Sĩ), Trực Phù (vòng Thái Tuế), Đế Vượng (vòng Tràng Sinh) |
| Tuần, Triệt | Không |
| Giáp | Dần (Tật Ách): Vũ Khúc hóa Quyền, Thiên Tướng, Tả Phù, Thiên Việt, Thiên Mã. Thìn (Tử Tức): Thất Sát (Hãm), Địa Kiếp (Hãm), Thiên La, Hoa Cái. Không phải cặp có tên |

### 2.2. Tam phương tứ chính

| Quan hệ | Cung | Chính tinh | Tứ Hóa | Sát, cát | Sao khác | Tuần/Triệt |
|---|---|---|---|---|---|---|
| Xung chiếu | Phúc Đức (Ất Dậu, Kim) | VCD, mượn Thái Dương, Thiên Lương từ Mão | Hóa Lộc chiếu từ Mão | Kình Dương (Hãm), Văn Khúc (Hãm) | Đào Hoa, Thiên Thọ, Nguyệt Đức, Tử Phù, Lực Sĩ, Thai | Tuần |
| Tam hợp | Mệnh (Quý Mùi, Thổ) | VCD, mượn Thiên Đồng (Hãm), Cự Môn (Hãm) từ Sửu | Hóa Kỵ (Thiên Đồng) xung chiếu Mệnh từ Sửu | Đà La (Đắc), Hỏa Tinh (Hãm) | Thiên Hình (Hãm), Phong Cáo, Thiếu Âm, Quan Phủ, Mộ | Triệt |
| Tam hợp | Quan Lộc (Đinh Hợi, Thủy) | Thái Âm (Miếu, hành Thủy) | Hóa Khoa (trên Thái Âm) | — | Hồng Loan, Thiên Riêu (Hãm), Thiên Y, Thai Phụ, Thiên Tài, Đẩu Quân, Long Đức, Tiểu Hao (Hãm), Tràng Sinh | — |

Hóa Quyền ở Dần (giáp), Hóa Kỵ ở Sửu (ngoài tam phương). Độ sáng trong hai bảng trên đều theo phần mềm.

### 2.3. Ngũ hành liên quan

- Cung Mão hành Mộc. Thái Dương hành Hỏa: Mộc sinh Hỏa, sao được cung nuôi. Thiên Lương hành Thổ: Mộc khắc Thổ, sao bị cung khắc.
- Bản mệnh Bạch Lạp Kim khắc hành cung Tài Bạch (Mộc). Mệnh–Cục: Mệnh khắc Cục.
- Thái Âm (Thủy) ở cung Hợi (Thủy): bình hòa.
- Tất cả thuộc H6. Không kết luận nào trong report dựa vào ngũ hành.

### 2.4. Bảng dữ kiện theo hạng (Q§3)

| Hạng | Dữ kiện | Vị trí so với Tài Bạch | Tần suất nền | Độ chắc dữ liệu |
|---|---|---|---|---|
| H1 | Thái Dương + Thiên Lương đồng cung (một bộ, tính một chỉ báo) | Tọa thủ | Thái Dương tọa Tài Bạch 8,5%; Thiên Lương 8,6%; đồng cung 1,4% | Vị trí: Đã kiểm. Độ sáng: Theo phần mềm |
| H2 | Hóa Lộc trên Thái Dương | Tọa thủ | 8%; Thái Dương hóa Lộc tại Tài Bạch 1,3% | Đã kiểm; cả ba bảng can Canh đều cho Thái Dương hóa Lộc |
| H2 | Hóa Khoa trên Thái Âm | Tam hợp (Quan Lộc) | Lộc tọa thủ + Khoa trong tam phương 3,1% | Đã kiểm theo phái đang dùng; đổi theo phái |
| H2 | Không có Lộc Tồn trong tam phương, nên không có Song Lộc | — | Có Lộc Tồn trong tam phương: 33% | Đã kiểm |
| H2 | Triệt tại Mệnh; Tuần tại Phúc Đức; bản cung không Tuần, Triệt | Tam hợp; xung chiếu | Mệnh gặp Triệt 16%; Phúc Đức gặp Tuần 17% | Đã kiểm |
| H2 | Phúc Đức VCD mượn Nhật Lương của Tài Bạch; Mệnh VCD | Xung chiếu; tam hợp | Mỗi cung khoảng 17% | Đã kiểm |
| H2 | Không có cách có tên đủ điều kiện (mục 5) | — | — | — |
| H3 | Kình Dương (Hãm) | Xung chiếu | 8,8% | Vị trí: Đã kiểm. Độ sáng: Theo phần mềm |
| H3 | Đà La (Đắc); cùng nhóm Lộc Tồn–Kình–Đà nên không tính riêng | Tam hợp (Mệnh) | Kình và Đà cùng trong tam phương 17% | Như trên |
| H3 | Hỏa Tinh (Hãm) | Tam hợp (Mệnh) | Từ 3 sát tinh trong tam phương: 34% (nền). Không sát tọa thủ và từ 3 sát ở tam hợp, xung chiếu: 14% | Như trên |
| H3 | Văn Khúc (Hãm), lục cát duy nhất trong tam phương | Xung chiếu | Tối đa 1 lục cát trong tam phương: 34% (nền) | Độ sáng Xương–Khúc khác nhau nhiều giữa các bảng (L§7) |
| H3 | Giáp: Dần có Tả Phù, Thiên Việt, Thiên Mã, Hóa Quyền; Thìn có Địa Kiếp. Không phải cặp có tên | Giáp | Hóa Quyền ở một bên giáp 16%; Không hoặc Kiếp ở một bên giáp 28% | Đã kiểm |
| H4 | Tại bản cung: không có | — | — | — |
| H4 | Đào Hoa (Phúc Đức); Thiên Hình (Mệnh) – Thiên Riêu (Quan Lộc) tính một; Thai Phụ (Quan Lộc) – Phong Cáo (Mệnh) tính một; Hồng Loan, Thiên Tài, Thiên Y (Quan Lộc); Thiên Thọ, Nguyệt Đức (Phúc Đức) | Tam hợp, xung chiếu | Đào Hoa hội 33%; Hồng Loan/Thiên Hỷ hội 50% | Đã kiểm |
| H5 | Đế Vượng, Hỷ Thần, Trực Phù | Tọa thủ | Đế Vượng tại Tài Bạch 8% | Đã kiểm |
| H5 | Tiểu Hao (Hãm) | Tam hợp (Quan Lộc) | Tiểu Hao hoặc Đại Hao trong tam phương 51% | Đã kiểm |
| H6 | Ngũ hành (mục 2.3); Mệnh chủ Vũ Khúc | — | — | Đã kiểm |

## 3. Chính tinh: bộ Nhật Lương tại Mão

**Thái Dương.** Theo nghĩa truyền thống, Thái Dương chủ quý (danh, địa vị, sự hiện diện công khai) hơn là chủ phú. Sao mang tính phát ra: chiếu sáng, cho đi, không giữ lại cho mình. Ở Tài Bạch, Thái Dương sáng hay được đọc là "có danh rồi mới có lợi" `[Chưa đối chiếu]`. Tại Mão, phần mềm xếp Thái Dương Vượng.

**Thiên Lương.** Theo nghĩa truyền thống, Thiên Lương là ấm tinh: che chở, gánh đỡ, giải nguy. Sao mang tính thanh, gắn với tư cách, chuyên môn và lời nói có trọng lượng. Thiên Lương ở Tài Bạch hay được đọc là không hợp cầu tài bằng đầu cơ; tiền đi qua chuyên môn hoặc qua vai trò che chở `[Chưa đối chiếu]`. Tại Mão, phần mềm xếp Thiên Lương Vượng.

**Hai sao hợp lại.** Cả hai sao cùng hướng ra ngoài: một sao làm người khác thấy mình, một sao che chở người khác. Cả hai đều không phải tài tinh (Vũ Khúc, Thiên Phủ, Thái Âm, Lộc Tồn). Vì vậy tiền trong cung này không đọc qua sao giữ tiền, mà qua sao của vị trí và tư cách. Đây là nền của TAI-01 và TAI-02.

**Về tên cách.** Thái Dương và Thiên Lương đồng cung tại Mão, nếu ở Mệnh, được sách gọi là "Nhật chiếu lôi môn" `[Chưa đối chiếu]`. Ở đây bộ sao nằm tại Tài Bạch nên không gọi tên cách (L§5.2).

**Ngũ hành (H6).** Cung Mộc nuôi Thái Dương (Hỏa) nhưng khắc Thiên Lương (Thổ). Nếu tách riêng, lực "phát ra" được cung đỡ hơn lực "che chở, giữ khuôn". Chỉ là điều chỉnh nhẹ.

## 4. Các phụ tinh/sát tinh quan trọng tại bản cung

- **Hóa Lộc (H2, trên Thái Dương).** Lộc chủ có được, trơn tru, nguồn lợi. Lộc gắn vào Thái Dương, tức gắn vào sao của danh và sự công khai, không gắn vào tài tinh. Lộc không đồng cung Địa Không, Địa Kiếp hay Hóa Kỵ, nên không thuộc dạng "Lộc bị phá" (L§4.5). Hóa Lộc tọa thủ Tài Bạch mà không có sát tinh hay Hóa Kỵ đồng cung gặp ở 4,9% lá số.
- **Đế Vượng (H5).** Mức sinh khí thịnh nhất của vòng Tràng Sinh (8% lá số có Đế Vượng tại Tài Bạch). Chỉ là sắc thái.
- **Hỷ Thần (H5, vòng Bác Sĩ).** Chủ hỷ sự, niềm vui. Sắc thái, không dựng kết luận.
- **Trực Phù (H5, vòng Thái Tuế).** AI không nắm chắc nghĩa truyền thống của sao này nên không dùng.
- **Không có** lục sát, lục cát hay trung tinh H4 nào tọa thủ. Một bản cung "mỏng" như vậy (không sát, không cát, không Tuần/Triệt) gặp ở khoảng 24% lá số, nên sự mỏng tự nó không phải nét riêng. Hệ quả cho cách đọc: tính chất của Tài Bạch gần như do bộ Nhật Lương và Hóa Lộc quyết định, còn sát tinh chỉ tác động từ tam phương.

## 5. Các bộ sao đồng cung và cơ chế phối hợp

**Nhật Lương + Hóa Lộc.** Thái Dương đưa năng lực ra chỗ người khác thấy. Thiên Lương đặt người này vào vai trò đáng tin. Hóa Lộc làm kênh đó sinh ra tiền. Cơ chế hợp lại: tiền đi theo mức độ mình **được thấy và được tin**, hơn là theo độ khéo mua bán. Mặt trái của cùng cơ chế: tiền cũng đi ra theo vai trò (TAI-02).

**Kiểm tên cách (L§5).**

| Cách | Điều kiện cốt lõi | Tại Tài Bạch | Kết quả |
|---|---|---|---|
| Dương Lương Xương Lộc `[Chưa đối chiếu]` | Thái Dương, Thiên Lương, Văn Xương, Lộc cùng hội | Có Thái Dương, Thiên Lương, Hóa Lộc; Văn Xương ở Tỵ, ngoài tam phương | Không thành cách |
| Nhật Nguyệt tịnh minh | Thái Dương, Thái Âm đều sáng, cùng chiếu cung xét | Thái Dương tọa thủ chứ không chiếu; Thái Âm chiếu từ Hợi | Không gọi tên. Nhật và Nguyệt cùng trong tam phương gặp ở 23% lá số, chỉ là nền |
| Song Lộc | Lộc Tồn và Hóa Lộc cùng tọa hoặc cùng hội | Lộc Tồn ở Thân, ngoài tam phương | Không |
| Lộc Mã giao trì | Lộc và Thiên Mã cùng tọa hoặc cùng hội | Thiên Mã ở Dần (giáp), ngoài tam phương | Không |
| Khoa Quyền Lộc hội | Ba Hóa trong tam phương | Hóa Quyền ở Dần (giáp) | Không |
| Lộc phùng Không Kiếp | Lộc đồng cung Không hoặc Kiếp | Không có | Lộc không bị phá |

## 6. Tuần, Triệt và vòng Tràng Sinh

- **Bản cung không có Tuần, Triệt.** Bộ Nhật Lương và Hóa Lộc không bị ngắt tại chỗ.
- **Tuần ở Phúc Đức (Dậu, xung chiếu).** Tuần làm chậm và làm nhẹ các sao tại Dậu: Kình Dương, Văn Khúc. Theo L§4.7, Tuần/Triệt giảm tốt của cát tinh và giảm xấu của hung tinh. Lực tranh đoạt của Kình chiếu sang Tài Bạch vì thế bị giảm, nhưng không mất.
- **Triệt ở Mệnh (Mùi, tam hợp).** Triệt làm nhẹ Đà La, Hỏa Tinh, Thiên Hình tại Mệnh, đồng thời ngắt bớt phần Mệnh góp vào tam phương của Tài Bạch.
- `[Phổ biến]` Triệt nặng ở tiền vận (khoảng trước 30 tuổi), Tuần nặng về hậu vận. Người này đang 27 tuổi âm; theo quan niệm này, Triệt ở Mệnh đang ở giai đoạn nặng, Tuần ở Phúc Đức thì chưa. Đây là điểm khác biệt phái (L§7), nên không kết luận nào dựa vào mốc tuổi này.
- **Vòng Tràng Sinh:** Đế Vượng tại Tài Bạch, Tràng Sinh tại Quan Lộc, Mộ tại Mệnh, Thai tại Phúc Đức. Các tên này đo sinh khí của cung, không mang nghĩa đen (L§4.8).

## 7. Cung xung chiếu tác động trở lại bản cung: Phúc Đức (Ất Dậu)

Phúc Đức vô chính diệu và mượn chính tinh xung chiếu, tức mượn đúng bộ Thái Dương–Thiên Lương hóa Lộc của Tài Bạch. Trục Tài Bạch–Phúc Đức vì vậy dùng chung một bộ chính tinh. Phần riêng của Phúc Đức chiếu sang Tài Bạch:

- **Kình Dương (H3, Hãm theo phần mềm).** Theo nghĩa truyền thống, Kình chủ tranh đoạt, cạnh tranh, cắt dứt, hình thương; hãm thì mặt phá rõ hơn. Chiếu vào Tài Bạch, Kình đưa yếu tố tranh giành và quyết định cứng vào chuyện tiền. Kình xung chiếu Tài Bạch gặp ở 8,8% lá số. Đây là căn cứ chính của TAI-03.
- **Văn Khúc (H3, Hãm theo phần mềm).** Chủ ngôn từ, văn chương, nghệ thuật. Độ sáng Văn Khúc khác nhau nhiều giữa các bảng (L§7), sao lại nằm dưới Tuần, nên không dựng kết luận.
- **Đào Hoa (H4).** Chủ sức hút, giao tế. H4 đứng một mình chỉ tô màu: nếu có chi tiêu cho giao tế, hình ảnh thì đó là sắc thái, không phải kết luận.
- **Thiên Thọ, Nguyệt Đức (H4), Tử Phù, Lực Sĩ (H5), Thai (Tràng Sinh):** sắc thái phụ, không dùng.

Suy đoán — chưa xác nhận: vì Phúc Đức không có chính tinh riêng mà mượn bộ Nhật Lương của Tài Bạch, cảm giác yên tâm của người này có thể gắn với việc mình có đang giữ được vai trò "người lo được" hay không. Nếu đúng, điều đó kéo theo cách chi tiền ở TAI-02.

## 8. Tam hợp thứ nhất tác động trở lại bản cung: Mệnh (Quý Mùi)

Mệnh vô chính diệu, mượn Thiên Đồng (Hãm) và Cự Môn (Hãm) từ Thiên Di, bị Hóa Kỵ (Thiên Đồng) xung chiếu. Tại Mệnh có Đà La (Đắc), Hỏa Tinh (Hãm), Thiên Hình (Hãm), gặp Triệt. Report này chỉ xét phần Mệnh chiếu sang Tài Bạch:

- **Hỏa Tinh (H3).** Chủ bộc phát, nhanh, nóng. Chiếu vào Tài Bạch, Hỏa làm quyết định về tiền dễ xảy ra nhanh khi bị kích.
- **Đà La (H3).** Chủ dây dưa, kéo dài, vướng ngầm. Đà cùng nhóm Lộc Tồn–Kình–Đà, vị trí cố định so với Kình, nên khi chấm mức chỉ tính chung một chỉ báo với Kình (Q§4.5). Về nghĩa, Đà thêm hai vế: dồn lâu trước khi quyết, và kéo dài hậu quả sau khi quyết.
- **Thiên Hình (H4).** Chủ kỷ luật, hình phạt, quy định. Cùng cặp cố định với Thiên Riêu ở Quan Lộc, tính là một chỉ báo H4, không dùng làm căn cứ.
- **Triệt** làm nhẹ ba sao trên (mục 6).
- **Hóa Kỵ xung Mệnh** (từ Sửu) nằm ngoài tam phương của Tài Bạch, chỉ ảnh hưởng gián tiếp qua Mệnh; không tính vào Tài Bạch.
- Chiều ngược lại: Hóa Lộc từ Tài Bạch và Hóa Khoa từ Quan Lộc đều tam hợp chiếu Mệnh. Script ghi ứng viên cách Minh Châu xuất hải cho Mệnh (Mệnh VCD tại Mùi, Thái Dương ở Mão, Thái Âm ở Hợi). Kiểm phá cách (Triệt, Hỏa Tinh hãm, Hóa Kỵ xung) thuộc report Mệnh, không dùng ở đây.

## 9. Tam hợp thứ hai tác động trở lại bản cung: Quan Lộc (Đinh Hợi)

- **Thái Âm (Miếu theo phần mềm).** Theo nghĩa truyền thống, Thái Âm là tài tinh thiên về tích lũy, tiền tĩnh, tài sản; tính âm, kín, đều. Đây là tài tinh duy nhất trong tam phương Tài Bạch. Vũ Khúc, Thiên Phủ và Lộc Tồn đều nằm ngoài tam phương. Đặc điểm "không có Vũ Khúc, Thiên Phủ trong tam phương" gặp ở 56% lá số nên chỉ làm nền.
- **Hóa Khoa (H2, trên Thái Âm).** Khoa chủ danh tiếng, uy tín, được biết đến. Khoa ở Quan Lộc chiếu sang Tài Bạch: uy tín trong công việc là một đầu vào của tiền. Hóa Lộc tọa thủ Tài Bạch cùng Hóa Khoa trong tam phương gặp ở 3,1% lá số.
- **Khác biệt phái ở đây quan trọng.** Với can Canh, có bảng đổi chỗ Khoa và Kỵ: Thái Âm hóa **Kỵ**, Thiên Đồng hóa Khoa. Theo bảng đó, Quan Lộc mang Hóa Kỵ chiếu vào Tài Bạch, và "uy tín công việc sinh ra tiền" chuyển thành "công việc có chỗ vướng". Một bảng khác cho Thiên Phủ hóa Khoa; khi đó tam phương Tài Bạch không có Khoa. Kết luận nào dựa vào Hóa Khoa đều phải hạ một bậc (TAI-01).
- **Tiểu Hao (H5, Hãm theo phần mềm).** Chủ hao nhỏ, chi lặt vặt. Tiểu Hao hoặc Đại Hao có mặt trong tam phương Tài Bạch ở 51% lá số, nên chỉ làm nền.
- **Hồng Loan, Thiên Riêu, Thai Phụ, Thiên Y, Thiên Tài (H4), Long Đức (H5), Đẩu Quân:** không liên quan trực tiếp tới tiền. Thiên Tài có thể đọc mở rộng là năng lực chuyên môn (nghĩa mở rộng), nhưng H4 đứng một mình nên không dựng kết luận.

## 10. Ghép tam phương tứ chính thành cấu trúc tổng thể

**Giáp (lực yếu).** Dần có Vũ Khúc hóa Quyền, Thiên Tướng, Tả Phù, Thiên Việt, Thiên Mã. Thìn có Thất Sát (Hãm), Địa Kiếp (Hãm). Không bên nào thành cặp có tên: Hữu Bật ở Tý, Thiên Khôi ở Ngọ, Địa Không ở Ngọ. "Hóa Quyền ở một bên giáp" (16%) và "Không hoặc Kiếp ở một bên giáp" (28%) đều phổ biến, và giáp không có tên là lực yếu (L§1.3, Q§3.1), nên chỉ ghi nhận.

**Điền Trạch (liên quan thêm).** Liêm Trinh (Miếu), Thiên Phủ (Vượng), theo phần mềm. Thiên Phủ là tài tinh thiên về giữ kho, nhưng Điền Trạch nằm ngoài tam phương Tài Bạch. Muốn nói về cách giữ tài sản thì cần report Điền Trạch riêng.

**Quét sao chủ đề tiền bạc trên toàn lá số (L§2).**

| Sao | Vị trí | Quan hệ với Tài Bạch |
|---|---|---|
| Hóa Lộc | Mão (Tài Bạch) | Tọa thủ |
| Lộc Tồn | Thân (Phụ Mẫu), gặp Tuần | Ngoài tam phương |
| Vũ Khúc (hóa Quyền) | Dần (Tật Ách) | Giáp |
| Thiên Phủ | Tuất (Điền Trạch) | Ngoài tam phương |
| Thái Âm (hóa Khoa) | Hợi (Quan Lộc) | Tam hợp |
| Địa Kiếp / Địa Không | Thìn (Tử Tức) / Ngọ (Huynh Đệ) | Giáp một bên / ngoài |
| Đại Hao / Tiểu Hao | Tỵ (Phu Thê) / Hợi (Quan Lộc) | Ngoài / tam hợp |
| Hóa Kỵ | Sửu (Thiên Di) | Ngoài tam phương |

**Ghép lại.**

1. Bản cung là bộ sao của danh và của vai trò che chở, mang Lộc không bị phá. Kênh vào gắn với việc được thấy, được tin (TAI-01) và ít bị ngắt tại gốc (TAI-04).
2. Cũng bộ sao đó đẩy tiền đi ra theo vai trò. Phần giữ tiền nằm ngoài bản cung: Thái Âm ở Quan Lộc, Thiên Phủ ở Điền Trạch (TAI-02).
3. Sát tinh không nằm trong cung mà đến từ Phúc Đức (Kình) và Mệnh (Đà, Hỏa). Chúng tác động vào **quyết định** về tiền, không vào nguồn tiền (TAI-03, TAI-04).
4. Tuần và Triệt làm nhẹ cả hai hướng sát tinh chiếu vào.

**Chuỗi hành vi (giả thuyết để kiểm chứng, không phải sự việc đã xảy ra).**

```text
Chuỗi A — chi theo vai trò (TAI-02)
Có người cần giúp, hoặc nhóm cần một người đứng ra trả
        ↓
Thấy mình ở vị trí "người lo được"
        ↓
Nhu cầu giữ vai trò và thể diện
        ↓
Đứng ra trả, cho, hoặc cho mượn không đặt hạn trả
        ↓
Được tin cậy hơn (nuôi lại TAI-01), nhưng tiền để dành mỏng; khoản cho mượn khó đòi

Chuỗi B — quyết định theo cú (TAI-03)
Bị thúc: giá sắp tăng, người khác đã có, bị so sánh, bị ép trả lời ngay
        ↓
Cảm giác sắp mất phần mình
        ↓
Đã cân nhắc lâu nhưng chưa chốt (Đà)
        ↓
Chốt nhanh một khoản lớn (Hỏa, Kình)
        ↓
Được việc nhanh, hoặc mất nhiều thời gian xử lý hậu quả (Đà)
```

## 11. Các khuynh hướng hành vi quan trọng

### TAI-01 Nguồn thu đi qua vị trí và uy tín công khai, hơn là qua giao dịch hay đầu cơ

- **Căn cứ:**
  - Thái Dương + Thiên Lương tọa thủ (H1, một bộ, tính một chỉ báo; đồng cung tại Tài Bạch 1,4%).
  - Hóa Lộc trên Thái Dương tọa thủ (H2; 8%; Thái Dương hóa Lộc tại Tài Bạch 1,3%).
  - Hóa Khoa trên Thái Âm chiếu từ Quan Lộc (H2, tam hợp; Lộc tọa thủ + Khoa trong tam phương 3,1%). Lộc và Khoa cùng sinh từ can năm, nhưng khoảng cách giữa Thái Dương và Thái Âm đổi theo vị trí Tử Vi, nên tính là hai chỉ báo độc lập (Q§4.5).
- **Nghĩa truyền thống → cơ chế:** Thái Dương chủ danh và sự công khai. Thiên Lương chủ tư cách, chuyên môn, không hợp đầu cơ. Lộc là kênh sinh lợi, Khoa là uy tín. Lộc bám vào sao danh, Khoa từ công việc chiếu sang. Cơ chế: thu nhập tăng khi mức độ được thấy và được tin tăng.
- **Biểu hiện:** trong công việc, thu nhập nghiêng về tăng theo bậc khi được giao vai trò có tên, được giới thiệu, được mời, hoặc khi chuyên môn được xác nhận công khai (sản phẩm đứng tên, chứng chỉ, chức danh), hơn là nhờ tìm chênh lệch giá, buôn bán ngắn hạn hay việc làm ẩn danh. Khoản thu nghiêng về loại minh bạch, có hợp đồng hoặc chức danh, hơn là loại không giấy tờ.
- **Mặt trưởng thành:** chủ động làm cho năng lực được nhìn thấy, và đàm phán thu nhập bằng uy tín. **Mặt mất cân bằng:** chờ được công nhận rồi mới đòi tiền, hoặc nhận vai trò có tên nhưng thù lao thấp vì trọng danh.
- **Phản chứng:**
  - Mệnh (tam hợp) vô chính diệu, gặp Triệt, có Hỏa Tinh hãm và Đà La: làm chậm việc "được thấy" ở tiền vận. Đây là điều chỉnh nhịp, không đổi hướng.
  - Kình Dương xung chiếu (H3): tiền cũng có thể đến qua tranh giành trực tiếp.
  - Đã tìm chỉ báo H1–H2 theo hướng "kiếm tiền trực tiếp" (Vũ Khúc, Tham Lang, Lộc Tồn trong tam phương): không thấy.
- **Thử phái:** cả ba bảng Tứ Hóa can Canh đều cho Thái Dương hóa Lộc. Hóa Khoa thì khác: một bảng cho Thái Âm hóa Kỵ (Kỵ vào tam phương, thành phản chứng H2), một bảng đưa Khoa ra khỏi tam phương. Theo hai bảng này, kết luận chỉ còn bước 5. **Kết luận đổi theo phái.**
- **Mức: Trung bình** — bước 4 của Q§4.2 cho Cao (H1 Nhật Lương, thêm hai chỉ báo H2 độc lập là Hóa Lộc và Hóa Khoa, không có phản chứng H1–H2); hạ một bậc theo Q§4.2a vì kết luận đổi khi thử bảng Tứ Hóa can Canh khác.
- **Sai nếu:** các lần thu nhập tăng rõ nhất từ khi đi làm đến từ giao dịch chênh lệch, đầu cơ hay việc không cần ai biết mình là người làm, còn các lần được giao vai trò có tên hoặc được công nhận chuyên môn không kéo theo thay đổi thu nhập.

### TAI-02 Tiền đi ra theo vai trò che chở và thể diện nhiều hơn là được giữ lại riêng

- **Căn cứ:**
  - Thái Dương + Thiên Lương tọa thủ (H1, một bộ): Thái Dương phát ra cho người khác, Thiên Lương che chở, gánh đỡ.
  - Tiểu Hao (H5) chiếu từ Quan Lộc: hao nhỏ. Vòng Bác Sĩ an theo Lộc Tồn, độc lập với vị trí chính tinh.
  - Nền, không tính thành chỉ báo: vắng tài tinh giữ tiền (Vũ Khúc, Thiên Phủ) trong tam phương (56%).
- **Nghĩa truyền thống → cơ chế:** Thái Dương là sao cho mà không giữ. Thiên Lương là sao đứng ra che chở. Đồng cung ở Tài Bạch, hai sao cùng kéo tiền theo hướng ra ngoài, gắn với vai trò "người lo được". Phần giữ tiền không có trong bản cung.
- **Biểu hiện:** khi ở vị trí người đứng ra (người lớn hơn trong nhóm, trưởng nhóm, người có thu nhập ổn định trong nhà), nghiêng về trả trước, bao, cho mượn không đặt hạn trả rõ, hơn là chia đều hoặc giữ phần của mình. Khoản chi cho người khác và cho thể diện chiếm tỉ lệ đáng kể trong tổng chi.
- **Mặt trưởng thành:** chi cho người khác có chủ đích và có trần, biến thành uy tín và quan hệ tin cậy, tức nuôi lại TAI-01. **Mặt mất cân bằng:** chi vì thể diện vượt khả năng, ngại đòi nợ, tiền để dành mỏng dù thu nhập không thấp.
- **Phản chứng:**
  - Thái Âm (Miếu theo phần mềm) ở Quan Lộc là tài tinh tích lũy, tam hợp chiếu vào Tài Bạch. Chính tinh ở tam hợp nhẹ hơn chính tinh tọa thủ (Q§3.1) nên không lật được bộ Nhật Lương, nhưng cho thấy có một đường tích lũy đi qua công việc.
  - Hóa Lộc tọa thủ: tiền vào đều có thể bù phần đi ra, nên tiền để dành mỏng không đồng nghĩa với thiếu tiền.
- **Thử phái:** Nhật Lương và Tiểu Hao không đổi. Bảng "Thái Âm hóa Kỵ" làm đường tích lũy qua Quan Lộc bị vướng, tức cùng hướng với kết luận. Bảng "Thiên Phủ hóa Khoa" không đổi gì trong tam phương. Vững qua phái.
- **Mức: Trung bình** — bước 5 của Q§4.2: có H1 cùng hướng, nhưng chỉ thêm một chỉ báo độc lập yếu (Tiểu Hao, H5), chưa đủ hai. Không hạ bậc: tính phát ra của Thái Dương không dựa vào độ sáng.
- **Sai nếu:** trong 12 tháng gần nhất, tiền chi cho người khác (bao, quà, cho mượn, hỗ trợ gia đình) dưới khoảng 1/10 tổng chi, và trong nhóm bạn hay đồng nghiệp người này thường là người đề nghị chia đều.

### TAI-03 Biến động tiền lớn xảy ra theo từng quyết định nhanh khi bị kích, hơn là tích hoặc hao dần

- **Căn cứ:**
  - Kình Dương (H3, Hãm theo phần mềm) xung chiếu từ Phúc Đức (8,8%).
  - Hỏa Tinh (H3, Hãm theo phần mềm) tam hợp từ Mệnh; độc lập với Kình.
  - Đà La (H3) tam hợp từ Mệnh: nêu nghĩa, nhưng tính chung với Kình (Q§4.5).
  - Có từ ba sát tinh trong tam phương gặp ở 34% lá số, nên chỉ làm nền. Sức phân biệt nằm ở Kình xung chiếu (8,8%) và ở tổ hợp "Hóa Lộc tọa thủ, không sát tinh tọa thủ, từ ba sát tinh ở tam hợp và xung chiếu" (1,4%).
- **Nghĩa truyền thống → cơ chế:** Kình chủ tranh đoạt, cắt dứt. Hỏa chủ bộc phát, nhanh. Đà chủ dây dưa, kéo dài. Ba sao không ở trong Tài Bạch mà ở tâm thế (Phúc Đức) và phản xạ bản thân (Mệnh), nên chúng tác động vào cách **ra quyết định** về tiền. Cơ chế: cân nhắc dồn lâu (Đà), bị kích bởi cạnh tranh hay sợ mất phần (Kình), rồi chốt nhanh (Hỏa).
- **Biểu hiện:** khi có yếu tố cạnh tranh hoặc bị thúc (giá sắp tăng, người khác đã có, bị so sánh, bị ép trả lời ngay), nghiêng về chốt một khoản chi, đầu tư hay cho mượn lớn trong thời gian ngắn, hơn là chia nhỏ và kéo dài quyết định. Thay đổi lớn trong tài chính cá nhân nghiêng về đến từ vài quyết định như vậy, hơn là từ tích lũy hay hao mòn đều qua nhiều tháng.
- **Mặt trưởng thành:** chốt đúng lúc, dám cắt lỗ, mặc cả cứng khi bị ép giá. **Mặt mất cân bằng:** mua hay đầu tư theo cú nóng, sau đó mất nhiều thời gian xử lý hậu quả.
- **Phản chứng:**
  - Tuần tại Dậu làm nhẹ Kình; Triệt tại Mùi làm nhẹ Hỏa, Đà. Đây là H2, giảm cường độ nhưng không đổi hướng.
  - Bản cung không có sát tinh.
  - Tiểu Hao (H5) ở Quan Lộc nghiêng về phương án bị loại (hao lặt vặt, dần dần). H5 không lật được H3 (Q§3.3).
- **Thử phái:** không phụ thuộc Tứ Hóa hay Khôi–Việt; Hỏa–Linh cho cùng vị trí ở cả hai phái. Cách đọc Tuần/Triệt theo tuổi khác nhau giữa các phái nhưng chỉ đổi cường độ theo giai đoạn. Vững qua phái.
- **Mức: Trung bình** — bước 2 của Q§4.2: chỉ báo mạnh nhất là H3 (Kình), có thêm một chỉ báo H3 độc lập cùng hướng (Hỏa). Lá số không đủ để nói các cú này thường được hay mất: phần đó dựa vào độ sáng Hãm của Kình, Hỏa (theo phần mềm) và bị Tuần/Triệt làm nhẹ, nên nếu nói "thường là mất" thì chỉ ở mức Thấp.
- **Sai nếu:** ba khoản chi, đầu tư hay cho mượn lớn nhất từ khi tự kiếm tiền đều được lên kế hoạch từ nhiều tuần trước và không có yếu tố bị thúc hay cạnh tranh; hoặc thay đổi lớn nhất trong tài chính cá nhân đến từ tích lũy hay hao mòn đều qua nhiều tháng.

### TAI-04 Thu nhập đổi do quyết định của chính mình nhiều hơn là do nguồn thu bị cắt ngang

- **Căn cứ:**
  - Hóa Lộc (H2) tọa thủ, không đồng cung Không, Kiếp, Kỵ hay sát tinh, không gặp Tuần/Triệt: Lộc không bị phá (4,9%).
  - Đế Vượng (H5) tọa thủ: sinh khí thịnh nhất của vòng Tràng Sinh (8%). Vòng Tràng Sinh an theo cục và chiều vận, độc lập với Hóa Lộc.
  - Nền, không tính: tam phương không có Hóa Kỵ (67%).
- **Nghĩa truyền thống → cơ chế:** Lộc gặp Không, Kiếp, Kỵ đồng cung là Lộc bị phá (L§4.5); ở đây kênh vào không có lực ngắt tại gốc. Lực phá trong tam phương (TAI-03) nằm ở Mệnh và Phúc Đức, tức ở phía người ra quyết định, không ở nguồn tiền.
- **Biểu hiện:** khi thu nhập thay đổi, nghiêng về thay đổi do chính mình chọn (đổi việc, nhận thêm việc, tự giảm việc, chi lớn) hơn là do nguồn thu bị cắt từ bên ngoài (bị cho nghỉ đột ngột, bị nợ lương, bị quỵt khoản lớn).
- **Mặt trưởng thành:** dùng sự ổn định của nguồn vào làm nền để chủ động chọn việc. **Mặt mất cân bằng:** vì nguồn vào ổn nên xem nhẹ rủi ro của các quyết định ở TAI-03.
- **Phản chứng:**
  - Kình Dương xung chiếu (H3): tranh đoạt có thể đến từ người khác, không chỉ từ quyết định của mình.
  - Địa Kiếp (Hãm) ở Thìn, giáp một bên (28%, lực yếu).
- **Thử phái:** cả ba bảng can Canh đều cho Thái Dương hóa Lộc; Đế Vượng không đổi. Vững qua phái. Độ sáng không phải căn cứ.
- **Mức: Trung bình** — bước 5 của Q§4.2: có H2 cùng hướng, nhưng chỉ thêm một chỉ báo độc lập (Đế Vượng, H5), chưa đủ hai. Thời gian đi làm tới nay còn ngắn, nên nhận định này cần thêm vài năm quan sát mới kiểm được rõ.
- **Sai nếu:** từ khi đi làm, nguồn thu chính đã bị cắt ngang ngoài ý muốn từ hai lần trở lên (bị cho nghỉ đột ngột, bị nợ lương kéo dài, bị quỵt khoản lớn), nhiều hơn số lần thu nhập đổi do chính mình chọn.

## 12. Lời khuyên xuất phát trực tiếp từ cấu trúc cung

Các lời khuyên dưới đây là cách làm việc với từng cơ chế, không phải khuyến nghị đầu tư (Q§6).

- **TAI-01 — Vì Lộc gắn vào sao của danh:** giữ một bản ghi kết quả công việc có tên mình (dự án, sản phẩm, số liệu). Khi đàm phán thu nhập, đưa bằng chứng uy tín ra trước, thay vì mặc cả bằng nhu cầu.
- **TAI-01 — Vì Mệnh gặp Triệt làm chậm việc được thấy:** không chờ người khác tự phát hiện năng lực; chủ động đề xuất nhận vai trò có tên.
- **TAI-02 — Vì Nhật Lương đẩy tiền ra theo vai trò:** đặt trước một mức "chi cho người khác" mỗi tháng. Hết mức đó thì nói thẳng là tháng này không lo thêm được.
- **TAI-02 — Vì phần giữ tiền không nằm ở bản cung mà ở Thái Âm bên Quan Lộc:** chuyển phần tích lũy tự động ngay khi nhận lương, để việc giữ tiền đi qua một cơ chế cố định gắn với công việc, không phụ thuộc quyết định từng lần.
- **TAI-02 — Vì vai trò che chở làm ngại đòi:** mọi khoản cho mượn đều ghi bằng tin nhắn, có số tiền và ngày trả.
- **TAI-03 — Vì quyết định dồn lâu rồi bật khi bị kích:** với khoản lớn hơn một ngưỡng tự đặt trước (ví dụ một tháng thu nhập), chờ ít nhất 48 giờ và viết ra ba lý do trước khi chốt. Những câu như "người khác đã có", "sắp hết suất" là tín hiệu để dừng lại, không phải để chốt.
- **TAI-03 — Vì Đà kéo dài hậu quả:** với mỗi khoản đã chốt, đặt trước một mốc xem lại và một điều kiện dừng lỗ.
- **TAI-04 — Vì nguồn vào ổn còn quyết định thì dễ bật:** khi rà soát tài chính, xem lại các quyết định lớn của chính mình trước, rồi mới tới nguồn thu.

## 13. Những điều cần kiểm chứng bằng thực tế

1. Kể lại hai lần thu nhập tăng rõ nhất từ khi đi làm. Mỗi lần gắn với việc gì: được giao vai trò có tên, được giới thiệu, chuyên môn được công nhận, hay một giao dịch, một cơ hội mua bán? (TAI-01)
2. Có lần nào bạn kiếm được một khoản đáng kể từ việc mà không ai biết bạn là người làm không? Khoản đó lớn cỡ nào so với thu nhập chính? (TAI-01, tìm phản ví dụ)
3. Trong 12 tháng gần nhất, tiền chi cho người khác (bao, quà, cho mượn, hỗ trợ gia đình) chiếm khoảng bao nhiêu phần tổng chi? (TAI-02)
4. Ba lần gần nhất đi ăn hay đi chơi theo nhóm, ai trả và trả theo cách nào? Có lần nào bạn là người đề nghị chia đều không? (TAI-02, tìm phản ví dụ)
5. Hiện có khoản cho mượn nào chưa được trả? Bạn đã nhắc chưa; nếu chưa thì vì sao? (TAI-02)
6. Với ba khoản chi, đầu tư hoặc cho mượn lớn nhất, mỗi khoản được quyết trong bao lâu, và lúc đó có yếu tố bị thúc, cạnh tranh hay so sánh không? (TAI-03)
7. Có khoản lớn nào bạn lên kế hoạch nhiều tháng rồi mới làm, không bị ai thúc không? (TAI-03, tìm phản ví dụ)
8. Sau những khoản chốt nhanh, bạn mất bao lâu để xử lý xong hậu quả (bán lại, đòi lại, trả nợ)? (TAI-03, vế Đà La)
9. Từ khi đi làm, thu nhập đã thay đổi mấy lần, và mỗi lần do bạn quyết hay do bên ngoài (bị cắt, bị nợ lương, bị quỵt)? (TAI-04)
10. Người thân hoặc bạn thân mô tả cách bạn tiêu tiền thế nào? Mô tả đó khác gì so với cách bạn tự mô tả? (chung)

## 14. Hộp bằng chứng kỹ thuật

> **Bản cung:** Tài Bạch tại Kỷ Mão, hành Mộc. Thái Dương (Vượng, Hỏa) hóa Lộc, Thiên Lương (Vượng, Thổ); Hỷ Thần, Trực Phù, Đế Vượng. Không sát, không cát, không Tuần/Triệt. Độ sáng theo phần mềm.
> **Tam hợp thứ nhất:** Mệnh tại Quý Mùi, VCD mượn Thiên Đồng, Cự Môn (Hãm), bị Hóa Kỵ xung; Đà La (Đắc), Hỏa Tinh (Hãm), Thiên Hình (Hãm); Triệt.
> **Tam hợp thứ hai:** Quan Lộc tại Đinh Hợi. Thái Âm (Miếu) hóa Khoa; Tiểu Hao (Hãm), Hồng Loan, Thiên Riêu (Hãm), Thiên Tài, Thai Phụ.
> **Đối cung:** Phúc Đức tại Ất Dậu, VCD mượn Nhật Lương của Tài Bạch; Kình Dương (Hãm), Văn Khúc (Hãm), Đào Hoa; Tuần.
> **Bộ sao trọng yếu:** Nhật Lương và Hóa Lộc tọa thủ; Hóa Khoa tam hợp (đổi theo phái); Kình Dương xung chiếu; Hỏa Tinh, Đà La tam hợp. Giáp Dần–Thìn không phải cặp có tên.
> **Tuần/Triệt và Tràng Sinh:** Tuần ở đối cung làm nhẹ Kình; Triệt ở Mệnh làm nhẹ Hỏa, Đà. Đế Vượng tại bản cung.
> **Cơ chế tổng hợp:** tiền vào theo mức được thấy và được tin, đi ra theo vai trò che chở, và biến động lớn đến từ các quyết định bị kích chứ không từ nguồn thu.
> **Yếu tố hỗ trợ:** Lộc không bị phá trên chính tinh sáng; Khoa từ công việc (theo phái đang dùng).
> **Yếu tố làm khó:** không có tài tinh giữ tiền tại bản cung; ba sát tinh chiếu từ Mệnh và Phúc Đức.
> **Độ tin cậy chung:** vị trí sao đã kiểm (104/104 sao khớp); độ sáng theo phần mềm; cả bốn nhận định hành vi ở mức Trung bình và chưa được kiểm nghiệm bằng sự kiện thực tế.

## 15. Kết luận cuối cùng

Tài Bạch của Huy là bộ Thái Dương–Thiên Lương hóa Lộc, sáng và sạch tại bản cung. Hệ thống nghiêng về kiểu kiếm tiền đi qua vị trí, uy tín và chuyên môn được công khai (TAI-01), và kiểu tiêu tiền đi ra theo vai trò người đứng ra lo (TAI-02). Chỗ cần để ý không nằm trong cung mà ở hai phía chiếu vào: Kình Dương từ Phúc Đức, Hỏa Tinh và Đà La từ Mệnh làm các quyết định tiền lớn dễ xảy ra theo cú khi bị kích (TAI-03), trong khi nguồn thu tại gốc ít bị cắt ngang (TAI-04). Cả bốn nhận định ở mức Trung bình. Các câu hỏi ở mục 13 là cách nhanh nhất để biết chúng đúng hay sai với thực tế.
