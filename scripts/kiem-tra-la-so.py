#!/usr/bin/env python3
"""Tính lại lá số tử vi, đối chiếu file dữ liệu, xuất cấu trúc cung, bảng hạn và tần suất nền.

Công thức: docs/cong-thuc-an-sao.md. Cách dùng output: QUY-TAC-LUAN-GIAI-TU-VI.md (Q§2).

  python3 scripts/kiem-tra-la-so.py data/hoang/tuvi-hoang-pham-huy-2026.data.json
  python3 scripts/kiem-tra-la-so.py data/hoang/tuvi-hoang-pham-huy-2026.data.json --nam-xem 2027 --cung "Phu Thê"
  python3 scripts/kiem-tra-la-so.py --duong-lich 2000-11-27 --gio 17:00 --gioi nu --ten Hường
  python3 scripts/kiem-tra-la-so.py --am-lich 2000-11-02 --gio 17:00 --gioi nu
  python3 scripts/kiem-tra-la-so.py --doi-chung 5 --seed 1
"""
import argparse
import json
import math
import random
import sys
import unicodedata
from datetime import datetime
from zoneinfo import ZoneInfo

CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
CUNG = ['Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 'Quan Lộc', 'Nô Bộc',
        'Thiên Di', 'Tật Ách', 'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ']
NAP_AM = ['Hải Trung Kim', 'Lư Trung Hỏa', 'Đại Lâm Mộc', 'Lộ Bàng Thổ', 'Kiếm Phong Kim',
          'Sơn Đầu Hỏa', 'Giản Hạ Thủy', 'Thành Đầu Thổ', 'Bạch Lạp Kim', 'Dương Liễu Mộc',
          'Tuyền Trung Thủy', 'Ốc Thượng Thổ', 'Tích Lịch Hỏa', 'Tùng Bách Mộc', 'Trường Lưu Thủy',
          'Sa Trung Kim', 'Sơn Hạ Hỏa', 'Bình Địa Mộc', 'Bích Thượng Thổ', 'Kim Bạch Kim',
          'Phú Đăng Hỏa', 'Thiên Hà Thủy', 'Đại Trạch Thổ', 'Thoa Xuyến Kim', 'Tang Đố Mộc',
          'Đại Khê Thủy', 'Sa Trung Thổ', 'Thiên Thượng Hỏa', 'Thạch Lựu Mộc', 'Đại Hải Thủy']
SO_CUC = {'Thủy': 2, 'Mộc': 3, 'Kim': 4, 'Thổ': 5, 'Hỏa': 6}
TEN_CUC = {2: 'Thủy nhị cục', 3: 'Mộc tam cục', 4: 'Kim tứ cục', 5: 'Thổ ngũ cục', 6: 'Hỏa lục cục'}

CHINH_TINH = ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh', 'Thiên Phủ',
              'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 'Thất Sát', 'Phá Quân']
LUC_SAT = ['Kình Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh', 'Địa Không', 'Địa Kiếp']
LUC_CAT = ['Tả Phù', 'Hữu Bật', 'Văn Xương', 'Văn Khúc', 'Thiên Khôi', 'Thiên Việt']
HOA = ['Hóa Lộc', 'Hóa Quyền', 'Hóa Khoa', 'Hóa Kỵ']
TU_HOA = {
    0: ['Liêm Trinh', 'Phá Quân', 'Vũ Khúc', 'Thái Dương'],
    1: ['Thiên Cơ', 'Thiên Lương', 'Tử Vi', 'Thái Âm'],
    2: ['Thiên Đồng', 'Thiên Cơ', 'Văn Xương', 'Liêm Trinh'],
    3: ['Thái Âm', 'Thiên Đồng', 'Thiên Cơ', 'Cự Môn'],
    4: ['Tham Lang', 'Thái Âm', 'Hữu Bật', 'Thiên Cơ'],
    5: ['Vũ Khúc', 'Tham Lang', 'Thiên Lương', 'Văn Khúc'],
    6: ['Thái Dương', 'Vũ Khúc', 'Thái Âm', 'Thiên Đồng'],
    7: ['Cự Môn', 'Thái Dương', 'Văn Khúc', 'Văn Xương'],
    8: ['Thiên Lương', 'Tử Vi', 'Tả Phù', 'Vũ Khúc'],
    9: ['Phá Quân', 'Cự Môn', 'Thái Âm', 'Tham Lang'],
}
LOC_TON = {0: 2, 1: 3, 2: 5, 3: 6, 4: 5, 5: 6, 6: 8, 7: 9, 8: 11, 9: 0}
KHOI_VIET = {0: (1, 7), 4: (1, 7), 1: (0, 8), 5: (0, 8), 2: (11, 9), 3: (11, 9),
             8: (3, 5), 9: (3, 5), 7: (6, 2), 6: (6, 2)}
TRIET = {0: (8, 9), 5: (8, 9), 1: (6, 7), 6: (6, 7), 2: (4, 5), 7: (4, 5),
         3: (2, 3), 8: (2, 3), 4: (0, 1), 9: (0, 1)}
TRANG_SINH_KHOI = {2: 8, 5: 8, 3: 11, 4: 5, 6: 2}
VONG_TRANG_SINH = ['Tràng Sinh', 'Mộc Dục', 'Quan Đới', 'Lâm Quan', 'Đế Vượng', 'Suy',
                   'Bệnh', 'Tử', 'Mộ', 'Tuyệt', 'Thai', 'Dưỡng']
VONG_THAI_TUE = ['Thái Tuế', 'Thiếu Dương', 'Tang Môn', 'Thiếu Âm', 'Quan Phù', 'Tử Phù',
                 'Tuế Phá', 'Long Đức', 'Bạch Hổ', 'Phúc Đức', 'Điếu Khách', 'Trực Phù']
VONG_BAC_SI = ['Bác Sĩ', 'Lực Sĩ', 'Thanh Long', 'Tiểu Hao', 'Tướng Quân', 'Tấu Thư',
               'Phi Liêm', 'Hỷ Thần', 'Bệnh Phù', 'Đại Hao', 'Phục Binh', 'Quan Phủ']
MENH_CHU = {0: 'Tham Lang', 1: 'Cự Môn', 11: 'Cự Môn', 2: 'Lộc Tồn', 10: 'Lộc Tồn', 3: 'Văn Khúc',
            9: 'Văn Khúc', 4: 'Liêm Trinh', 8: 'Liêm Trinh', 5: 'Vũ Khúc', 7: 'Vũ Khúc', 6: 'Phá Quân'}
