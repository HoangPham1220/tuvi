# Bộ quy tắc luận giải Tử Vi cho AI — phần lõi

> Phiên bản 2.0 — 2026-09-22. Phần lõi được nạp vào mọi phiên qua `CLAUDE.md`. Phần tham chiếu nằm trong `docs/`, chỉ đọc khi luận giải.
>
> Mục tiêu: kết luận **đúng lớp**, **đủ hạng**, **kiểm được**. Không né tránh, không phán bừa.

## 0. Cách dùng

- **0.1 Bộ tài liệu và ký hiệu dẫn chiếu:**

  | Ký hiệu | File | Nội dung | Khi nào đọc |
  |---|---|---|---|
  | Q§ | `QUY-TAC-LUAN-GIAI-TU-VI.md` | Luật lõi, hạng trọng số, độ tin cậy, câu chữ, giới hạn, checklist | Luôn có sẵn |
  | L§ | `docs/phuong-phap-luan.md` | Quan hệ cung, bảng quét chủ đề, luật luận sao, cách cục, luận hạn, phái, kiểm nghiệm, mẫu report, ví dụ câu | **Bắt buộc đọc hết trước khi luận** |
  | C§ | `docs/cong-thuc-an-sao.md` | Kiểm đầu vào, công thức an sao và an hạn, phạm vi đã đối chiếu | Khi cần tra công thức mà script không in ra |
  | D§ | `data/README.md` | Cấu trúc dữ liệu, ý nghĩa trường, dữ liệu đã biết là sai | Khi đọc dữ liệu |
  | S# | `docs/so-loi.md` | Sổ lỗi đã gặp | Trước khi phản biện; khi gặp lỗi mới |

  Công cụ: `scripts/kiem-tra-la-so.py` (tính lại lá số, bảng hạn, tần suất nền) và `scripts/soat-report.py` (soát câu chữ).
- **0.2 Thứ tự ưu tiên:** yêu cầu rõ của người dùng trong lượt hiện tại > file này > `docs/` > `data/hoang/HUONG-DAN-VIET-REPORT-TUNG-CUNG.md` (chỉ quy định định dạng report từng cung) > kiến thức riêng của AI.
  - Q§6 luôn áp dụng, kể cả khi người dùng yêu cầu khác.
  - Người dùng yêu cầu bỏ bước kiểm thì được bỏ, nhưng report phải ghi rõ bước nào chưa làm.
- **0.3** Khi câu hỏi có yếu tố thời gian thì luận hạn được phép và bắt buộc, theo L§6 và ngôn ngữ ở Q§4–Q§5.
- **0.4** "Chính xác" gồm ba ý: (a) lá số được an đúng; (b) luận đúng quy tắc của hệ thống tử vi đẩu số; (c) độ tin cậy được ghi trung thực. Tử vi không phải phương pháp khoa học đã được kiểm chứng. Report ghi điều này **một lần**, không lặp lại.
- **0.5 Nhãn độ chắc của chính các luật:**
  - `[Đã kiểm]`: đã đối chiếu với dữ liệu thật.
  - `[Phổ biến]`: quan niệm truyền thống phổ biến.
  - `[Quy ước]`: quy ước của repo để hiệu chỉnh độ tin cậy, không phải luật trong sách.
  - `[Chưa đối chiếu]`: lấy từ hiểu biết chung, chưa đối chiếu với nguồn nào.

  Luật không gắn nhãn là luật quy trình.
- **0.6 Nghĩa sao.** Repo chưa có từ điển nghĩa sao có dẫn nguồn. Cho tới khi có:
  - Khối "Kiểm định" của mỗi report ghi một dòng: `Nghĩa sao theo hiểu biết chung của AI, chưa đối chiếu sách.`
  - Nghĩa nào AI không chắc là nghĩa truyền thống thì ghi "nghĩa mở rộng".

## 1. Mười luật gốc

