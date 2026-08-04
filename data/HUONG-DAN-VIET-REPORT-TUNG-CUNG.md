# Hướng dẫn cho Codex: viết report luận giải chuyên sâu theo từng cung

## 1. Mục đích

Khi người dùng yêu cầu:

> Hãy luận giải cung `<TÊN CUNG>` theo hướng dẫn trong file này.

Codex phải đọc toàn bộ dữ liệu lá số, tạo một report Markdown độc lập chỉ tập trung vào cung được yêu cầu và tam phương tứ chính của cung đó.

Report phải giải thích theo mạch:

> Dữ liệu cung và sao → ý nghĩa chức năng → tác động của vị trí và trạng thái → cơ chế phối hợp → chuỗi hành vi → biểu hiện trưởng thành/mất cân bằng → lời khuyên xuất phát trực tiếp từ cơ chế.

Không viết theo kiểu chỉ liệt kê “có sao X nên có tính Y”.

## 2. Cách xác định đầu vào

### 2.1. Cung mục tiêu

Cung mục tiêu lấy từ yêu cầu của người dùng, ví dụ:

- Mệnh.
- Thiên Di.
- Quan Lộc.
- Tài Bạch.
- Phúc Đức.
- Tật Ách.
- Nô Bộc.
- Phu Thê.

Chuẩn hóa khác biệt viết hoa, dấu cách và chính tả nhỏ, nhưng không tự đổi sang một cung khác.

Nếu tên cung không tồn tại trong dữ liệu, phải báo rõ và không tạo report giả.

### 2.2. File dữ liệu

1. Tìm các file JSON lá số trong `data/`.
2. Không coi chính file hướng dẫn này là dữ liệu lá số.
3. Nếu chỉ có một JSON lá số phù hợp, tự động sử dụng file đó.
4. Nếu có nhiều JSON và yêu cầu không chỉ rõ người hoặc file, phải hỏi người dùng chọn file; không tự chọn ngẫu nhiên.
5. Đọc toàn bộ JSON trước khi phân tích.
6. Không sửa file JSON nguồn.

Với workspace hiện tại, file mặc định là:

```text
data/tuvi-hoang-pham-huy-2026.json
```

Chỉ dùng mặc định này khi nó vẫn tồn tại và không có JSON lá số khác gây mơ hồ.

## 3. Kiểm tra dữ liệu bắt buộc

Trước khi luận giải, Codex phải kiểm tra:

1. JSON hợp lệ.
2. Thông tin ngày, giờ, múi giờ và giới tính.
3. Có đủ 12 cung thật.
4. Bỏ qua phần tử kỹ thuật có `cungSo: 0`.
5. Xác định đúng Cung Mệnh và vị trí an Thân.
6. Đủ 14 chính tinh hoặc ghi rõ chính tinh nào thiếu.
7. Xác định toàn bộ phụ tinh và sát tinh tại cung mục tiêu.
8. Xác định trạng thái Miếu–Vượng–Đắc–Hãm đúng theo trường `saoDacTinh`.
9. Xác định bốn Hóa theo đúng vị trí có trong file.
10. Xác định vòng Tràng Sinh.
11. Xác định Tuần và Triệt.
12. Kiểm tra quan hệ ngũ hành giữa bản mệnh, cục, hành cung và hành sao khi dữ liệu có cung cấp.

Không coi `has_luangiai: false` là thiếu dữ liệu lá số. Trường này chỉ có nghĩa API không cung cấp bài luận giải viết sẵn.

Nếu schema có trường mâu thuẫn, phải công khai mâu thuẫn và loại trường đó khỏi bằng chứng quyết định. Ví dụ, file hiện tại có hai bộ Mệnh Chủ/Thân Chủ khác nhau nên không được tự chọn một bộ.

Nếu JSON chỉ ghi vị trí của Hóa mà không ghi chính tinh phát hóa, chỉ được luận Hóa theo cung. Không tự gán sao phát hóa từ kiến thức bên ngoài.

Không dùng riêng trường `saoTot` để kết luận tốt hoặc xấu.

