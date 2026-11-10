---
workflow: faceless-explainer
flow: automation
storyboard: yes
message: "4 chặng Chuẩn bị → Gửi hàng → Tại Bangkok → Kết thúc; dễ sai nhất là gửi hàng mẫu (nếu dùng công ty vận chuyển khác: khai báo hải quan F&B, xin giấy phép nhập khẩu trước 2 tuần)"
destination: youtube
aspect: 1920x1080
language: vi
audience: "Doanh nghiệp thực phẩm & đồ uống Việt Nam đang cân nhắc hoặc đã đăng ký trưng bày tại THAIFEX 2027"
length: 70s
angle: how-to
voice: vi-VN-HoaiMyNeural
style_preset: thaifex-journey
---

## Intent

Phần đầu (cảnh 1–5, ~70s) của video hướng dẫn "THAIFEX 2027: Những điểm công ty trưng bày cần lưu ý".
Kể theo hành trình 4 chặng; cảnh 5 (gửi hàng mẫu) là cảnh quan trọng nhất. Tông sáng, trung tính, không chói,
giọng điệu hướng dẫn thân thiện, đáng tin. Cảnh 6–9 làm sau, nối tiếp trong cùng project.
Nguồn: docs/YEU-CAU-VIDEO-THAIFEX-2026.md (mục 4, cảnh 1–5) và docs/script-v3.md (s1–s5).

## Assets

- Không có logo: dùng chữ "THAIFEX 2027" (biến, thay logo sau).
- Mọi hình là minh họa vẽ phẳng tự tạo (danh sách trong frame.md).

## Customizations

- Lồng tiếng: Edge TTS vi-VN-HoaiMyNeural (nữ, ấm, nhịp vừa), đọc nguyên văn script-v3.md s1–s5; chữ/hình xuất hiện theo mốc thời gian từng từ.
- Biến sửa được trong Studio (nhãn tiếng Việt): tên sự kiện, 4 tên chặng, 4 màu chặng, màu nền, tiêu đề cảnh, nhãn chip, chữ con dấu ("DỄ SAI NHẤT", "KHAI BÁO", "THÔNG QUAN", "TRƯỚC 2 TUẦN"), logo.
- Hiệu ứng âm thanh: whoosh khi chuyển cảnh, tiếng đóng dấu, tick, "ding".
- Thanh tiến trình 4 chặng ở cạnh dưới, sáng ở chặng đang nói.
- Nhạc nền: làm sau bằng motion-studio music.mjs (mood pulse), giảm khi có lời đọc.

## Notes

- KHÔNG bịa ngày, hạn chót, giá, số liệu. Chỉ dùng "tháng 5", "IMPACT, Bangkok", "2 tuần", "24/24".
- Không emoji, không nền tối (kể cả kết), không chữ chồng lên hình.
- Cảnh 3: không tự phân công loại gian hàng nào do ai dàn dựng.
- Cảnh 5: 2 điều (khai báo hải quan, giấy phép nhập khẩu) nằm dưới điều kiện "nếu dùng công ty vận chuyển khác".
- Nói chuyện với người dùng bằng tiếng Việt.