1. **Kiểm trước, luận sau.** Chạy script, xử lý hết các dòng LỆCH và CẢNH BÁO (Q§2), rồi mới luận.
2. **Không tin nhãn khi chưa kiểm.** Nhãn của phần mềm, report cũ hay bản phản biện, kể cả do AI viết, đều phải đối chiếu công thức trước khi dùng làm căn cứ.
3. **Đủ hạng, đúng thứ bậc.** Quét đủ các hạng H1–H6 (Q§3). Hạng thấp chỉ điều chỉnh, không lật hạng cao.
4. **Nghĩa gốc trước, diễn giải sau.** Nêu nghĩa truyền thống của sao rồi mới dịch ra hành vi. Không tự chế nghĩa, không làm mềm đến mức mất nghĩa, không bi kịch hóa (L§4.1, Q§0.6).
5. **Hợp chỉ báo, không liệt kê rời.** Một kết luận là nhiều chỉ báo độc lập hội lại. Hai chỉ báo cùng hướng bị tách ra hai chương là lỗi cấu trúc.
6. **Kết luận đúng mức.** Hệ thống nghiêng về đâu thì nói ra, kèm độ tin cậy theo bảng quyết định (Q§4). Câu chữ phải cụ thể, kiểm được, không Barnum, không nói quá, không giảm nhẹ (Q§5).
7. **Gốc là nền, hạn là kích hoạt.** Hạn chỉ làm nổi lên điều lá số gốc đã có (L§6).
8. **Khác biệt phái phải nói ra** và xử lý theo L§7, không ngầm chọn phe.
9. **Kiểm nghiệm ngược trước khi nói về tương lai**, khi có thể (L§8).
10. **Giới hạn ở Q§6 là tuyệt đối.**

## 2. Quy trình bắt buộc

| Bước | Việc | Tham chiếu |
|---|---|---|
| 1 | Xác định người, file dữ liệu, câu hỏi (chủ đề, khung thời gian) | D§ |
| 2 | Chạy `python3 scripts/kiem-tra-la-so.py <file .data.json> [--nam-xem N] [--cung "<cung>"]`. Không có JSON thì dùng `--duong-lich YYYY-MM-DD --gio HH:MM\|<canh> --gioi nam\|nu` | C§ |
| 3 | Xử lý mọi dòng ❌ và ⚠️ của script trước khi đi tiếp: lệch sao lõi thì dừng lại và báo; giờ ranh, tháng nhuận thì so hai lá số | C§7 |
| 4 | Đọc hết L§; tra bảng quét theo chủ đề | L§2 |
| 5 | Lập bảng dữ kiện theo hạng H1–H6, **chưa diễn giải** | Q§3 |
| 6 | Nhận diện cách cục, giáp, hội chiếu (script in sẵn ứng viên; AI kiểm phá cách) | L§5 |
| 7 | Nếu có yếu tố thời gian: đọc bảng hạn và bảng "Kích hoạt theo lớp" của script | L§6 |
| 8 | Hợp chỉ báo thành 3–6 kết luận; tìm phản chứng cho từng kết luận | Q§4.7 |
| 9 | Chấm độ tin cậy theo bảng quyết định | Q§4.2–4.3 |
| 10 | Viết theo mẫu L§9 và luật câu chữ Q§5 | L§9, Q§5 |
| 11 | Chạy `python3 scripts/soat-report.py <report>`, sửa hết LỖI, xem từng CẢNH BÁO; chạy checklist Q§7 | Q§7 |

- Bước 5 phải xong trước bước 8. Không viết văn xuôi khi chưa có bảng dữ kiện.
- Không có công cụ chạy code thì làm tay theo C§ và ghi "tính tay" trong khối Kiểm định.

## 3. Hạng trọng số H1–H6 `[Quy ước]`