## 4. Xác định tam phương tứ chính

Tam phương tứ chính của cung mục tiêu gồm:

1. Bản cung.
2. Hai cung cùng nhóm tam hợp địa chi.
3. Cung xung chiếu.

### 4.1. Các nhóm tam hợp địa chi

| Nhóm | Địa chi |
|---|---|
| Hợi–Mão–Mùi | Hợi, Mão, Mùi |
| Dần–Ngọ–Tuất | Dần, Ngọ, Tuất |
| Tỵ–Dậu–Sửu | Tỵ, Dậu, Sửu |
| Thân–Tý–Thìn | Thân, Tý, Thìn |

### 4.2. Các cặp xung chiếu

| Cung | Đối cung |
|---|---|
| Tý | Ngọ |
| Sửu | Mùi |
| Dần | Thân |
| Mão | Dậu |
| Thìn | Tuất |
| Tỵ | Hợi |

Phải xác định quan hệ từ `cungTen` trong JSON. Không suy đoán tam phương tứ chính chỉ từ tên chức năng như Mệnh, Quan Lộc hoặc Thiên Di.

### 4.3. Giới hạn phạm vi

Phân bổ nội dung:

- 60–70% dành cho bản cung mục tiêu.
- 20–30% dành cho hai cung tam hợp và cung xung chiếu, nhưng chỉ xét cách chúng tác động tới cung mục tiêu.
- 10–15% dành cho tổng hợp, lời khuyên và hộp bằng chứng.

Ví dụ, report Thiên Di không được biến thành report đầy đủ về Mệnh, Phúc Đức hay Phu Thê. Các cung liên hệ chỉ trả lời:

> Chúng hỗ trợ, làm yếu, kích hoạt hoặc điều chỉnh cách Thiên Di biểu hiện như thế nào?

## 5. Phạm vi luận theo từng cung

Mỗi report chỉ luận hành vi thuộc phạm vi cung mục tiêu:

| Cung | Phạm vi hành vi được phép luận |
|---|---|
| Mệnh | Bản sắc, phản xạ căn bản, cách tự tổ chức và biểu hiện bản thân |
| Thân | Vùng đời sống cá nhân đầu tư nhiều sự tham gia thực tế; phải xét cung nơi an Thân |
| Thiên Di | Cách tương tác với môi trường bên ngoài, phản hồi xã hội, thích nghi và biểu hiện khi ra khỏi vùng quen thuộc |
| Quan Lộc | Cách đảm nhiệm vai trò, làm việc, xử lý trách nhiệm và tiêu chuẩn nghề nghiệp; không dự đoán chức vụ |
| Tài Bạch | Cách định giá, sử dụng nguồn lực và biến năng lực thành giá trị; không dự đoán giàu nghèo |
| Phúc Đức | Nền tinh thần, niềm tin, cách tạo cảm giác an tâm và phục hồi nội tâm |
| Tật Ách | Cách phản ứng khi căng thẳng hoặc mất cân bằng; không chẩn đoán bệnh |
| Nô Bộc | Hành vi với bạn bè, đồng nghiệp, nhóm và cộng đồng |
| Phu Thê | Hành vi trong quan hệ một-một và cách điều tiết gần–xa; không dự đoán kết quả hôn nhân |
| Phụ Mẫu | Cách tiếp nhận thẩm quyền, khuôn mẫu hướng dẫn và phản ứng với người định hướng; không quy kết sự kiện gia đình |
| Huynh Đệ | Cách chia sẻ vị trí, cạnh tranh hoặc hợp tác với người ngang hàng; không dự đoán số lượng anh chị em |
| Điền Trạch | Quan hệ tâm lý với không gian riêng, sự ổn định và ranh giới sở hữu; không dự đoán bất động sản |
| Tử Tức | Cách phản ứng với sản phẩm do mình tạo ra, trách nhiệm nuôi dưỡng hoặc người cần được hướng dẫn; không dự đoán con cái |

Nếu một cách đọc là quy tắc mở rộng hoặc khác nhau giữa các trường phái, phải nói rõ.

