param(
    [Parameter(Mandatory = $true)][string]$InputPath,
    [Parameter(Mandatory = $true)][string]$JsonOutputPath,
    [Parameter(Mandatory = $true)][string]$MarkdownOutputPath
)

$ErrorActionPreference = 'Stop'
$source = Get-Content -LiteralPath $InputPath -Raw -Encoding UTF8 | ConvertFrom-Json
$thienBan = $source.data.thienban
$diaBan = $source.data.diaban

$elements = @{ K = 'Kim'; M = 'Mộc'; T = 'Thủy'; H = 'Hỏa'; O = 'Thổ' }
$statuses = @{ M = 'Miếu'; V = 'Vượng'; Đ = 'Đắc'; B = 'Bình'; H = 'Hãm' }

function Convert-YinYang($value) {
    if ($value -eq 1) { return 'Dương' }
    if ($value -eq -1) { return 'Âm' }
    return $null
}

function Convert-Star($star) {
    [ordered]@{
        id = [int]$star.saoID
        name = [string]$star.saoTen
        element = $elements[[string]$star.saoNguHanh]
        polarity = Convert-YinYang $star.saoAmDuong
        nature = if ($star.saoTot -eq 1) { 'Cát' } elseif ($star.saoTot -eq 0) { 'Hung' } else { 'Trung tính' }
        categoryId = [int]$star.saoLoai
        constellation = if ([string]::IsNullOrWhiteSpace([string]$star.saoPhuongVi)) { $null } else { [string]$star.saoPhuongVi }
        dignity = if ($null -eq $star.saoDacTinh) { $null } else { $statuses[[string]$star.saoDacTinh] }
        isMain = ([int]$star.saoLoai -eq 1)
        isHighlighted = ([int]$star.inDam -eq 1)
        isLifeCycle = ([int]$star.vongTrangSinh -eq 1)
    }
}

$palaces = @($diaBan.thapNhiCung | ForEach-Object {
    $palace = $_
    [ordered]@{
        position = [int]$palace.cungSo
        earthlyBranch = [string]$palace.cungTen
        heavenlyStem = [string]$palace.cungCan
        element = [string]$palace.hanhCung
        polarity = Convert-YinYang $palace.cungAmDuong
        palace = [string]$palace.cungChu
        isBodyPalace = [bool]$palace.cungThan
        cycles = [ordered]@{
            majorAge = [int]$palace.cungDaiHan
            annualBranch = [string]$palace.cungTieuHan
            monthlyIndex = [int]$palace.cungNguyetHan
        }
        restrictions = [ordered]@{
            tuan = [bool]$palace.tuanTrung
            triet = [bool]$palace.trietLo
        }
        stars = @($palace.cungSao | ForEach-Object { Convert-Star $_ })
    }
})

$uiPalaces = @($palaces | ForEach-Object {
    $mainStars = @($_.stars | Where-Object { $_.isMain } | ForEach-Object {
        if ($_.dignity) { '{0} ({1})' -f $_.name, $_.dignity } else { $_.name }
    })
    $highlighted = @($_.stars | Where-Object { $_.isHighlighted -and -not $_.isMain } | ForEach-Object { $_.name })
    [ordered]@{
        position = $_.position
        title = $_.palace
        location = '{0} {1}' -f $_.heavenlyStem, $_.earthlyBranch
        element = $_.element
        isBodyPalace = $_.isBodyPalace
        mainStars = $mainStars
        highlightedStars = $highlighted
        restrictions = @(
            if ($_.restrictions.tuan) { 'Tuần' }
            if ($_.restrictions.triet) { 'Triệt' }
        )
        starCount = $_.stars.Count
    }
})

$machineData = [ordered]@{
    schemaVersion = '1.0.0'
    data = [ordered]@{
        person = [ordered]@{
            name = [string]$thienBan.ten
            gender = [string]$thienBan.namNu
            genderCode = [int]$thienBan.gioiTinh
            birth = [ordered]@{
                solar = [ordered]@{ day = [int]$thienBan.ngayDuong; month = [int]$thienBan.thangDuong; year = [int]$thienBan.namDuong }
                lunar = [ordered]@{ day = [int]$thienBan.ngayAm; month = [int]$thienBan.thangAm; year = [int]$thienBan.namAm; isLeapMonth = ([int]$thienBan.thangNhuan -ne 0) }
                time = [ordered]@{ hour = [int]$thienBan.hour; minute = [int]$thienBan.mins; timezone = [double]$thienBan.timeZone; pillar = [string]$thienBan.gioSinh }
            }
        }
        reading = [ordered]@{
            year = [int]$thienBan.namXem
            age = [int]$thienBan.tuoiXem
            generatedDate = [datetime]::ParseExact([string]$thienBan.today, 'dd/MM/yyyy', $null).ToString('yyyy-MM-dd')
            yearPillar = '{0} {1}' -f $thienBan.canNamXemTen, $thienBan.chiNamXemTen
        }
        chart = [ordered]@{
            lunarBirthMonth = [int]$diaBan.thangSinhAmLich
            lunarBirthHourBranchIndex = [int]$diaBan.gioSinhAmLich
            lifePalacePosition = [int]$diaBan.cungMenh
            bodyPalacePosition = [int]$diaBan.cungThan
            servantPalacePosition = [int]$diaBan.cungNoboc
            healthPalacePosition = [int]$diaBan.cungTatAch
            birthPillars = [ordered]@{
                year = '{0} {1}' -f $thienBan.canNamTen, $thienBan.chiNamTen
                month = '{0} {1}' -f $thienBan.canThangTen, $thienBan.chiThangTen
                day = '{0} {1}' -f $thienBan.canNgayTen, $thienBan.chiNgayTen
                hour = [string]$thienBan.gioSinh
            }
            destiny = [ordered]@{
                polarity = [string]$thienBan.amDuongNamSinh
                balance = [string]$thienBan.amDuongMenh
                element = $elements[[string]$thienBan.menh]
                destinyName = [string]$thienBan.banMenh
                configuration = [string]$thienBan.tenCuc
                relationship = [string]$thienBan.sinhKhac
            }
            palaces = $palaces
        }
    }
}