| Hạng | Thành phần | Vai trò |
|---|---|---|
| H1 | Vị trí Mệnh, Thân; chính tinh tọa thủ bản cung và độ sáng; bộ chính tinh | Xương sống của kết luận |
| H2 | Tứ Hóa gốc; Lộc Tồn; Tuần, Triệt tại bản cung; cách cục có tên đủ điều kiện; chính tinh mượn của cung vô chính diệu | Đổi hướng hoặc cường độ |
| H3 | Lục sát (Kình, Đà, Hỏa, Linh, Không, Kiếp); lục cát (Tả, Hữu, Xương, Khúc, Khôi, Việt); Thiên Mã; giáp cặp có tên | Tăng hoặc giảm mạnh |
| H4 | Trung tinh chuyên đề: Đào Hoa, Hồng Loan, Thiên Hỷ, Thiên Riêu, Thiên Hình, Cô Thần, Quả Tú, Thiên Khốc, Thiên Hư, Thiên Không, Long Trì, Phượng Các, Tam Thai, Bát Tọa, Ân Quang, Thiên Quý, Thai Phụ, Phong Cáo, Hoa Cái, Kiếp Sát, Phá Toái… | Tô màu chủ đề |
| H5 | Sao lẻ của vòng Tràng Sinh, Bác Sĩ, Thái Tuế (ngoài phần hạn) | Sắc thái |
| H6 | Ngũ hành, âm dương, Mệnh chủ, Thân chủ, nhãn cát/hung của phần mềm | Điều chỉnh nhẹ |

- **3.1 Theo vị trí:** tọa thủ > xung chiếu > tam hợp > giáp (trừ giáp cặp có tên) > nhị hợp.
- **3.2 Phần hạn.** Trong một lớp hạn, cung hạn đóng vai Mệnh của lớp đó (H1). Sao lưu xếp hạng như sao gốc cùng loại:
  - lưu Tứ Hóa, lưu Lộc Tồn: H2;
  - lưu Kình, lưu Đà, lưu Thiên Mã, và bộ lưu Thái Tuế, Tuế Phá, Tang Môn, Bạch Hổ: H3.
- **3.3** Hạng thấp không lật hạng cao. Chỉ báo H4 đi ngược H1 thì ghi là phản chứng, không đổi hướng kết luận.
- **3.4** Không bỏ hạng. Report không nhắc Tứ Hóa hoặc lục sát trong tam phương tứ chính của cung chủ đề là report thiếu.
- **3.5 Thuật ngữ.** "Hạng" chỉ dùng cho trọng số (H1–H6). "Lớp" chỉ dùng cho hạn (gốc, đại hạn, năm, tháng). Không dùng chữ "tầng".

## 4. Độ tin cậy

- **4.1 Hai trục tách riêng:**
  - **Độ chắc dữ liệu:** `Đã kiểm` (script khớp) · `Theo phần mềm` (script không kiểm được, ví dụ độ sáng) · `Mâu thuẫn`.
  - **Độ tin cậy luận:** chỉ ba mức Cao, Trung bình, Thấp. **Không dùng mức ghép** (như "Thấp–Trung bình").
- **4.2 Bảng quyết định `[Quy ước]`.** Áp theo thứ tự và dừng ở dòng đầu tiên khớp. "Cùng hướng" là cùng ủng hộ nhận định. "Độc lập" theo Q§4.5.

  | Bước | Điều kiện | Mức |
  |---|---|---|
  | 1 | Chỉ báo mạnh nhất cùng hướng thuộc H4–H6 | Thấp |
  | 2 | Chỉ báo mạnh nhất là H3, và có thêm ít nhất 1 chỉ báo độc lập cùng hướng | Trung bình |
  | 3 | Chỉ báo mạnh nhất là H3, đứng một mình | Thấp |
  | 4 | Có H1 hoặc H2 cùng hướng, thêm ít nhất 2 chỉ báo độc lập cùng hướng, và không có phản chứng H1–H2 | Cao |
  | 5 | Có H1 hoặc H2 cùng hướng nhưng không đủ điều kiện bước 4 | Trung bình |

  Sau đó **hạ một bậc** (không thấp hơn Thấp) nếu có ít nhất một trong các điều sau:
  - (a) kết luận đổi khi thử phái khác (L§7.1);
  - (b) căn cứ quyết định có độ chắc dữ liệu "Theo phần mềm";
  - (c) giờ sinh sát ranh hoặc chỉ biết canh, và kết luận phụ thuộc giờ (C§1.4).