## 6. Quy tắc diễn giải sao

### 6.1. Không dùng từ khóa đơn lẻ

Không viết:

> Có Đà La nên người này trì hoãn.

Phải viết theo dạng có điều kiện:

> Trong quy tắc đang sử dụng, Đà La biểu thị lực cản, độ bám và điểm vướng khó giải quyết nhanh. Khi nằm trực tiếp tại Mệnh, chức năng này có thể đi vào cách cá nhân xử lý bản thân: tiếp tục kiểm tra hoặc chưa hành động khi còn điều chưa thông. Trong đời sống, nó có thể biểu hiện thành trì hoãn; mặt trưởng thành của cùng cơ chế là sức bền với vấn đề khó.

### 6.2. Luôn đi theo thứ tự

Với mỗi sao hoặc bộ sao quan trọng, phân tích theo thứ tự:

1. Sao có chức năng biểu tượng gì theo quy tắc đang dùng?
2. Sao nằm tại cung nào và vì sao vị trí đó quan trọng?
3. Trạng thái Miếu–Vượng–Đắc–Hãm làm chức năng dễ hay khó điều tiết thế nào?
4. Sao đồng cung với những sao nào?
5. Tam hợp và đối cung bổ sung hay phản biện điều gì?
6. Tuần/Triệt và vòng Tràng Sinh điều chỉnh nhịp biểu hiện ra sao?
7. Cơ chế tổng hợp tạo chuỗi hành vi nào?
8. Khi trưởng thành, cơ chế đó biểu hiện thế nào?
9. Khi mất cân bằng, nó biểu hiện thế nào?
10. Lời khuyên nào tác động trực tiếp vào cơ chế đó?

### 6.3. Miếu–Vượng–Đắc–Hãm

- Miếu, Vượng và Đắc không tự động có nghĩa là tốt về đạo đức.
- Chúng thường chỉ chức năng biểu hiện rõ hoặc dễ sử dụng hơn.
- Hãm không có nghĩa chắc chắn xấu.
- Hãm thường chỉ chức năng khó điều tiết, dễ quá mức, thiếu ổn định hoặc phụ thuộc hoàn cảnh hơn.

### 6.4. Cát tinh và sát tinh

- Không tâng bốc cát tinh.
- Không bi kịch hóa sát tinh.
- Mỗi sao phải có khả năng biểu hiện trưởng thành và mất cân bằng nếu tổ hợp cho phép.
- Sát tinh có thể trở thành sức bền, khả năng hành động, đặt giới hạn hoặc chịu áp lực khi được điều tiết.
- Cát tinh có thể trở thành tự mãn, né tránh hoặc lệ thuộc vào thuận lợi khi mất cân bằng.

### 6.5. Tuần, Triệt và vòng Tràng Sinh

- Không nói Tuần/Triệt xóa hoàn toàn sao.
- Chỉ dùng như lực ngắt, chặn, trì hoãn, làm lệch hoặc buộc điều chỉnh.
- Công khai rằng ý nghĩa cụ thể khác nhau giữa các trường phái.
- Các tên Bệnh, Tử, Mộ, Tuyệt không được dùng để suy ra bệnh tật, tuổi thọ hoặc sự kiện.

### 6.6. Ngũ hành

- Chỉ sử dụng dữ liệu hành có trong file.
- Không tự thêm hành sao nếu file không có.
- Ngũ hành là lớp điều chỉnh, không được lấn át chính tinh, vị trí cung và quan hệ tam phương tứ chính.
- Nếu kết luận phụ thuộc ngũ hành, độ tin cậy tối đa nên là thấp hoặc trung bình, trừ khi có chỉ dấu khác hỗ trợ mạnh.

## 7. Phân biệt bốn tầng nội dung

Trong quá trình suy luận, luôn phân biệt:

### 7.1. Dữ liệu trực tiếp

Ví dụ:

> Thiên Di tại Sửu có Thiên Đồng hãm, Cự Môn hãm và Hóa Kỵ đắc.

### 7.2. Quy tắc đang sử dụng

Ví dụ:

