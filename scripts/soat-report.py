#!/usr/bin/env python3
"""Soát câu chữ của report luận giải theo Q§4–Q§5 (QUY-TAC-LUAN-GIAI-TU-VI.md).

  python3 scripts/soat-report.py rp/<report>.md [rp/<report2>.md ...]

LỖI: phải sửa trước khi giao. CẢNH BÁO: phải đọc lại từng chỗ; được giữ nếu có lý do.
Exit code 1 khi còn LỖI.
"""
import re
import sys

PHU_DINH = re.compile(r'\b(không|chưa|chẳng)\b')
# Từ đứng trong câu đã có phủ định phía trước ("không phải… chắc chắn") là câu rào, không tính.
BO_QUA_KHI_PHU_DINH = {'chắc chắn', 'định mệnh'}
TU_CAM = [
    (r'chắc chắn', 'từ tuyệt đối "chắc chắn" (Q§4.4)'),
    (r'định mệnh', 'từ "định mệnh" (Q§4.4)'),
    (r'không thể tránh', 'từ "không thể tránh" (Q§4.4)'),
    (r'số phải', 'từ "số phải" (Q§4.4)'),
    (r'luôn luôn', 'từ tuyệt đối "luôn luôn" (Q§5.4)'),
    (r'không bao giờ', 'từ tuyệt đối "không bao giờ" (Q§5.4)'),
    (r'cực kỳ', 'từ tuyệt đối "cực kỳ" (Q§5.4)'),
    (r'đại hung|hạn rất nặng', 'nhãn dọa (Q§5.4)'),
    (r'(Thấp|Trung bình|Cao)\s*[–-]\s*(Trung bình|Cao)', 'mức tin cậy ghép; chỉ dùng ba mức (Q§4.1)'),
]
CANH_BAO = [
    (r'không (có|đủ) căn cứ', 'kiểm lại: có chỉ báo H1–H3 thì phải viết "hệ thống nghiêng về…" (Q§4.4)'),
    (r'bề ngoài .{0,40}bên trong|lúc hướng ngoại|lúc hướng nội', 'mẫu Barnum hai cực (Q§5.3)'),
    (r'tiềm năng chưa|coi trọng gia đình|muốn được công nhận|đôi khi lo lắng|trái tim ấm áp',
     'tính từ ai cũng nhận (Q§5.3)'),
    (r'có thời điểm trong đời|về sau sẽ khá|mọi khó khăn rồi', 'thời gian mơ hồ hoặc an ủi (Q§5.3)'),
    (r'hãy sống tích cực|hãy cố gắng|hãy bình tĩnh|hãy tin vào bản thân', 'lời khuyên chung chung (Q§5.3)'),
    (r'\bluôn\b', 'từ "luôn": kiểm có phải tuyệt đối hóa không (Q§5.4)'),
    (r'\bsẽ\b', 'từ "sẽ": kiểm có biến xu hướng thành sự kiện không (Q§5.4)'),
]
MA_KET_LUAN = re.compile(r'^#{2,4}\s+([A-ZĐ]{2,}-\d{2,})\b')
MUC_CAO = re.compile(r'(Độ tin cậy|Mức)\s*[:：]?\s*\**\s*Cao\b')


def soat(path):
    loi, canh_bao = [], []
    dong = open(path, encoding='utf-8').read().splitlines()
    trong_code = False
    for i, d in enumerate(dong, 1):
        if d.strip().startswith('```'):
            trong_code = not trong_code
        if trong_code or d.lstrip().startswith('>'):
            continue
        thap = d.lower()
        for mau, ly_do in TU_CAM:
            for cau in re.split(r'[.;!?]', thap if mau.islower() else d):
                m = re.search(mau, cau)
                if not m:
                    continue
                if mau in BO_QUA_KHI_PHU_DINH and PHU_DINH.search(cau[:m.start()].lower()):
                    continue
                loi.append((i, ly_do, d.strip()))
                break
        for mau, ly_do in CANH_BAO:
            if re.search(mau, thap):
                canh_bao.append((i, ly_do, d.strip()))

    # Từng kết luận có mã: phải có "Sai nếu" và mức tin cậy; mức Cao không dùng "có thể".
    muc = []
    for i, d in enumerate(dong):
        m = MA_KET_LUAN.match(d)
        if m:
            muc.append((i, m.group(1)))
    for j, (i, ma) in enumerate(muc):
        het = muc[j + 1][0] if j + 1 < len(muc) else len(dong)
        for k in range(i + 1, het):
            if re.match(r'^#{1,3}\s', dong[k]) and not MA_KET_LUAN.match(dong[k]):
                het = k
                break
        khoi = '\n'.join(dong[i:het])
        if 'sai nếu' not in khoi.lower():
            loi.append((i + 1, f'{ma} thiếu "Sai nếu…" (Q§5.2)', dong[i].strip()))
        if not re.search(r'Độ tin cậy|Mức\s*[:：]', khoi):
            loi.append((i + 1, f'{ma} thiếu mức tin cậy (Q§4)', dong[i].strip()))
        if MUC_CAO.search(khoi) and re.search(r'\bcó thể\b', khoi.lower()):
            canh_bao.append((i + 1, f'{ma} mức Cao nhưng dùng "có thể" (Q§5.5)', dong[i].strip()))
    if not muc:
        canh_bao.append((1, 'không thấy kết luận có mã (### XXX-01); không kiểm được Q§5.2', ''))

    gioi_han = [i + 1 for i, d in enumerate(dong) if re.match(r'^#{2,4}\s+.*[Gg]iới hạn', d)]
    if len(gioi_han) > 1:
        loi.append((gioi_han[1], f'có {len(gioi_han)} mục "Giới hạn"; chỉ viết một lần (L§9.3)', ''))
    return loi, canh_bao


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    con_loi = False
    for path in sys.argv[1:]:
        loi, canh_bao = soat(path)
        print(f'# {path}: {len(loi)} LỖI, {len(canh_bao)} CẢNH BÁO')
        for muc, ds in (('LỖI', loi), ('CẢNH BÁO', canh_bao)):
            for i, ly_do, trich in sorted(ds):
                print(f'{path}:{i}: [{muc}] {ly_do}' + (f' | {trich[:110]}' if trich else ''))
        con_loi = con_loi or bool(loi)
    sys.exit(1 if con_loi else 0)


if __name__ == '__main__':
    main()