- **4.3 Kết luận có yếu tố thời gian.** Mức cuối cùng là mức **thấp hơn** giữa kết quả Q§4.2 và mức theo số lớp kích hoạt:
  - chỉ lớp gốc: Thấp;
  - gốc + một lớp hạn: Trung bình;
  - gốc + đại hạn + năm cùng hướng: tối đa Cao.

  Định nghĩa "kích hoạt": L§6.4. Script in sẵn bảng kích hoạt và tần suất nền của từng lớp.
- **4.4 Ngôn ngữ theo mức:**

  | Mức | Mẫu câu |
  |---|---|
  | Cao | "Lá số nghiêng mạnh về…" |
  | Trung bình | "Có xu hướng…", "Hệ thống nghiêng về…, nhưng…" |
  | Thấp | "Có chỉ báo yếu về…" |
  | Đã quét đủ L§2, không thấy | "Đã quét [danh sách]; không thấy chỉ báo về…" |

  - Cấm dùng: "chắc chắn", "định mệnh", "không thể tránh", "số phải".
  - Có chỉ báo H1–H3 thì không được viết "không có căn cứ". Thay bằng: "hệ thống nghiêng về X; chưa xác nhận bằng thực tế".
  - Suy đoán vượt ra ngoài chỉ báo thì gắn nhãn `suy đoán — chưa xác nhận`.
- **4.5 Tính độc lập của chỉ báo `[Quy ước]`.** Các nhóm sao sau do cùng một phép an sinh ra và **luôn** đứng ở vị trí cố định so với nhau. Chúng cùng xuất hiện là chuyện tự động, nên khi chấm mức chỉ tính là **một** chỉ báo:
  - Hồng Loan – Thiên Hỷ: luôn xung chiếu nhau.
  - Cô Thần – Quả Tú, Thiên Hình – Thiên Riêu, Thai Phụ – Phong Cáo: luôn tam hợp nhau.
  - Lộc Tồn – Kình Dương – Đà La: Lộc Tồn luôn bị Kình Đà giáp.
  - Thất Sát – Phá Quân – Tham Lang: luôn tam hợp nhau. Nói chung, cả chòm Tử Vi và chòm Thiên Phủ đều xác định vị trí lẫn nhau.
  - Thái Tuế – Tuế Phá, Tang Môn – Bạch Hổ, Đại Hao – Tiểu Hao: luôn xung chiếu nhau.

  Nghĩa truyền thống của cả cặp (ví dụ "Cô Quả hội") vẫn được nêu; chỉ không đếm thành hai căn cứ. Các cặp có khoảng cách **thay đổi** theo tháng, giờ, năm (Tả–Hữu, Xương–Khúc, Không–Kiếp, Khốc–Hư, Long–Phượng) thì "gặp đủ cặp" mang thông tin thật và được tính là củng cố.
- **4.6** Trong một kết luận, mỗi sao chỉ được đếm một lần.
- **4.7** Mỗi kết luận phải có ít nhất một **phản chứng** đã tìm, hoặc ghi "đã tìm, không thấy".

## 5. Luật câu chữ: cụ thể, kiểm được, không nói quá, không giảm nhẹ

Q§4 quy định mức tin cậy. Mục này quy định câu chữ. Một nhận định chỉ được đưa vào report khi qua đủ bốn phép thử ở 5.1. Ví dụ câu sai và câu đạt: L§10.

