# Video THAIFEX 2027 – Báo cáo tóm tắt cách thực hiện

09/11/2026 · Andrew

## Tổng quan

Video hướng dẫn "THAIFEX 2027: Những điểm công ty trưng bày cần lưu ý" đã hoàn thành bản nháp đủ 9 cảnh, dài 2 phút 47 giây, khung 1920x1080 cho YouTube.

- **Người xem:** doanh nghiệp thực phẩm & đồ uống Việt Nam đang cân nhắc hoặc đã đăng ký trưng bày tại THAIFEX.
- **Cách kể:** một hành trình 4 chặng — Chuẩn bị → Gửi hàng → Tại Bangkok → Kết thúc.
- **Phong cách:** hình minh họa phẳng tông sáng, kết hợp ảnh gian hàng thật; giọng đọc nữ tiếng Việt; chữ và hình xuất hiện đúng lúc giọng đọc nhắc tới.
- **Cách làm:** toàn bộ video được dựng bằng máy (trợ lý AI + công cụ dựng video bằng code), không quay phim, không dựng tay trên phần mềm biên tập.
- **Nơi lưu:** mã nguồn dự án trên GitHub [andrewtdo74-cyber/Motion-Studio-video](https://github.com/andrewtdo74-cyber/Motion-Studio-video); file video mp4 lưu trên máy, gửi riêng.

## Quy trình thực hiện

Dự án đi qua 5 bước; mỗi bước đều có người duyệt trước khi sang bước sau.

1. **Lên yêu cầu và kịch bản.** Tóm tài liệu "Thông tin & kế hoạch trưng bày" thành file yêu cầu, rồi viết kịch bản phân cảnh và lời đọc theo hành trình 4 chặng. Chỉ dùng thông tin có trong tài liệu, không tự thêm ngày, giá hay số liệu.
2. **Chuẩn bị hình ảnh và nội dung.** Hình minh họa được vẽ bằng code theo bộ màu 4 chặng; ảnh gian hàng thật lấy từ mẫu đơn đăng ký TAA27 (trang 5); nội dung từng loại gian hàng lấy từ bảng tiện ích trong cùng tài liệu và bổ sung của người phụ trách.
3. **Tạo giọng đọc.** Lời đọc được chuyển thành giọng nói tự động (giọng nữ HoaiMy). Công cụ trả về mốc thời gian của từng từ để chữ và hình xuất hiện đúng lúc.
4. **Dựng cảnh và hiệu ứng.** Mỗi cảnh là một trang thiết kế riêng; chuyển động, hiệu ứng âm thanh (whoosh, tick, đóng dấu) và nhạc nền được gắn theo mốc thời gian lời đọc.
5. **Kiểm tra, xuất video và chỉnh sửa.** Công cụ tự kiểm tra lỗi bố cục, độ tương phản chữ, rồi xuất file mp4. Người phụ trách xem video, gửi góp ý (kèm ảnh chụp màn hình), và vòng sửa – xuất lại lặp lại đến khi đạt.

## Nội dung video

Video gồm 9 cảnh nối tiếp nhau; thanh tiến trình 4 chặng ở cạnh dưới sáng lên theo chặng đang nói.

| Cảnh | Thời điểm | Nội dung chính |
| --- | --- | --- |
| 1. Mở đầu | 0:00 | Câu hỏi "Quý vị đang quan tâm trưng bày tại THAIFEX 2027?", ảnh gian hàng Quốc gia Việt Nam, bảng "Lưu ý" 4 dòng |
| 2. Bốn chặng | 0:08 | Giới thiệu hành trình từ đăng ký đến tháo dỡ |
| 3. Chọn loại gian hàng | 0:15 | 3 loại gian hàng (Quốc gia Việt Nam, tiêu chuẩn, gian thô), đặc điểm từng loại, dịch vụ thuê thêm |
| 4. Hồ sơ & ngân sách | 1:19 | Hồ sơ đăng ký, bảng tính ngân sách, hướng dẫn thanh toán |
| 5. Gửi hàng mẫu | 1:27 | Chỗ dễ sai nhất: hạn chót, khai báo hải quan, giấy phép nhập khẩu trước 2 tuần |
| 6. Đến Bangkok | 1:51 | Vé, khách sạn, bảo hiểm; thuê xe van cho nhóm từ 4 người; chuyển khoản và tiền mặt bạt Thái |
| 7. Khách mua hàng | 2:17 | 3 nguồn khách: Ban tổ chức, chương trình AFW – Công ty Phương Bắc, đối tác tự mời |
| 8. Kết thúc hội chợ | 2:26 | Nhận thế nào, trả đúng như thế; poster, hình dán để lại cho Ban tổ chức |
| 9. Kêu gọi | 2:37 | Quét mã QR nhận bộ tài liệu; hẹn gặp tại THAIFEX 2027 |

## Công cụ sử dụng

Tất cả công cụ đều miễn phí hoặc mã nguồn mở, chạy trên máy tính cá nhân.

| Công cụ | Dùng để |
| --- | --- |
| Claude (trợ lý AI) | Đọc tài liệu, viết kịch bản, dựng cảnh, sửa theo góp ý |
| HyperFrames | Dựng video từ các trang thiết kế, kiểm tra lỗi, xuất mp4 |
| Edge TTS | Tạo giọng đọc tiếng Việt kèm mốc thời gian từng từ |
| FFmpeg | Cắt ghép âm thanh, nối nhạc nền, chụp khung hình để kiểm tra |
| GitHub | Lưu trữ và quản lý phiên bản dự án |

## Lưu ý và việc còn lại

Bản hiện tại là bản nháp; còn 4 việc cần bổ sung trước khi phát hành.

- [ ] Thay ô giữ chỗ "MÃ QR" ở cảnh 9 bằng mã QR / link form thật
- [ ] Bổ sung hotline/email và logo đơn vị tổ chức
- [ ] Xác nhận tháng diễn ra THAIFEX 2027 (cảnh 1 đang ghi "Tháng 5" theo kỳ 2026)
- [ ] Nghe duyệt toàn bộ giọng đọc và hiệu ứng âm thanh

Kinh nghiệm rút ra:

- **Mọi thông tin trên video phải có nguồn.** Chỉ đưa lên những gì có trong tài liệu chính thức hoặc người phụ trách xác nhận.
- **Sửa nội dung rất nhanh.** Đổi chữ, đổi năm, thêm đoạn mới chỉ mất vài phút sửa và khoảng 5–7 phút xuất lại video.
- **Góp ý bằng ảnh chụp màn hình** kèm thời điểm (ví dụ "giây 24") giúp sửa đúng chỗ ngay lần đầu.
- **Ảnh lấy từ PDF có độ phân giải thấp** (khoảng 350px); nên xin ảnh gốc nét hơn cho bản cuối.