THAN_CHU = {0: 'Hỏa Tinh', 6: 'Hỏa Tinh', 1: 'Thiên Tướng', 7: 'Thiên Tướng', 2: 'Thiên Lương',
            8: 'Thiên Lương', 3: 'Thiên Đồng', 9: 'Thiên Đồng', 4: 'Văn Xương', 10: 'Văn Xương',
            5: 'Thiên Cơ', 11: 'Thiên Cơ'}
# Nhóm tam hợp theo chi năm: 0 Thân Tý Thìn, 1 Tỵ Dậu Sửu, 2 Dần Ngọ Tuất, 3 Hợi Mão Mùi
NHOM = lambda z: z % 4
GIAP_CO_TEN = [('Không–Kiếp', 'Địa Không', 'Địa Kiếp'), ('Kình–Đà', 'Kình Dương', 'Đà La'),
               ('Hỏa–Linh', 'Hỏa Tinh', 'Linh Tinh'), ('Tả–Hữu', 'Tả Phù', 'Hữu Bật'),
               ('Xương–Khúc', 'Văn Xương', 'Văn Khúc'), ('Khôi–Việt', 'Thiên Khôi', 'Thiên Việt'),
               ('Nhật–Nguyệt', 'Thái Dương', 'Thái Âm')]
SAO_LOI = set(CHINH_TINH + LUC_SAT + LUC_CAT + HOA + ['Lộc Tồn'])


def md(x):
    return x % 12


def jiazi(c, z):
    return next(i for i in range(60) if i % 10 == c and i % 12 == z)


def canh_gio(hour):
    return ((hour + 1) // 2) % 12


# ---------------------------------------------------------------- Âm lịch (thuật toán Hồ Ngọc Đức)

def _jd(dd, mm, yy):
    a = (14 - mm) // 12
    y = yy + 4800 - a
    m = mm + 12 * a - 3
    jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    if jd < 2299161:
        jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
    return jd


def _new_moon(k):
    T = k / 1236.85
    T2, T3 = T * T, T * T * T
    dr = math.pi / 180
    jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
    jd1 += 0.00033 * math.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
    M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
    Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
    F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3
    C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) + 0.0021 * math.sin(2 * dr * M)
    C1 = C1 - 0.4068 * math.sin(Mpr * dr) + 0.0161 * math.sin(dr * 2 * Mpr)
    C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
    C1 = C1 + 0.0104 * math.sin(dr * 2 * F) - 0.0051 * math.sin(dr * (M + Mpr))
    C1 = C1 - 0.0074 * math.sin(dr * (M - Mpr)) + 0.0004 * math.sin(dr * (2 * F + M))
    C1 = C1 - 0.0004 * math.sin(dr * (2 * F - M)) - 0.0006 * math.sin(dr * (2 * F + Mpr))
    C1 = C1 + 0.0010 * math.sin(dr * (2 * F - Mpr)) + 0.0005 * math.sin(dr * (2 * Mpr + M))
    if T < -11:
        deltat = 0.001 + 0.000839 * T + 0.0002261 * T2 - 0.00000845 * T3 - 0.000000081 * T * T3
    else:
        deltat = -0.000278 + 0.000265 * T + 0.000262 * T2
    return jd1 + C1 - deltat


def _new_moon_day(k, tz):
    return math.floor(_new_moon(k) + 0.5 + tz / 24)


def _sun_longitude(day_number, tz):
    T = (day_number - 0.5 - tz / 24 - 2451545.0) / 36525
    T2 = T * T
    dr = math.pi / 180
    M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
    L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
    DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
    DL += (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) + 0.000290 * math.sin(dr * 3 * M)
    L = (L0 + DL) * dr
    L = L - math.pi * 2 * math.floor(L / (math.pi * 2))
    return math.floor(L / math.pi * 6)


def _lunar_month11(yy, tz):
    off = _jd(31, 12, yy) - 2415021
    k = math.floor(off / 29.530588853)
    nm = _new_moon_day(k, tz)
    if _sun_longitude(nm, tz) >= 9:
        nm = _new_moon_day(k - 1, tz)
    return nm


def _leap_month_offset(a11, tz):
    k = math.floor((a11 - 2415021.076998695) / 29.530588853 + 0.5)
    i = 1
    arc = _sun_longitude(_new_moon_day(k + i, tz), tz)
    while True:
        last = arc
        i += 1
        arc = _sun_longitude(_new_moon_day(k + i, tz), tz)
        if not (arc != last and i < 14):
            break
    return i - 1


def duong_sang_am(dd, mm, yy, tz=7):
    """Trả về (ngày, tháng, năm, nhuận) âm lịch."""
    day_number = _jd(dd, mm, yy)
    k = math.floor((day_number - 2415021.076998695) / 29.530588853)
    month_start = _new_moon_day(k + 1, tz)
    if month_start > day_number:
        month_start = _new_moon_day(k, tz)
    a11 = _lunar_month11(yy, tz)
    b11 = a11
    if a11 >= month_start:
        lunar_year = yy
        a11 = _lunar_month11(yy - 1, tz)
    else:
        lunar_year = yy + 1
        b11 = _lunar_month11(yy + 1, tz)
    lunar_day = day_number - month_start + 1
    diff = math.floor((month_start - a11) / 29)
    leap = False
    lunar_month = diff + 11
    if b11 - a11 > 365:
        leap_diff = _leap_month_offset(a11, tz)
        if diff >= leap_diff:
            lunar_month = diff + 10
            if diff == leap_diff:
                leap = True
    if lunar_month > 12:
        lunar_month -= 12
    if lunar_month >= 11 and diff < 4:
        lunar_year -= 1
    return lunar_day, lunar_month, lunar_year, leap


# ---------------------------------------------------------------- An sao