$json = $machineData | ConvertTo-Json -Depth 20
[System.IO.File]::WriteAllText($JsonOutputPath, $json + [Environment]::NewLine, [System.Text.UTF8Encoding]::new($false))

function Escape-Markdown([string]$value) {
    if ($null -eq $value) { return '' }
    return $value.Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
}

$solarBirth = '{0:00}/{1:00}/{2}' -f $thienBan.ngayDuong, $thienBan.thangDuong, $thienBan.namDuong
$lunarBirth = '{0:00}/{1:00}/{2}' -f $thienBan.ngayAm, $thienBan.thangAm, $thienBan.namAm
$birthTime = '{0:00}:{1:00} ({2})' -f $thienBan.hour, $thienBan.mins, $thienBan.gioSinh
$md = [System.Collections.Generic.List[string]]::new()
$md.Add(('# Lá số tử vi {0} — {1}' -f $thienBan.namXem, $thienBan.ten))
$md.Add('')
$md.Add('## Tổng quan')
$md.Add('')
$md.Add('| Thông tin | Giá trị |')
$md.Add('|---|---|')
$md.Add(('| Họ tên | {0} |' -f (Escape-Markdown $thienBan.ten)))
$md.Add(('| Giới tính | {0} |' -f $thienBan.namNu))
$md.Add(('| Ngày sinh dương lịch | {0} |' -f $solarBirth))
$md.Add(('| Ngày sinh âm lịch | {0} |' -f $lunarBirth))
$md.Add(('| Giờ sinh | {0} |' -f $birthTime))
$md.Add(('| Năm xem | {0} — {1} tuổi |' -f $thienBan.namXem, $thienBan.tuoiXem))
$md.Add(('| Bản mệnh | {0} |' -f $thienBan.banMenh))
$md.Add(('| Cục | {0} |' -f $thienBan.tenCuc))
$md.Add(('| Mệnh và Cục | {0} |' -f $thienBan.sinhKhac))
$md.Add(('| Âm dương | {0} |' -f $thienBan.amDuongMenh))
$md.Add('')
$md.Add('## Tổng hợp 12 cung')
$md.Add('')
$md.Add('| Cung | Vị trí | Chính tinh | Sao nổi bật | Tuần/Triệt | Ghi chú |')
$md.Add('|---|---|---|---|---|---|')
foreach ($palace in $uiPalaces) {
    $main = if ($palace.mainStars.Count) { $palace.mainStars -join ', ' } else { 'Vô chính diệu' }
    $highlight = if ($palace.highlightedStars.Count) { $palace.highlightedStars -join ', ' } else { '—' }
    $restriction = if ($palace.restrictions.Count) { $palace.restrictions -join ', ' } else { '—' }
    $note = if ($palace.isBodyPalace) { 'Thân cư' } else { '—' }
    $md.Add(('| {0} | {1} · {2} | {3} | {4} | {5} | {6} |' -f (Escape-Markdown $palace.title), (Escape-Markdown $palace.location), $palace.element, (Escape-Markdown $main), (Escape-Markdown $highlight), $restriction, $note))
}
$md.Add('')
$md.Add('## Chi tiết các cung')
foreach ($palace in $palaces) {
    $md.Add('')
    $headingNote = if ($palace.isBodyPalace) { ' · Thân cư' } else { '' }
    $md.Add(('### {0} — {1} {2}{3}' -f $palace.palace, $palace.heavenlyStem, $palace.earthlyBranch, $headingNote))
    $md.Add('')
    $flags = @()
    if ($palace.restrictions.tuan) { $flags += 'Tuần' }
    if ($palace.restrictions.triet) { $flags += 'Triệt' }
    $md.Add(('- Ngũ hành: **{0}**; Đại hạn: **{1} tuổi**; Tiểu hạn: **{2}**; Nguyệt hạn: **tháng {3}**.' -f $palace.element, $palace.cycles.majorAge, $palace.cycles.annualBranch, $palace.cycles.monthlyIndex))
    if ($flags.Count) { $md.Add(('- Án ngữ: **{0}**.' -f ($flags -join ', '))) }
    $md.Add('')
    $md.Add('| Nhóm sao | Danh sách |')
    $md.Add('|---|---|')
    foreach ($nature in @('Cát', 'Hung', 'Trung tính')) {
        $names = @($palace.stars | Where-Object { $_.nature -eq $nature } | ForEach-Object {
            if ($_.dignity) { '{0} ({1})' -f $_.name, $_.dignity } else { $_.name }
        })
        $value = if ($names.Count) { $names -join ', ' } else { '—' }
        $md.Add(('| {0} | {1} |' -f $nature, (Escape-Markdown $value)))
    }
}
$md.Add('')
$md.Add('> Thông tin tử vi chỉ mang tính tham khảo.')
$md.Add('')
[System.IO.File]::WriteAllLines($MarkdownOutputPath, $md, [System.Text.UTF8Encoding]::new($false))