> Thiên Đồng được dùng cho nhu cầu thích nghi và tìm điểm chung; Cự Môn được dùng cho việc phân biệt bằng ngôn ngữ và chất vấn.

### 7.3. Suy luận hành vi

Ví dụ:

> Khi gặp môi trường mập mờ, cá nhân có thể bắt đầu bằng thích nghi rồi chuyển sang chất vấn khi cảm thấy thông tin không nhất quán.

### 7.4. Phản biện hoặc dữ liệu chưa đủ

Ví dụ:

> Tấu Thư và Đường Phù hỗ trợ trình bày có trình tự, nên không thể kết luận người này thiếu năng lực giao tiếp. Không có dữ liệu hành vi thực tế để xác định tần suất tranh luận.

Trong phần văn xuôi có thể không cần gắn nhãn bốn tầng ở mọi đoạn, nhưng hộp bằng chứng cuối report phải thể hiện rõ chúng.

## 8. Phong cách văn xuôi bắt buộc

### 8.1. Viết theo cơ chế, không viết như từ điển sao

Ưu tiên dạng:

> Sao A tạo lực giữ. Sao B tạo tốc độ kích hoạt. Sao C đưa phản ứng thành phân định. Khi ba sao đồng cung tại cung mục tiêu, chuỗi hành vi dễ hình thành là giữ điểm vướng → tích áp → phản ứng dứt.

Không viết một danh sách rời:

> Sao A: trì hoãn. Sao B: nóng. Sao C: hình phạt.

### 8.2. Chỉ giải thích đầy đủ một sao ở lần xuất hiện quan trọng đầu tiên

Những lần sau dùng cách gọi ngắn:

> “Cơ chế giữ và trì kéo của Đà La…”

Không chép lại toàn bộ định nghĩa của sao ở nhiều mục.

### 8.3. Luôn viết có điều kiện

Ưu tiên:

- Có xu hướng…
- Dễ biểu hiện khi…
- Nếu mất cân bằng có thể…
- Khi được điều tiết, cùng cơ chế có thể trở thành…
- Dữ liệu làm tăng khả năng…

Không dùng:

- Chắc chắn.
- Luôn luôn.
- Không thể thay đổi.
- Số phận buộc phải.

### 8.4. Dùng ví dụ hành vi

Ví dụ phải cụ thể và có hai phía:

> Khi tiêu chí dự án bị đổi mà không báo, biểu hiện trưởng thành là yêu cầu ghi lại quyết định, ảnh hưởng và người chịu trách nhiệm. Biểu hiện mất cân bằng là giữ khó chịu, quy người kia thiếu trách nhiệm, rồi phản ứng gay gắt khi một lỗi nhỏ khác xuất hiện.

Không biến ví dụ thành khẳng định rằng sự việc đã xảy ra.

## 9. Quy tắc viết lời khuyên

Mỗi lời khuyên phải chỉ rõ nó xử lý cơ chế nào.

### 9.1. Mẫu đúng

> Vì Đà La làm điểm vướng được giữ lâu, hãy đặt hạn chót cho quá trình thu thập thông tin và một tiêu chí “đủ để quyết định”.

> Vì Hỏa Tinh–Thiên Hình có thể làm phản ứng chuyển nhanh sang cắt bỏ, không đưa ra quyết định loại bỏ ở đỉnh kích hoạt; trước hết ghi rõ ranh giới nào đã bị vượt.

> Vì Cự Môn–Hóa Kỵ nhạy với cách hiểu, hãy tách dữ kiện quan sát được, cách diễn giải và phần chưa biết về động cơ.

### 9.2. Mẫu không đạt

- Hãy sống tích cực.
- Hãy cố gắng hơn.
- Hãy bình tĩnh.
- Nên ngủ đủ.
- Hãy tin vào bản thân.

Các lời khuyên trên quá chung và không được phép dùng nếu không có liên hệ trực tiếp với cơ chế vừa phân tích.

### 9.3. Yêu cầu đối với lời khuyên

