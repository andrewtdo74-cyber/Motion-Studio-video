# Kế hoạch làm video motion — THAIFEX 2026: Thông tin & Kế hoạch trưng bày tại Hội chợ

Làm hoàn toàn bằng **Claude Code** (tab Code trong app Claude Desktop) + **Remotion** (dựng video bằng React), lồng tiếng tiếng Việt bằng AI.

---

## 1. Công cụ

| Hạng mục | Công cụ | Ghi chú |
|---|---|---|
| Dựng & render video | Remotion (React) | Claude Code viết code, xem trước ở Remotion Studio, xuất MP4 |
| Lồng tiếng — bản nháp | Edge TTS (miễn phí) | Giọng `vi-VN-HoaiMyNeural` (nữ) / `vi-VN-NamMinhNeural` (nam) |
| Lồng tiếng — bản chính | ElevenLabs | Free ~10.000 ký tự/tháng nhưng **không được dùng thương mại**; gói Starter (~$5/tháng) để đăng công khai |
| Phương án khác | Google Cloud TTS, FPT.AI, Vbee | Giọng Việt tốt, có API |
| Thiết kế tinh chỉnh (tùy chọn) | Figma connector | |
| Nhạc nền | Nhạc không bản quyền | |

## 2. Cần chuẩn bị

- [ ] Cài **Node.js** bản LTS (nodejs.org) — bắt buộc
- [ ] Cài **Python** (nếu dùng Edge TTS cho bản nháp)
- [ ] Logo THAIFEX / công ty, hình minh họa gốc → bỏ vào `assets/`
- [ ] Chọn tỉ lệ: **16:9** (YouTube, chiếu sự kiện) hay **9:16** (Reels, TikTok) — hoặc cả hai
- [ ] (Bản chính) Tạo API key ElevenLabs, lưu vào file `.env` trong thư mục dự án — không dán vào chat

## 3. Cấu trúc thư mục

```
thaifex-video/
  KE-HOACH-VIDEO-THAIFEX-2026.md
  script.md          ← kịch bản + lời thoại từng cảnh
  .env               ← ELEVENLABS_API_KEY=... (không chia sẻ)
  src/scenes/        ← mỗi mục A–G một file
  assets/
    images/          ← logo, hình minh họa
    audio/voice/     ← giọng đọc từng cảnh
    audio/music/     ← nhạc nền
  out/               ← video xuất ra
```

## 4. Phân cảnh dự kiến (~2 phút)

| # | Cảnh | Nội dung chính | Thời lượng |
|---|---|---|---|
| 0 | Intro | THAIFEX 2026 — Thông tin & kế hoạch trưng bày | 6s |
| 1 | A. Trở thành công ty trưng bày | Lợi ích hội chợ quốc tế & gian hàng Quốc gia, các bước tham dự, quy trình đăng ký, ngân sách, brochure, hồ sơ, thanh toán | 15s |
| 2 | B. Kế hoạch trưng bày | B1 Dàn dựng gian hàng (Quốc gia / tiêu chuẩn / đất trống) · B2 Thuê thiết bị · B3 Dịch vụ khác · B4 Gửi hàng mẫu (lưu ý hải quan, giấy phép nhập khẩu trước 2 tuần) | 25s |
| 3 | C. Dàn dựng & tháo dỡ | Hoàn trả thiết bị, tháo dỡ sau hội chợ — trả lại đúng hiện trạng lúc nhận | 12s |
| 4 | D. Di chuyển & lưu trú | Tại VN: vé máy bay, khách sạn, bảo hiểm · Tại Bangkok: di chuyển đến IMPACT, ăn uống, ứng dụng gọi xe, tiền tệ (chuyển khoản / tiền mặt THB) | 20s |
| 5 | E. Quản lý khách thăm | (đang cập nhật) | 5s |
| 6 | F. Thông tin chia sẻ | Sản phẩm & khu vực IMPACT, cách trưng bày, bao bì mẫu mã, mời khách mua hàng (BTC, công ty tự mời, chương trình AFW – Công ty Phương Bắc) | 18s |
| 7 | G. Thông tin khác | Kinh tế XNK Thái Lan, quan hệ Việt–Thái, liên kết hữu ích, thời tiết tháng 5 | 10s |
| 8 | Outro | Kêu gọi công ty trưng bày điền form để nhận tài liệu chi tiết | 6s |

## 5. Quy trình

1. **Kịch bản** — Claude viết `script.md` (lời thoại từng cảnh) → bạn duyệt
2. **Nhận diện** — bảng màu đỏ đậm / xanh dương / xanh lá theo tài liệu, font Be Vietnam Pro
3. **Giọng nháp** — tạo bằng Edge TTS, thời lượng cảnh tự khớp theo audio
4. **Dựng motion** — chữ trượt vào, bullet hiện lần lượt, icon (tàu hàng, máy bay, gian hàng, bản đồ)
5. **Duyệt bản nháp** — xem ở Remotion Studio, góp ý chỉnh sửa
6. **Giọng chính** — tạo lại bằng ElevenLabs khi kịch bản đã chốt
7. **Render** — MP4 1080p (+ bản 9:16 nếu cần)

## 6. Mẹo lời thoại tiếng Việt cho TTS

- Viết đầy đủ chữ tắt: "BTC" → "Ban tổ chức", "DV" → "dịch vụ", "THB" → "bạt Thái"
- Thêm dấu phẩy để giọng ngắt hơi tự nhiên
- Nghe thử cách đọc "2026", "IMPACT", "AFW" và sửa phiên âm nếu cần

## 7. Bước tiếp theo

Tạo folder `thaifex-video`, đặt file này vào, mở folder đó trong Claude Code và nói **"bắt đầu"**.