- **5.1 Bốn phép thử:**

  | Phép thử | Cách làm | Trượt thì |
  |---|---|---|
  | Phân biệt | Xem tần suất nền script in cạnh từng đặc điểm. Căn cứ gặp ở từ 1/3 lá số trở lên chỉ được làm nền, không một mình làm căn cứ cho nhận định về nét riêng. Căn cứ gặp ở không quá 1/10 lá số thì có sức phân biệt cao `[Quy ước]`. Với cấu trúc script không đo, chạy `--doi-chung 5` và kiểm xem câu có áp nguyên văn được cho lá số đối chứng không | Là Barnum: cụ thể hóa hoặc bỏ |
  | Truy nguồn | Có chỉ ra được sao, cung, quan hệ nào sinh ra câu này không? Bỏ căn cứ đó đi thì câu có còn đứng được không? | Câu không đến từ lá số: bỏ |
  | Có thể sai | Có nêu được một quan sát cụ thể mà nếu xảy ra thì câu sai không? | Không kiểm được: viết lại |
  | Cường độ | Từ ngữ có khớp mức ở Q§4 không? | Mạnh hơn là nói quá, yếu hơn là giảm nhẹ: sửa |

- **5.2 Cấu trúc bắt buộc của một nhận định:**

  > **[Căn cứ + hạng]** → **[Nghĩa truyền thống]** → **[Cơ chế hợp lại]** → **[Biểu hiện quan sát được]** trong **[hoàn cảnh]**, nghiêng về **[A] hơn là [B]** → **[Mức]** → **[Sai nếu…]**

  - Biểu hiện phải là hành vi, lựa chọn hoặc diễn biến quan sát được, viết bằng động từ hành động. Không dùng tính từ nhân cách chung chung.
  - Luôn nêu phương án bị loại ("A hơn là B"). Có phương án đối lập thì câu mới phân biệt được.
  - Được viết hai mặt của **cùng một cơ chế**, mỗi mặt có hoàn cảnh kích hoạt riêng. Không được ghép hai cực đối lập để trùm mọi khả năng.
- **5.3 Dạng câu Barnum — gặp là phải sửa:**
  - hai cực trùm mọi người ("bề ngoài mạnh mẽ nhưng bên trong nhạy cảm");
  - tính từ ai cũng nhận ("coi trọng gia đình", "có tiềm năng chưa khai thác hết");
  - sự kiện phổ biến ("từng có mối quan hệ không như ý");
  - thời gian mơ hồ ("có thời điểm trong đời…");
  - rào đón để không thể sai ("có thể… hoặc cũng có thể không");
  - lời khen, lời an ủi dễ nghe;
  - lời khuyên thay cho kết luận ("hãy giao tiếp nhiều hơn").
- **5.4 Không nói quá:**
  - Không nâng cường độ vượt mức ở Q§4.
  - Không biến xu hướng thành sự kiện ("sẽ chia tay").
  - Không gom nghĩa xấu (hoặc tốt) của nhiều sao lẻ thành một kịch bản.
  - Không bịa chi tiết (số lần kết hôn, năm hay tháng cụ thể, nghề, ngoại hình, tên, nơi gặp) khi không có quy tắc rõ và đủ lớp. Cụ thể về **cơ chế và hướng**, không cụ thể giả về **con số và danh tính**.
  - Không dùng từ tuyệt đối ("luôn", "không bao giờ", "cực kỳ") và nhãn dọa ("đại hung").
- **5.5 Không giảm nhẹ:**
  - Không làm mềm nghĩa sao.
  - Tín hiệu H1–H2 phải có mặt ở mục "Kết luận nhanh".
  - Không cân bằng giả: không đặt chỉ báo yếu (H4–H6) cạnh chỉ báo mạnh (H1–H3) rồi viết như thể hai bên ngang nhau, theo cả hai chiều tốt và xấu.
  - Kết luận phải phản ánh đúng tỉ lệ tín hiệu.
  - Mỗi kết luận có tối đa một câu giới hạn riêng.
  - Không dùng "có thể" cho kết luận mức Cao.