- Cụ thể.
- Có thể quan sát hoặc thực hiện.
- Gắn với hoàn cảnh kích hoạt.
- Không chẩn đoán tâm lý.
- Không yêu cầu người đọc thay đổi toàn bộ tính cách.
- Tận dụng mặt trưởng thành của chính tổ hợp, không chỉ cố “loại bỏ điểm xấu”.

## 10. Độ tin cậy

Sử dụng rubric:

- **Cao:** Có bằng chứng trực tiếp tại cung mục tiêu và ít nhất hai chỉ dấu độc lập hỗ trợ; ít phụ thuộc khác biệt trường phái.
- **Trung bình:** Có bằng chứng trực tiếp nhưng cần phụ tinh, tam hợp hoặc một quy tắc mở rộng.
- **Thấp:** Chủ yếu dựa vào phụ tinh, ngũ hành, Tuần/Triệt hoặc quy tắc khác nhau đáng kể giữa các trường phái.

Có thể viết mức ghép như `Trung bình–cao` nếu giải thích rõ phần nào cao và phần nào trung bình.

Không chấm hầu hết mọi nhận định là cao.

Phân biệt:

- Độ chắc của vị trí sao trong JSON.
- Độ chắc của quy tắc diễn giải.
- Độ chắc của suy luận hành vi.

## 11. Cấu trúc file report bắt buộc

Report nên có cấu trúc sau, điều chỉnh tên mục theo cung mục tiêu:

```markdown
# Luận Cung <TÊN CUNG> và tam phương tứ chính

## Phạm vi

## 1. Kết luận nhanh về Cung <TÊN CUNG>

## 2. Dữ liệu trực tiếp
### 2.1. Bản cung
### 2.2. Tam phương tứ chính
### 2.3. Ngũ hành liên quan

## 3. Chính tinh hoặc cấu trúc chính của bản cung

## 4. Các phụ tinh/sát tinh quan trọng tại bản cung

## 5. Các bộ sao đồng cung và cơ chế phối hợp

## 6. Tuần, Triệt và vòng Tràng Sinh

## 7. Cung xung chiếu tác động trở lại bản cung

## 8. Tam hợp thứ nhất tác động trở lại bản cung

## 9. Tam hợp thứ hai tác động trở lại bản cung

## 10. Ghép tam phương tứ chính thành cấu trúc tổng thể

## 11. Các khuynh hướng hành vi quan trọng

## 12. Lời khuyên xuất phát trực tiếp từ cấu trúc cung

## 13. Những điều cần kiểm chứng bằng thực tế

## 14. Hộp bằng chứng kỹ thuật

## 15. Kết luận cuối cùng
```

Nếu bản cung vô chính diệu, mục 3 phải giải thích vô chính diệu và nguyên tắc mượn lực từ đối cung/tam hợp.

Nếu cung mục tiêu cũng là nơi an Thân, phải có một mục riêng giải thích vai trò của Thân nhưng không mở rộng sang các cung không liên quan.

## 12. Yêu cầu cho mỗi khuynh hướng quan trọng

Mỗi khuynh hướng quan trọng phải có:

- Mã nhận định ổn định, ví dụ `THIENDI-01` hoặc `QUANLOC-02`.
- Nhận định.
- Bằng chứng chính tại bản cung.
- Bằng chứng hỗ trợ từ tam phương hoặc đối cung.
- Cơ chế hình thành.
- Hoàn cảnh kích hoạt.
- Biểu hiện trưởng thành.
- Biểu hiện mất cân bằng.
- Yếu tố phản biện.
- Độ tin cậy.

Không cần lặp lại toàn bộ phần giải nghĩa sao trong mỗi mã nhận định; có thể dẫn về mục đã giải thích cơ chế.

## 13. Chuỗi hành vi

Với các tổ hợp quan trọng, viết ít nhất một chuỗi hành vi có thể quan sát:

```text
Tín hiệu kích hoạt
        ↓
Phản ứng nhận thức
        ↓
Điểm vướng hoặc nhu cầu
        ↓
Hành động biểu hiện
        ↓
Hậu quả gần về tương tác
```