class LaSo:
    def __init__(self, nam_am, m, d, h, nam):
        self.nam_am, self.m, self.d, self.h, self.nam = nam_am, m, d, h, nam
        self.c = (nam_am + 6) % 10
        self.y = (nam_am + 8) % 12
        c, y = self.c, self.y
        self.thuan = (c % 2 == 0) == nam  # dương nam, âm nữ
        self.menh = md(m + 1 - h)
        self.than = md(m + 1 + h)
        can_dan = {0: 2, 5: 2, 1: 4, 6: 4, 2: 6, 7: 6, 3: 8, 8: 8, 4: 0, 9: 0}[c]
        self.can_cung = {z: (can_dan + md(z - 2)) % 10 for z in range(12)}
        self.chuc = {md(self.menh + k): CUNG[k] for k in range(12)}
        nap = NAP_AM[jiazi(self.can_cung[self.menh], self.menh) // 2]
        self.cuc = SO_CUC[nap.split()[-1]]
        self.nap_am_cung_menh = nap
        self.ban_menh = NAP_AM[jiazi(c, y) // 2]
        n = self.cuc
        s = {}
        q = math.ceil(d / n)
        r = q * n - d
        tv = md(q + 1 + r) if r % 2 == 0 else md(q + 1 - r)
        for ten, o in [('Tử Vi', 0), ('Thiên Cơ', -1), ('Thái Dương', -3), ('Vũ Khúc', -4),
                       ('Thiên Đồng', -5), ('Liêm Trinh', -8)]:
            s[ten] = md(tv + o)
        tp = md(4 - tv)
        for ten, o in [('Thiên Phủ', 0), ('Thái Âm', 1), ('Tham Lang', 2), ('Cự Môn', 3),
                       ('Thiên Tướng', 4), ('Thiên Lương', 5), ('Thất Sát', 6), ('Phá Quân', 10)]:
            s[ten] = md(tp + o)
        lt = LOC_TON[c]
        s['Lộc Tồn'], s['Kình Dương'], s['Đà La'] = lt, md(lt + 1), md(lt - 1)
        s['Văn Xương'], s['Văn Khúc'] = md(10 - h), md(4 + h)
        s['Tả Phù'], s['Hữu Bật'] = md(m + 3), md(11 - m)
        s['Địa Kiếp'], s['Địa Không'] = md(11 + h), md(11 - h)
        g = NHOM(y)
        hk, lk = {0: (2, 10), 1: (3, 10), 2: (1, 3), 3: (9, 10)}[g]
        if self.thuan:
            s['Hỏa Tinh'], s['Linh Tinh'] = md(hk + h), md(lk - h)
        else:
            s['Hỏa Tinh'], s['Linh Tinh'] = md(hk - h), md(lk + h)
        s['Thiên Khôi'], s['Thiên Việt'] = KHOI_VIET[c]
        s['Thiên Mã'] = {0: 2, 1: 11, 2: 8, 3: 5}[g]
        s['Đào Hoa'] = {0: 9, 1: 6, 2: 3, 3: 0}[g]
        s['Hoa Cái'] = {0: 4, 1: 1, 2: 10, 3: 7}[g]
        s['Kiếp Sát'] = {0: 5, 1: 2, 2: 11, 3: 8}[g]
        s['Phá Toái'] = {0: 5, 6: 5, 3: 5, 9: 5, 2: 9, 8: 9, 5: 9, 11: 9}.get(y, 1)
        s['Hồng Loan'] = md(3 - y)
        s['Thiên Hỷ'] = md(3 - y + 6)
        cq = {11: (2, 10), 0: (2, 10), 1: (2, 10), 2: (5, 1), 3: (5, 1), 4: (5, 1),
              5: (8, 4), 6: (8, 4), 7: (8, 4), 8: (11, 7), 9: (11, 7), 10: (11, 7)}[y]
        s['Cô Thần'], s['Quả Tú'] = cq
        s['Thiên Hình'], s['Thiên Riêu'] = md(m + 8), md(m)
        s['Thiên Y'] = md(m)
        s['Thiên Khốc'], s['Thiên Hư'] = md(6 - y), md(6 + y)
        s['Long Trì'], s['Phượng Các'] = md(4 + y), md(10 - y)
        s['Giải Thần'] = md(10 - y)
        s['Tam Thai'] = md(s['Tả Phù'] + d - 1)
        s['Bát Tọa'] = md(s['Hữu Bật'] - (d - 1))
        s['Ân Quang'] = md(s['Văn Xương'] + d - 2)
        s['Thiên Quý'] = md(s['Văn Khúc'] - (d - 2))
        s['Thai Phụ'], s['Phong Cáo'] = md(s['Văn Khúc'] + 2), md(s['Văn Khúc'] - 2)
        s['Thiên Tài'], s['Thiên Thọ'] = md(self.menh + y), md(self.than + y)
        s['Thiên Giải'], s['Địa Giải'] = md(m + 7), md(m + 6)
        s['Nguyệt Đức'], s['Thiên Đức'] = md(5 + y), md(9 + y)
        s['Thiên Không'] = md(y + 1)
        s['Thiên La'], s['Địa Võng'] = 4, 10
        s['Thiên Thương'], s['Thiên Sứ'] = md(self.menh + 5), md(self.menh + 7)
        s['Đẩu Quân'] = md(y - (m - 1) + h)
        s['Quốc Ấn'], s['Đường Phù'] = md(lt + 8), md(lt - 7)
        for i, ten in enumerate(VONG_THAI_TUE):
            s[ten] = md(y + i)
        huong = 1 if self.thuan else -1
        for i, ten in enumerate(VONG_BAC_SI):
            s[ten] = md(lt + huong * i)
        ts = TRANG_SINH_KHOI[n]
        for i, ten in enumerate(VONG_TRANG_SINH):
            s[ten] = md(ts + huong * i)
        for ten, goc in zip(HOA, TU_HOA[c]):
            s[ten] = s[goc]
        self.sao = s
        self.hoa_goc = dict(zip(HOA, TU_HOA[c]))
        self.tuan = {md(y - c - 2), md(y - c - 1)}
        self.triet = set(TRIET[c])
        self.dai_han = {md(self.menh + huong * k): n + 10 * k for k in range(12)}
        self.tieu_han_khoi = {0: 10, 1: 7, 2: 4, 3: 1}[g]

    def vi_tri_chuc(self, chuc):
        return next(z for z, c in self.chuc.items() if chuan(c) == chuan(chuc))

    def sao_tai(self, z):
        return [ten for ten, p in self.sao.items() if p == z]

    def chinh_tinh_tai(self, z):
        return [t for t in CHINH_TINH if self.sao[t] == z]

    def tuoi_am(self, nam_xem):
        return nam_xem - self.nam_am + 1

    def tieu_han(self, nam_xem):
        a = self.tuoi_am(nam_xem)
        return md(self.tieu_han_khoi + (a - 1 if self.nam else -(a - 1)))

    def dai_han_tai(self, nam_xem):
        a = self.tuoi_am(nam_xem)
        for z, bd in self.dai_han.items():
            if bd <= a <= bd + 9:
                return z
        return None

    def luu(self, nam_xem):
        """Các sao lưu và cung hạn của năm xem."""
        yc, yz = (nam_xem + 6) % 10, (nam_xem + 8) % 12
        lt = LOC_TON[yc]
        l = {'Tiểu hạn': self.tieu_han(nam_xem), 'Lưu Thái Tuế': yz, 'Lưu Tang Môn': md(yz + 2),
             'Lưu Tuế Phá': md(yz + 6), 'Lưu Bạch Hổ': md(yz + 8), 'Lưu Lộc Tồn': lt,
             'Lưu Kình Dương': md(lt + 1), 'Lưu Đà La': md(lt - 1),
             'Lưu Thiên Mã': {0: 2, 1: 11, 2: 8, 3: 5}[NHOM(yz)]}
        hoa = {}
        for ten, goc in zip(HOA, TU_HOA[yc]):
            l['Lưu ' + ten] = self.sao[goc]
            hoa[ten] = goc
        return l, hoa, yc, yz


# ---------------------------------------------------------------- Cấu trúc và kích hoạt

def tam_phuong(z):
    return [md(z + 4), md(z + 8)]


def dac_diem(ls, z):
    """Danh sách đặc điểm cấu trúc của cung z, dùng cho tần suất nền."""
    out = []
    s = ls.sao
    tptc = {z, md(z + 6), md(z + 4), md(z + 8)}
    if not ls.chinh_tinh_tai(z):
        out.append('Vô chính diệu')
    if z in ls.tuan:
        out.append('Tuần')
    if z in ls.triet:
        out.append('Triệt')
    if s['Lộc Tồn'] not in tptc and s['Hóa Lộc'] not in tptc:
        out.append('Vô Lộc')
    for h in HOA:
        if s[h] == z:
            out.append(h + ' tọa thủ')
    if s['Hóa Kỵ'] == md(z + 6):
        out.append('Hóa Kỵ xung chiếu')
    if s['Lộc Tồn'] == z:
        out.append('Lộc Tồn tọa thủ')
    n_sat = sum(1 for t in LUC_SAT if s[t] == z)
    if n_sat >= 1:
        out.append('Có sát tinh tọa thủ')
    if n_sat >= 2:
        out.append('Từ 2 sát tinh tọa thủ')
    for ten, a, b in GIAP_CO_TEN:
        if {s[a], s[b]} == {md(z - 1), md(z + 1)}:
            out.append('Giáp ' + ten)
    if s['Lộc Tồn'] in tptc and s['Hóa Lộc'] in tptc:
        out.append('Song Lộc hội')
    if all(s[h] in tptc for h in HOA[:3]):
        out.append('Khoa Quyền Lộc hội')
    if s['Cô Thần'] in tptc or s['Quả Tú'] in tptc:
        out.append('Cô Thần/Quả Tú hội')
    if s['Hồng Loan'] in tptc or s['Thiên Hỷ'] in tptc:
        out.append('Hồng Loan/Thiên Hỷ hội')
    if s['Đào Hoa'] in tptc:
        out.append('Đào Hoa hội')
    if ls.than == z:
        out.append('Thân cư')
    return out


def ung_vien_cach(ls, z):
    s = ls.sao
    tptc = {z, md(z + 6), md(z + 4), md(z + 8)}
    out = []
    if s['Tử Vi'] == s['Thiên Phủ'] == z:
        out.append('Tử Phủ đồng cung')
    if s['Cự Môn'] == s['Thái Dương'] == z:
        out.append('Cự Nhật đồng cung')
    if all(s[t] in tptc for t in ['Tử Vi', 'Thiên Phủ', 'Vũ Khúc', 'Thiên Tướng']):
        out.append('Tử Phủ Vũ Tướng hội')
    if all(s[t] in tptc for t in ['Thiên Cơ', 'Thái Âm', 'Thiên Đồng', 'Thiên Lương']):
        out.append('Cơ Nguyệt Đồng Lương hội')
    if any(s[t] == z for t in ['Thất Sát', 'Phá Quân', 'Tham Lang']):
        out.append('Sát Phá Tham')
    if (z == ls.menh and z == 7 and not ls.chinh_tinh_tai(z)
            and s['Thái Dương'] == 3 and s['Thái Âm'] == 11):
        out.append('Minh Châu xuất hải (Mệnh VCD tại Mùi, Nhật Mão, Nguyệt Hợi)')
    if (s['Lộc Tồn'] in tptc or s['Hóa Lộc'] in tptc) and s['Thiên Mã'] in tptc:
        out.append('Lộc Mã giao trì (Lộc và Mã cùng trong tam phương tứ chính)')
    if (s['Lộc Tồn'] == z or s['Hóa Lộc'] == z) and (s['Địa Không'] == z or s['Địa Kiếp'] == z):
        out.append('Lộc phùng Không Kiếp')
    return out


def kich_hoat(ls, nam_xem, z, l=None, dh=None):
    """Lớp hạn kích hoạt cung z theo L§6.4. Trả về (lớp đại hạn, lớp năm, ghi nhận)."""
    if l is None:
        dh = ls.dai_han_tai(nam_xem)
        l = ls.luu(nam_xem)[0]
    lop_dh = []
    if dh == z:
        lop_dh.append('cung đại hạn')
    elif dh == md(z + 6):
        lop_dh.append('cung đại hạn xung chiếu')
    lop_nam = []
    if l['Tiểu hạn'] == z:
        lop_nam.append('cung tiểu hạn')
    if l['Lưu Thái Tuế'] == z:
        lop_nam.append('cung lưu Thái Tuế')
    nhom_luu = ['Lưu Hóa Lộc', 'Lưu Hóa Quyền', 'Lưu Hóa Khoa', 'Lưu Hóa Kỵ', 'Lưu Lộc Tồn']
    toa = [k for k in nhom_luu if l[k] == z]
    if len(toa) >= 2:
        lop_nam.append(' + '.join(toa) + ' tọa thủ')
    ghi_nhan = []
    if len(toa) == 1:
        ghi_nhan.append(toa[0] + ' tọa thủ (một sao, không tính lớp)')
    for k, p in l.items():
        if k in nhom_luu and p == md(z + 6):
            ghi_nhan.append(k + ' xung chiếu')
        if k in ('Tiểu hạn', 'Lưu Thái Tuế') and p == md(z + 6):
            ghi_nhan.append(k + ' xung chiếu')
        if k in ('Lưu Kình Dương', 'Lưu Đà La', 'Lưu Thiên Mã', 'Lưu Tang Môn', 'Lưu Bạch Hổ',
                 'Lưu Tuế Phá') and p == z:
            ghi_nhan.append(k + ' tọa thủ')
    if dh in tam_phuong(z):
        ghi_nhan.append('đại hạn ở tam hợp')
    if l['Tiểu hạn'] in tam_phuong(z):
        ghi_nhan.append('tiểu hạn ở tam hợp')
    return lop_dh, lop_nam, ghi_nhan


# ---------------------------------------------------------------- Tần suất nền

def la_so_ngau_nhien(rng):
    c = rng.randrange(10)
    y = rng.choice([z for z in range(12) if (z - c) % 2 == 0])
    nam_am = 1984 + jiazi(c, y)
    return LaSo(nam_am, rng.randint(1, 12), rng.randint(1, 30), rng.randrange(12), rng.random() < 0.5)


def tan_suat_nen(n, seed=0):
    rng = random.Random(seed)
    dem = {k: {} for k in CUNG}
    lop = {k: [0, 0, 0] for k in CUNG}
    for _ in range(n):
        ls = la_so_ngau_nhien(rng)
        nam_xem = ls.nam_am + rng.randint(15, 70)
        l, dh = ls.luu(nam_xem)[0], ls.dai_han_tai(nam_xem)
        for z in range(12):
            chuc = ls.chuc[z]
            for f in dac_diem(ls, z):
                dem[chuc][f] = dem[chuc].get(f, 0) + 1
            a, b, _ = kich_hoat(ls, nam_xem, z, l, dh)
            lop[chuc][0] += bool(a)
            lop[chuc][1] += bool(b)
            lop[chuc][2] += bool(a) and bool(b)
    return ({k: {f: v / n for f, v in d.items()} for k, d in dem.items()},
            {k: [v / n for v in x] for k, x in lop.items()})


def pct(p):
    if p is None:
        return '?'
    return f'{p * 100:.0f}%' if p >= 0.01 else f'{p * 100:.1f}%'


# ---------------------------------------------------------------- Đọc file

def chuan(ten):
    t = unicodedata.normalize('NFC', ten).strip().lower()
    return t.replace('sỹ', 'sĩ').replace('trường sinh', 'tràng sinh')


def doc_file(path):
    d = json.load(open(path, encoding='utf-8'))['data']
    b = d['person']['birth']
    ls = LaSo(b['lunar']['year'], b['lunar']['month'], b['lunar']['day'],
              canh_gio(b['time']['hour']), d['person']['genderCode'] == 1)
    return d, ls


# ---------------------------------------------------------------- Output

def ten_cung(ls, z):
    return f"{ls.chuc[z]} ({CAN[ls.can_cung[z]]} {CHI[z]})"


def in_dau_vao(out, duong, am, gio, phut, tz, nhuan=False, canh=None):
    out.append('## 1. Đầu vào (C§1)\n')
    if gio is None:
        out.append(f'- Chỉ biết canh **{CHI[canh]}**, không có giờ phút: không kiểm được giờ ranh; '
                   'report phải ghi rõ các kết luận phụ thuộc giờ (C§1.4).')
        gio, phut = 12, 0
    else:
        canh = canh_gio(gio)
        t = gio * 60 + phut
        moc = [60 * (2 * k + 1) for k in range(12)]
        kc = min(min(abs(t - b), 1440 - abs(t - b)) for b in moc)
        out.append(f'- Giờ sinh {gio:02d}:{phut:02d} = canh **{CHI[canh]}**, cách mốc chuyển canh gần nhất **{kc} phút**.')
        if kc <= 15:
            out.append('  - ⚠️ **Giờ ranh** (≤ 15 phút): xem mục "Lá số canh lân cận" bên dưới, hạ độ tin cậy các kết luận phụ thuộc giờ.')
        if gio == 23:
            out.append('  - ⚠️ **Giờ Tý đêm**: quy ước giữ ngày / sang ngày sau cho kết quả khác nhau (L§7).')
    if duong:
        dd, mm, yy = duong
        vn = duong_sang_am(dd, mm, yy, 7)
        cn = duong_sang_am(dd, mm, yy, 8)
        out.append(f'- Dương lịch {dd:02d}/{mm:02d}/{yy} → âm lịch Việt Nam (UTC+7): '
                   f'{vn[0]}/{vn[1]}{" nhuận" if vn[3] else ""}/{vn[2]}.')
        if cn != vn:
            out.append(f'  - ⚠️ Âm lịch Trung Quốc (UTC+8) khác: {cn[0]}/{cn[1]}{" nhuận" if cn[3] else ""}/{cn[2]}. '
                       'Phải dùng lịch Việt Nam.')
        if am and (am[0], am[1], am[2], am[3]) != vn:
            out.append(f'  - ❌ **LỆCH**: file ghi âm lịch {am[0]}/{am[1]}{" nhuận" if am[3] else ""}/{am[2]}.')
        elif am:
            out.append('  - ✅ Khớp ngày âm trong file.')
        try:
            off = datetime(yy, mm, dd, gio, phut, tzinfo=ZoneInfo('Asia/Ho_Chi_Minh')).utcoffset().total_seconds() / 3600
            dong = f'- Múi giờ pháp định theo tzdb (lịch sử Sài Gòn) lúc sinh: UTC+{off:g}.'
            if tz is not None and abs(off - tz) > 1e-6:
                dong += f' ⚠️ File ghi UTC+{tz:g}; nếu sinh ở miền Nam, giờ đồng hồ phải quy đổi (C§1.5).'
            if yy < 1976:
                dong += ' Người sinh ở miền Bắc trước 1976 cần tra riêng.'
            out.append(dong)
        except Exception:
            pass
    if nhuan:
        out.append('- ⚠️ **Tháng nhuận**: hai quy ước cho tháng khác nhau (C§1.6). Xem mục "Lá số theo quy ước nhuận chia đôi".')
    out.append('')


def in_tong_quan(out, ls):
    out.append('## 2. Lá số tính lại (C§3)\n')
    out.append(f'- Năm sinh âm: **{CAN[ls.c]} {CHI[ls.y]}**; bản mệnh {NAP_AM[jiazi(ls.c, ls.y) // 2]}; '
               f'{"nam" if ls.nam else "nữ"}, can năm {"dương" if ls.c % 2 == 0 else "âm"} → chiều vận **{"thuận" if ls.thuan else "nghịch"}**.')
    out.append(f'- Âm lịch dùng để an: ngày {ls.d}, tháng {ls.m}, canh giờ {CHI[ls.h]}.')
    out.append(f'- Mệnh tại **{CHI[ls.menh]}**; Thân tại **{CHI[ls.than]}** (Thân cư {ls.chuc[ls.than]}).')
    out.append(f'- Cục: {ls.nap_am_cung_menh} (cung Mệnh {CAN[ls.can_cung[ls.menh]]} {CHI[ls.menh]}) → **{TEN_CUC[ls.cuc]}**.')
    out.append(f'- Mệnh chủ (theo chi cung Mệnh): {MENH_CHU[ls.menh]}; Thân chủ (theo chi năm sinh): {THAN_CHU[ls.y]}. Hạng H6.')
    out.append(f'- Tuần: {", ".join(CHI[z] for z in sorted(ls.tuan))}; Triệt: {", ".join(CHI[z] for z in sorted(ls.triet))}.')
    out.append('- Tứ Hóa gốc (can ' + CAN[ls.c] + '): ' + '; '.join(
        f'{h}: {ls.hoa_goc[h]} ({CHI[ls.sao[h]]}, {ls.chuc[ls.sao[h]]})' for h in HOA) + '.')
    if ls.c in (6, 8):
        out.append('  - ⚠️ Tứ Hóa can ' + CAN[ls.c] + ' có khác biệt phái (C§4, L§7).')
    if ls.c == 6:
        out.append('  - ⚠️ Khôi–Việt can Canh theo sách Việt (Ngọ/Dần); sách Trung Hoa: Sửu/Mùi (L§7).')
    out.append('')


def in_doi_chieu(out, d, ls):
    out.append('## 3. Đối chiếu với file (C§7)\n')
    file_sao = {}
    for p in d['chart']['palaces']:
        z = CHI.index(p['earthlyBranch'])
        for st in p['stars']:
            file_sao.setdefault(chuan(st['name']), set()).add(z)
    tinh = {chuan(k): v for k, v in ls.sao.items()}
    khop, lech, khong_tinh = 0, [], []
    for ten, v in tinh.items():
        if ten not in file_sao:
            continue
        if file_sao[ten] == {v}:
            khop += 1
        else:
            lech.append((ten, v, file_sao[ten]))
    for ten in file_sao:
        if ten not in tinh:
            khong_tinh.append(ten)
    out.append(f'- Khớp **{khop}** sao; lệch **{len(lech)}** sao.')
    for ten, v, f in lech:
        loi = '❌ LỆCH SAO LÕI' if any(chuan(x) == ten for x in SAO_LOI) else '⚠️ lệch'
        out.append(f'  - {loi}: {ten} — tính ra {CHI[v]}, file ghi {", ".join(CHI[z] for z in sorted(f))}')
    if khong_tinh:
        out.append(f'- Có trong file nhưng script không tính (chưa có công thức đã kiểm): {", ".join(sorted(khong_tinh))}.')
    lech_truong = []
    nam_file = d['reading']['year']
    th = ls.tieu_han(nam_file)
    l, _, _, _ = ls.luu(nam_file)
    thang_gieng = md(th - (ls.m - 1) + ls.h)
    for p in d['chart']['palaces']:
        z = CHI.index(p['earthlyBranch'])
        cy = p['cycles']
        if cy['majorAge'] != ls.dai_han[z]:
            lech_truong.append(f'majorAge tại {CHI[z]}')
        nhan = CHI[md(ls.y + (z - ls.tieu_han_khoi) * (1 if ls.nam else -1))]
        if cy['annualBranch'] != nhan:
            lech_truong.append(f'annualBranch tại {CHI[z]}')
        if cy['monthlyIndex'] != md(z - thang_gieng) + 1:
            lech_truong.append(f'monthlyIndex tại {CHI[z]}')
        if p['restrictions']['tuan'] != (z in ls.tuan) or p['restrictions']['triet'] != (z in ls.triet):
            lech_truong.append(f'Tuần/Triệt tại {CHI[z]}')
        if p['palace'] and chuan(p['palace']) != chuan(ls.chuc[z]):
            lech_truong.append(f'tên cung tại {CHI[z]}')
    if lech_truong:
        out.append('- ❌ Trường lệch: ' + '; '.join(lech_truong))
    else:
        out.append('- ✅ `majorAge`, `annualBranch` (nhãn tiểu hạn), `monthlyIndex` (nguyệt hạn phép Việt, '
                   f'năm {nam_file}), Tuần/Triệt, tên cung: khớp cả 12 cung.')
    out.append('- Độ sáng (`dignity`) và nhãn `nature` lấy theo phần mềm, script không kiểm (C§8, D§2).\n')


def in_canh_lan_can(out, ls, gio, phut):
    if gio is None:
        return
    t = gio * 60 + phut
    moc = [60 * (2 * k + 1) for k in range(12)]
    b = min(moc, key=lambda x: min(abs(t - x), 1440 - abs(t - x)))
    kc = min(abs(t - b), 1440 - abs(t - b))
    if kc > 15:
        return
    h2 = md(ls.h + (1 if (t - b) % 1440 > 720 else -1))
    ls2 = LaSo(ls.nam_am, ls.m, ls.d, h2, ls.nam)
    out.append(f'## Lá số canh lân cận: canh {CHI[h2]} (C§1.4)\n')
    doi = []
    if ls2.menh != ls.menh:
        doi.append(f'Mệnh {CHI[ls.menh]} → {CHI[ls2.menh]}')
    if ls2.than != ls.than:
        doi.append(f'Thân cư {ls.chuc[ls.than]} → {ls2.chuc[ls2.than]}')
    if ls2.cuc != ls.cuc:
        doi.append(f'cục {TEN_CUC[ls.cuc]} → {TEN_CUC[ls2.cuc]}')
    for ten in ls.sao:
        if ten in SAO_LOI and ls.sao[ten] != ls2.sao[ten]:
            doi.append(f'{ten} {CHI[ls.sao[ten]]} → {CHI[ls2.sao[ten]]}')
    out.append('- Thay đổi: ' + ('; '.join(doi) if doi else 'không có sao lõi nào đổi') + '\n')


def in_cau_truc(out, ls, cung_loc, ts, d=None):
    out.append('## 4. Cấu trúc cung (L§1, L§5) — kèm tần suất nền (Q§5.1)\n')
    out.append('Tần suất nền = tỉ lệ lá số ngẫu nhiên có cùng đặc điểm tại **cùng cung chức**. '
               'Đặc điểm càng phổ biến càng ít sức phân biệt.\n')
    do_sang = {}
    if d:
        for p in d['chart']['palaces']:
            z = CHI.index(p['earthlyBranch'])
            for st in p['stars']:
                if st.get('dignity'):
                    do_sang[(chuan(st['name']), z)] = st['dignity']
    for k in range(12):
        z = md(ls.menh + k)
        if cung_loc:
            goc = ls.vi_tri_chuc(cung_loc)
            if z not in (goc, md(goc + 6), *tam_phuong(goc)):
                continue
        chuc = ls.chuc[z]

        def ghi(t):
            ds = do_sang.get((chuan(t), z))
            return f'{t} ({ds})' if ds else t
        ct = ls.chinh_tinh_tai(z)
        dong = f'### {ten_cung(ls, z)}'
        if z == ls.than:
            dong += ' · Thân cư'
        out.append(dong + '\n')
        if ct:
            out.append('- Chính tinh: ' + ', '.join(ghi(t) for t in ct))
        else:
            muon = ls.chinh_tinh_tai(md(z + 6))
            out.append('- Vô chính diệu → mượn chính tinh xung chiếu (H2): ' + (', '.join(muon) or 'không có'))
        sat = [ghi(t) for t in LUC_SAT if ls.sao[t] == z]
        cat = [ghi(t) for t in LUC_CAT if ls.sao[t] == z]
        if sat:
            out.append('- Lục sát tọa thủ: ' + ', '.join(sat))
        if cat:
            out.append('- Lục cát tọa thủ: ' + ', '.join(cat))
        hoa = []
        for h in HOA:
            p = ls.sao[h]
            if p == z:
                hoa.append(f'{h} ({ls.hoa_goc[h]}) tọa thủ')
            elif p == md(z + 6):
                hoa.append(f'{h} ({ls.hoa_goc[h]}) xung chiếu từ {CHI[p]}')
            elif p in tam_phuong(z):
                hoa.append(f'{h} ({ls.hoa_goc[h]}) tam hợp từ {CHI[p]}')
        out.append('- Tứ Hóa gốc: ' + ('; '.join(hoa) if hoa else 'không có trong tam phương tứ chính'))
        con = [t for t in ls.sao_tai(z) if t not in CHINH_TINH + LUC_SAT + LUC_CAT + HOA]
        out.append('- Sao khác tọa thủ: ' + ', '.join(ghi(t) for t in con))
        out.append(f'- Tam hợp: {ten_cung(ls, md(z + 4))}, {ten_cung(ls, md(z + 8))}; '
                   f'xung chiếu: {ten_cung(ls, md(z + 6))}; giáp: {CHI[md(z - 1)]}, {CHI[md(z + 1)]}.')
        dd = dac_diem(ls, z)
        out.append('- Đặc điểm: ' + ('; '.join(f'{f} ({pct(ts[chuc].get(f, 0.0))})' for f in dd) if dd else '—'))
        cach = ung_vien_cach(ls, z)
        if cach:
            out.append('- Ứng viên cách (điều kiện vị trí đã đủ; còn phải kiểm phá cách L§5.3): ' + '; '.join(cach))
        out.append('')


def in_han(out, ls, nam_xem, cung_loc, lop_nen):
    a = ls.tuoi_am(nam_xem)
    l, hoa, yc, yz = ls.luu(nam_xem)
    dh = ls.dai_han_tai(nam_xem)
    out.append(f'## 5. Hạn năm {CAN[yc]} {CHI[yz]} {nam_xem} — tuổi âm {a} (C§6, L§6)\n')
    if dh is None:
        out.append('- Tuổi âm nằm ngoài các đại hạn đã an.\n')
        return
    out.append(f'- **Đại hạn** {ls.dai_han[dh]}–{ls.dai_han[dh] + 9}: {ten_cung(ls, dh)}.')
    chuc_dh = ', '.join(f'{CUNG[k]} = {CHI[md(dh + k)]}' for k in range(1, 12))
    out.append(f'  - Đại hạn cung chức (L§6.2b): {chuc_dh}.')
    cdh = ls.can_cung[dh]
    out.append('  - Tứ Hóa đại hạn theo can ' + CAN[cdh] + ' (tùy phái, không tính lớp): ' + '; '.join(
        f'{h}: {g} ({CHI[ls.sao[g]]}, {ls.chuc[ls.sao[g]]})' for h, g in zip(HOA, TU_HOA[cdh])) + '.')
    out.append(f'- **Tiểu hạn**: {ten_cung(ls, l["Tiểu hạn"])}.')
    out.append(f'- **Lưu Thái Tuế**: {ten_cung(ls, yz)}; lưu Tang Môn {CHI[l["Lưu Tang Môn"]]}, '
               f'lưu Tuế Phá {CHI[l["Lưu Tuế Phá"]]} ({ls.chuc[l["Lưu Tuế Phá"]]}), lưu Bạch Hổ {CHI[l["Lưu Bạch Hổ"]]}.')
    out.append(f'- Lưu Lộc Tồn {CHI[l["Lưu Lộc Tồn"]]} ({ls.chuc[l["Lưu Lộc Tồn"]]}), lưu Kình {CHI[l["Lưu Kình Dương"]]}, '
               f'lưu Đà {CHI[l["Lưu Đà La"]]}, lưu Thiên Mã {CHI[l["Lưu Thiên Mã"]]}.')
    out.append('- **Lưu Tứ Hóa** (can ' + CAN[yc] + '): ' + '; '.join(
        f'{h}: {hoa[h]} ({CHI[l["Lưu " + h]]}, {ls.chuc[l["Lưu " + h]]})' for h in HOA) + '.')
    th = l['Tiểu hạn']
    vn = md(th - (ls.m - 1) + ls.h)
    tq = md(yz - (ls.m - 1) + ls.h)
    out.append(f'- Nguyệt hạn tháng Giêng: phép Việt (khởi từ tiểu hạn) tại {CHI[vn]}; '
               f'phép Trung Hoa (khởi từ lưu Thái Tuế) tại {CHI[tq]}. Các tháng sau đi thuận. Mức tin cậy tối đa: Thấp.\n')
    out.append('### Kích hoạt theo lớp (L§6.4)\n')
    out.append('| Cung | Lớp đại hạn | Lớp năm | Ghi nhận, không tính lớp |')
    out.append('|---|---|---|---|')
    for k in range(12):
        z = md(ls.menh + k)
        if cung_loc and ls.chuc[z] != cung_loc:
            continue
        a1, b1, g1 = kich_hoat(ls, nam_xem, z)
        out.append(f'| {ten_cung(ls, z)} | {"✅ " + "; ".join(a1) if a1 else "—"} | '
                   f'{"✅ " + "; ".join(b1) if b1 else "—"} | {"; ".join(g1) or "—"} |')
    if lop_nen:
        m0 = sum(v[0] for v in lop_nen.values()) / 12
        m1 = sum(v[1] for v in lop_nen.values()) / 12
        m2 = sum(v[2] for v in lop_nen.values()) / 12
        out.append(f'\nTần suất nền (trung bình mọi cung): lớp đại hạn {pct(m0)}, lớp năm {pct(m1)}, '
                   f'cả hai cùng lúc {pct(m2)}.\n')


def in_doi_chung(out, n, seed):
    rng = random.Random(seed)
    out.append(f'# Lá số đối chứng ngẫu nhiên (seed {seed}) — dùng cho phép thử phân biệt Q§5.1\n')
    for i in range(n):
        ls = la_so_ngau_nhien(rng)
        out.append(f'## Đối chứng {i + 1}: {CAN[ls.c]} {CHI[ls.y]}, tháng {ls.m}, ngày {ls.d}, '
                   f'canh {CHI[ls.h]}, {"nam" if ls.nam else "nữ"}; Mệnh {CHI[ls.menh]}, Thân cư {ls.chuc[ls.than]}\n')
        for k in range(12):
            z = md(ls.menh + k)
            ct = ', '.join(ls.chinh_tinh_tai(z)) or 'VCD'
            sat = ', '.join(t for t in LUC_SAT if ls.sao[t] == z)
            hoa = ', '.join(h for h in HOA if ls.sao[h] == z)
            khac = ', '.join(dac_diem(ls, z))
            out.append(f'- {ls.chuc[z]} ({CHI[z]}): {ct}' + (f' | sát: {sat}' if sat else '')
                       + (f' | {hoa}' if hoa else '') + (f' | {khac}' if khac else ''))
        out.append('')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('file', nargs='?', help='file .data.json (schema 1.0.0)')
    ap.add_argument('--duong-lich', help='YYYY-MM-DD, dùng khi không có file')
    ap.add_argument('--am-lich', help='YYYY-MM-DD âm lịch (năm âm), dùng khi không có file')
    ap.add_argument('--nhuan', action='store_true', help='tháng âm là tháng nhuận (với --am-lich)')
    ap.add_argument('--gio', help='HH:MM, hoặc tên canh (ví dụ Dậu) khi chỉ biết canh')
    ap.add_argument('--gioi', choices=['nam', 'nu'])
    ap.add_argument('--ten', default='')
    ap.add_argument('--nam-xem', type=int)
    ap.add_argument('--cung', help='chỉ in cung chủ đề và tam phương tứ chính, ví dụ "Phu Thê"')
    ap.add_argument('--mau', type=int, default=10000, help='số lá số ngẫu nhiên để tính tần suất nền')
    ap.add_argument('--doi-chung', type=int, help='in N lá số đối chứng ngẫu nhiên rồi thoát')
    ap.add_argument('--seed', type=int, default=0)
    a = ap.parse_args()

    out = []
    if a.doi_chung:
        in_doi_chung(out, a.doi_chung, a.seed)
        print('\n'.join(out))
        return

    d = None
    if a.file:
        d, ls = doc_file(a.file)
        b = d['person']['birth']
        duong = (b['solar']['day'], b['solar']['month'], b['solar']['year'])
        am = (b['lunar']['day'], b['lunar']['month'], b['lunar']['year'], b['lunar']['isLeapMonth'])
        gio, phut, tz = b['time']['hour'], b['time']['minute'], b['time'].get('timezone')
        ten = d['person']['name']
        nam_xem = a.nam_xem or d['reading']['year']
        nh = am[3]
        canh = None
    else:
        if not (a.gio and a.gioi and (a.duong_lich or a.am_lich)):
            ap.error('cần file, hoặc --gio, --gioi và --duong-lich/--am-lich')
        canh = None
        if chuan(a.gio) in [chuan(c) for c in CHI]:
            canh = [chuan(c) for c in CHI].index(chuan(a.gio))
            gio, phut = None, None
        else:
            gio, phut = map(int, a.gio.split(':'))
        tz = 7
        if a.duong_lich:
            yy, mm, dd = map(int, a.duong_lich.split('-'))
            duong = (dd, mm, yy)
            ad, am_, ay, nh = duong_sang_am(dd, mm, yy, 7)
        else:
            ay, am_, ad = map(int, a.am_lich.split('-'))
            nh = a.nhuan
            duong = None
        am = None
        ls = LaSo(ay, am_, ad, canh if gio is None else canh_gio(gio), a.gioi == 'nam')
        ten = a.ten
        nam_xem = a.nam_xem or datetime.now().year
    cung_loc = None
    if a.cung:
        cung_loc = next((c for c in CUNG if chuan(c) == chuan(a.cung)), None)
        if not cung_loc:
            ap.error('không có cung ' + a.cung)

    ts, lop_nen = tan_suat_nen(a.mau, 0) if a.mau else ({k: {} for k in CUNG}, None)

    out.append(f'# Kiểm tra lá số{" — " + ten if ten else ""}\n')
    out.append(f'_Sinh bởi `scripts/kiem-tra-la-so.py`; tần suất nền từ {a.mau} lá số ngẫu nhiên (seed 0)._\n')
    in_dau_vao(out, duong, am, gio, phut, tz, nh, canh)
    in_tong_quan(out, ls)
    if nh and ls.d >= 16:
        ls2 = LaSo(ls.nam_am, ls.m % 12 + 1, ls.d, ls.h, ls.nam)
        out.append(f'## Lá số theo quy ước nhuận chia đôi: tháng {ls2.m} (C§1.6)\n')
        doi = [f'{t} {CHI[ls.sao[t]]} → {CHI[ls2.sao[t]]}' for t in ls.sao
               if t in SAO_LOI and ls.sao[t] != ls2.sao[t]]
        out.append('- Thay đổi: ' + ('; '.join(doi) if doi else 'không có sao lõi nào đổi') + '\n')
    in_canh_lan_can(out, ls, gio, phut)
    if d:
        in_doi_chieu(out, d, ls)
    in_cau_truc(out, ls, cung_loc, ts, d)
    in_han(out, ls, nam_xem, cung_loc, lop_nen)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
