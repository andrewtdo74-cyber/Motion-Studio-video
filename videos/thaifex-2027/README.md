# Video hướng dẫn THAIFEX 2027

Video hướng dẫn (tiếng Việt) **"THAIFEX 2027: Những điểm công ty trưng bày cần lưu ý"** dành cho doanh nghiệp thực phẩm & đồ uống Việt Nam trưng bày tại hội chợ THAIFEX (IMPACT, Bangkok, tháng 5).

- Thời lượng: ~2 phút 53 giây, 1920×1080, 9 cảnh
- Cách làm: hoạt hình vẽ phẳng (không quay thật, không nhân vật), lồng tiếng AI
- Công cụ: [HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP) qua skill Motion Studio
- Giọng đọc: ElevenLabs, giọng **HuyenTrang**, model Eleven v3 (bản cũ dùng Edge TTS HoaiMy)

## Nội dung video

Kể theo hành trình **4 bước**:

| Cảnh | Nội dung |
|---|---|
| 1 | Mở đầu: "Quý vị đang quan tâm trưng bày tại THAIFEX 2027?" + bảng LƯU Ý |
| 2 | Hành trình 4 bước: Chuẩn bị → Gửi hàng → Tại Bangkok → Kết thúc |
| 3 | Bước 1: chọn loại gian hàng (Quốc gia, tiêu chuẩn, gian thô) và thiết bị thuê thêm |
| 4 | Bước 1: hồ sơ đăng ký, ngân sách, thanh toán |
| 5 | Bước 2: gửi hàng mẫu, chỗ dễ sai nhất (khai báo hải quan, giấy phép nhập khẩu trước 2 tuần) |
| 6 | Bước 3: đến Bangkok (vé, khách sạn, bảo hiểm, xe van, thanh toán) |
| 7 | Bước 3: khách mua hàng đến từ đâu |
| 8 | Bước 4: hoàn trả gian hàng khi hội chợ kết thúc |
| 9 | Kêu gọi: quét mã QR nhận bộ tài liệu |

## Cấu trúc thư mục

```
videos/thaifex-2027/
├── README.md                 ← file này
├── LOG-CHINH-SUA.xlsx        ← nhật ký mọi lần chỉnh sửa (ngày giờ, cảnh, nội dung, lý do)
├── docs/                     ← yêu cầu, kế hoạch, kịch bản, lời đọc, báo cáo
│   ├── YEU-CAU-VIDEO-THAIFEX-2026.md, KE-HOACH-..., KICH-BAN-V3.md
│   ├── script-v3.md          ← lời thoại gốc s1–s9
│   ├── LOI-DOC-ANNA-THU.md   ← 13 đoạn lời đọc chia theo file giọng
│   └── bao-cao-tom-tat.md, bao-cao-chi-tiet.md
├── index.html                ← file chính: thứ tự cảnh, giọng, hiệu ứng âm thanh
├── compositions/frames/      ← 9 file cảnh (01-mo-dau.html … 09-cta.html)
├── assets/
│   ├── voice-huyentrang/     ← giọng đọc đang dùng (ElevenLabs)
│   ├── voice/                ← giọng cũ (Edge TTS)
│   ├── sfx/, music-long.wav  ← hiệu ứng âm thanh, nhạc nền
│   └── fonts/                ← Be Vietnam Pro
├── tools/                    ← script hỗ trợ (tạo giọng, canh thời gian)
└── renders/                  ← file MP4 xuất ra (không đưa lên GitHub)
```

## Cách làm việc với project

Cần Node.js và Python. Mở terminal trong thư mục này (`videos/thaifex-2027`):

```bash
npx hyperframes@0.8.181 preview      # xem trước trong trình duyệt
npx hyperframes@0.8.181 lint         # kiểm tra lỗi
npx hyperframes@0.8.181 render --quality high --output renders/ten-file.mp4
```

### Tạo lại giọng đọc (ElevenLabs)

1. Tạo file `.env` ở thư mục gốc `Motion Studio` (dùng chung cho mọi dự án) với dòng `ELEVENLABS_API_KEY=...` (file này không lên GitHub).
2. Sửa lời trong `docs/LOI-DOC-ANNA-THU.md`.
3. Chạy `python tools/eleven_vo.py eleven_v3`.
4. Canh lại thời gian bằng `tools/retime_voice.py` (chạy trên bản đã commit với giọng cũ).

Cần gói ElevenLabs trả phí (Starter trở lên) mới dùng được giọng tiếng Việt trong Voice Library qua API.

## Lưu ý khi chỉnh sửa

- Không chạy lại `assemble-index`: file `index.html` đã sửa tay, chạy lại sẽ mất chỉnh sửa.
- Chữ có dấu trong biến (`data-composition-variables`) phải viết dạng `\uXXXX`, nếu không sẽ lỗi font.
- Không bịa ngày, hạn chót, giá, số liệu; chỉ dùng thông tin có trong tài liệu.
- Mỗi lần sửa nhớ ghi thêm một dòng vào `LOG-CHINH-SUA.xlsx`.

## Lịch sử phiên bản

| Bản | Ngày | Thay đổi chính |
|---|---|---|
| v1 | 09/11/2026 | 9 cảnh, ảnh gian hàng thật |
| v2 | 10/11/2026 | Vẽ lại gian hàng và bìa hồ sơ theo style phẳng |
| v3 | 10/11/2026 | Đổi "chặng" thành "bước" |
| v4 | 10/11/2026 | Sửa dấu "?" bị nghiêng |
| v5 | 10/11/2026 | Giọng ElevenLabs HuyenTrang, canh lại thời gian |
| (đang sửa) | 10/11/2026 | Số gian đổi thành NO.00; dự án chuyển sang thư mục thaifex-2027 |

Chi tiết từng lần sửa: xem `LOG-CHINH-SUA.xlsx`.