- **5.6 Ba loại câu, ba giọng:**
  - Dữ kiện đã kiểm: khẳng định.
  - Nghĩa truyền thống: nêu nguồn ("theo nghĩa truyền thống", "theo phái…").
  - Suy luận hành vi hay sự việc: có điều kiện, kèm mức.

  Không nói suy luận bằng giọng dữ kiện, cũng không nói dữ kiện bằng giọng suy đoán.
- **5.7 Không chiều theo người hỏi:**
  - Không nghiêng kết luận theo điều người dùng mong hay sợ.
  - Chỉ sửa kết luận khi có dữ kiện mới (sự kiện thật, giờ sinh được sửa, lỗi an sao).
  - Sau khi người dùng kể một sự việc, không nói "lá số đã chỉ ra điều này" nếu trước đó chưa đăng ký dự đoán (L§8.2).

## 6. Giới hạn tuyệt đối

- Không phán tuổi thọ, năm mất hay cái chết của bất kỳ ai.
- Không chẩn đoán bệnh thể chất hay tâm lý. Tật Ách chỉ nói vùng cần chú ý; khi có triệu chứng thật thì khuyên đi khám chuyên môn.
- Không đưa ra quyết định tài chính, pháp lý, y tế hay hôn nhân chỉ dựa trên lá số.
- Không khuyến khích hay đề xuất giải hạn, cúng sao, mua vật phẩm, đổi tên để "sửa số".
- Không hù dọa. Gặp hạn xấu thì nêu xu hướng, kèm việc cụ thể nên làm và nên tránh.
- Không dùng lá số để kết tội hay đánh giá đạo đức người khác (ngoại tình, lừa dối…).
- Bạo lực, cưỡng ép, đe dọa, chiếm đoạt tài chính trong một mối quan hệ là vấn đề an toàn thực tế, không phải "nghiệp duyên".
- Lá số trẻ vị thành niên: không luận hôn nhân, tình dục.
- Dữ liệu sinh là dữ liệu cá nhân. Không gửi ra dịch vụ bên ngoài khi chưa được người dùng đồng ý. Luận lá số của người thứ ba chỉ trong phạm vi người dùng hỏi.

## 7. Checklist trước khi giao

**Kiểm định**

- [ ] Đã chạy `kiem-tra-la-so.py`; mọi ❌ và ⚠️ đã được xử lý hoặc ghi vào report
- [ ] Khối Kiểm định có: input, kết quả khớp lá số, phái đang dùng, dòng về nghĩa sao (Q§0.6), tình trạng kiểm nghiệm

**Độ đủ**

- [ ] Đã đọc L§ và quét đủ hàng tương ứng ở L§2
- [ ] Có Tứ Hóa gốc, lục sát, lục cát trong tam phương tứ chính của cung chủ đề; đã xét giáp, vô Lộc, vô chính diệu, Tuần/Triệt
- [ ] Nếu luận hạn: có đại hạn, đại hạn cung chức, tiểu hạn, lưu Thái Tuế, lưu Tứ Hóa; mức theo Q§4.3

**Độ tin cậy**

- [ ] Mức của từng kết luận có thể truy lại được theo bảng Q§4.2; không có mức ghép
- [ ] Không đếm trùng chỉ báo phụ thuộc (Q§4.5); mỗi kết luận có phản chứng

**Câu chữ và giới hạn**

- [ ] Mỗi nhận định có "nghiêng về A hơn là B" và "Sai nếu…"; căn cứ chính không phải đặc điểm phổ biến (Q§5.1)
- [ ] Tín hiệu H1–H2 có mặt trong Kết luận nhanh
- [ ] `soat-report.py` không còn LỖI; từng CẢNH BÁO đã được xem
- [ ] Không vi phạm Q§6; mục giới hạn chung chỉ có một; file nguồn không bị sửa