Chuỗi này là giả thuyết để kiểm chứng, không phải sự kiện chắc chắn.

## 14. Câu hỏi kiểm chứng

Cuối report phải có 8–12 câu hỏi tự quan sát.

Câu hỏi phải:

- Yêu cầu ví dụ gần đây.
- Hỏi tần suất hoặc hoàn cảnh.
- Yêu cầu ít nhất một phản ví dụ.
- Phân biệt dữ kiện và cách diễn giải.
- Có thể hỏi thêm quan sát của người làm việc cùng hoặc người gần gũi.

Không chỉ hỏi theo kiểu dẫn dắt “Bạn có thường… không?”.

Ví dụ tốt:

> Trong ba lần gần nhất gặp người nói không rõ ý, bạn đã hỏi để xác minh, tự suy đoán hay tránh tương tác? Có trường hợp nào bạn chấp nhận “chưa biết” mà không tiếp tục phân tích không?

## 15. Hộp bằng chứng kỹ thuật

Cuối report phải có hộp ngắn theo mẫu:

> **Bản cung:** Vị trí, hành cung, chính tinh, phụ tinh/sát tinh trọng yếu, trạng thái.  
> **Tam hợp thứ nhất:** Cung, chính tinh và sao hỗ trợ liên quan.  
> **Tam hợp thứ hai:** Cung, chính tinh và sao hỗ trợ liên quan.  
> **Đối cung:** Cung, chính tinh và sao liên quan.  
> **Bộ sao trọng yếu:** Chỉ nêu đúng quan hệ đồng cung/tam hợp/xung chiếu.  
> **Tuần/Triệt và Tràng Sinh:** Vị trí và cách điều tiết đang dùng.  
> **Cơ chế tổng hợp:** Một câu.  
> **Yếu tố hỗ trợ:** Một dòng.  
> **Yếu tố làm khó:** Một dòng.  
> **Độ tin cậy chung:** Phân biệt cấu trúc và hành vi thực tế.

## 16. Quy tắc đặt tên và lưu file

Tạo report trong thư mục `rp/`.

Tên file mặc định:

```text
rp/cung-<ten-cung-khong-dau>-va-tam-phuong-tu-chinh.md
```

Ví dụ:

```text
rp/cung-thien-di-va-tam-phuong-tu-chinh.md
rp/cung-tat-ach-va-tam-phuong-tu-chinh.md
rp/cung-phuc-duc-va-tam-phuong-tu-chinh.md
```

Nếu đã tồn tại file cùng tên:

1. Đọc file hiện có.
2. Chỉ ghi đè khi người dùng yêu cầu sửa hoặc làm lại.
3. Nếu yêu cầu chỉ nói “viết report” và file đã tồn tại, tạo tên có hậu tố `-v2` hoặc hỏi người dùng tùy mức độ khác biệt.

Không tự động sửa report tổng hợp.

Không tự động gộp nhiều report.

Không tự động commit hoặc push Git nếu người dùng chưa yêu cầu trong lượt hiện tại hoặc chưa thiết lập rõ workflow tự động cho repository.

## 17. Những điều tuyệt đối không làm

- Không tự bổ sung sao không có trong JSON.
- Không khẳng định một cách cục vì các sao chỉ cùng xuất hiện đâu đó trong lá số.
- Không nhầm đồng cung, tam hợp, xung chiếu hoặc giáp cung.
- Không dự đoán sự kiện, vận hạn, tương lai, tuổi thọ, bệnh tật hoặc kết quả chắc chắn.
- Không dùng tên vòng Tràng Sinh theo nghĩa đen về sinh tử.
- Không chẩn đoán bệnh tâm lý hoặc gán nhãn nhân cách lâm sàng.
- Không dùng riêng `saoTot` để đánh giá.
- Không bỏ qua chỉ dấu phản biện.
- Không biến phụ tinh nhỏ thành kết luận cốt lõi nếu thiếu hỗ trợ.
- Không đưa lời khuyên chung chung không liên quan tới cơ chế vừa phân tích.
- Không dùng ngôn ngữ tâng bốc, hù dọa hoặc định mệnh.

## 18. Quy trình làm việc cho Codex

Khi nhận lệnh luận một cung, thực hiện theo thứ tự:

1. Xác định cung mục tiêu.
2. Xác định file JSON.
3. Đọc toàn bộ JSON.
4. Kiểm tra dữ liệu bắt buộc.
5. Lọc cung mục tiêu và toàn bộ sao tại đó.
6. Xác định hai cung tam hợp và cung xung chiếu bằng địa chi.
7. Lập bảng dữ liệu trực tiếp trước khi viết suy luận.
8. Xác định 3–6 bộ sao hoặc cơ chế quan trọng nhất.
9. Tìm chỉ dấu hỗ trợ và phản biện.
10. Viết văn xuôi sâu cho bản cung.
11. Luận các cung liên hệ chỉ trong phạm vi tác động trở lại bản cung.
12. Ghép thành 4–7 khuynh hướng hành vi có mã.
13. Viết lời khuyên gắn trực tiếp với từng cơ chế.
14. Viết câu hỏi kiểm chứng và phản chứng.
15. Tạo hộp bằng chứng kỹ thuật.
16. Kiểm tra lại mọi tên sao, vị trí, trạng thái và quan hệ cung với JSON.
17. Kiểm tra Markdown.
18. Lưu file trong `rp/`.
19. Báo cho người dùng đường dẫn, phạm vi, số từ và các giới hạn quan trọng.

## 19. Tiêu chuẩn chất lượng trước khi hoàn tất

Codex chỉ được coi report hoàn tất khi trả lời “có” cho các câu hỏi sau:

- Đã đọc toàn bộ JSON chưa?
- Đã bỏ `cungSo: 0` chưa?
- Đã xác định đúng bản cung, hai tam hợp và đối cung chưa?
- Đã liệt kê đủ sao tại bản cung chưa?
- Đã giữ đúng trạng thái Miếu–Vượng–Đắc–Hãm chưa?
- Đã phân biệt đồng cung, tam hợp và xung chiếu chưa?
- Đã xét Tuần, Triệt và vòng Tràng Sinh chưa?
- Đã giải thích vì sao tổ hợp dẫn tới hành vi chưa?
- Đã có mặt trưởng thành và mất cân bằng chưa?
- Đã có chỉ dấu phản biện chưa?
- Lời khuyên có gắn với cơ chế cụ thể không?
- Có câu hỏi tìm phản ví dụ không?
- Có kết luận nào vượt quá dữ liệu không?
- Có câu nào mang tính dự đoán hoặc định mệnh không?
- File nguồn có được giữ nguyên không?

## 20. Mẫu lệnh sử dụng

### Cách ngắn

```text
Hãy luận giải cung Thiên Di theo hướng dẫn trong:
data/HUONG-DAN-VIET-REPORT-TUNG-CUNG.md
```

### Chỉ rõ file dữ liệu

```text
Hãy dùng data/tuvi-hoang-pham-huy-2026.json và luận giải cung Thiên Di theo hướng dẫn trong data/HUONG-DAN-VIET-REPORT-TUNG-CUNG.md. Tạo report trong rp/.
```

### Yêu cầu sửa report đã có

```text
Hãy đọc lại dữ liệu và cập nhật report cung Thiên Di theo hướng dẫn trong data/HUONG-DAN-VIET-REPORT-TUNG-CUNG.md. Giữ các phần đúng, sửa các suy luận chưa đủ bằng chứng và ghi đè file report hiện tại.
```

## 21. Mẫu phản hồi cuối của Codex

Sau khi tạo report, phản hồi ngắn gọn:

```text
Đã tạo report chuyên sâu cho Cung <TÊN CUNG>:

[tên-file.md](/đường/dẫn/tuyệt/đối/tới/file.md)

- Dữ liệu nguồn: ...
- Bản cung: ...
- Tam phương: ... và ...
- Đối cung: ...
- Số từ: ...
- Giới hạn quan trọng: ...

File JSON nguồn không bị sửa đổi.
```
