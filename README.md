# Motion Studio: các dự án video

Nơi chứa các dự án video làm bằng [HyperFrames](https://hyperframes.heygen.com) (HTML + GSAP) với skill Motion Studio: hoạt hình vẽ phẳng, lồng tiếng AI, render ra MP4.

## Danh sách dự án

| Dự án | Thư mục | Trạng thái | Mô tả |
|---|---|---|---|
| THAIFEX 2027 | [videos/thaifex-2027](videos/thaifex-2027/README.md) | Bản v5 (2:53) | Video hướng dẫn công ty trưng bày tại THAIFEX, 9 cảnh, giọng ElevenLabs HuyenTrang |
| fMA 3D Showroom | [videos/fma-3d-showroom](videos/fma-3d-showroom/README.md) | Kịch bản v2 | Video giới thiệu showroom 3D theo yêu cầu của furnitureMarket.Asia, 10 cảnh (~1:50) |

## Cấu trúc chung

```
Motion Studio/
├── README.md          ← file này: danh sách dự án
├── .env               ← API key dùng chung (ElevenLabs…), KHÔNG lên GitHub
└── videos/
    └── <ten-du-an>/   ← mỗi dự án một thư mục, tự chứa đủ mọi thứ
        ├── README.md          ← giới thiệu và cách làm việc với dự án
        ├── LOG-CHINH-SUA.xlsx ← nhật ký chỉnh sửa của dự án
        ├── docs/              ← yêu cầu, kịch bản, lời đọc, báo cáo
        ├── index.html, compositions/, assets/, tools/
        └── renders/           ← MP4 xuất ra (không lên GitHub)
```

## Bắt đầu dự án mới

1. Tạo thư mục `videos/<ten-du-an>` (chữ thường, không dấu, nối bằng gạch ngang).
2. Nhờ Claude dùng skill Motion Studio để dựng project: chọn phong cách, viết kịch bản, tạo giọng.
3. Tạo `README.md`, `LOG-CHINH-SUA.xlsx` và thư mục `docs/` trong dự án.
4. Thêm một dòng vào bảng **Danh sách dự án** ở trên.

## Quy ước

- Chỉ xuất dữ liệu ra Excel (`.xlsx`), không dùng CSV.
- Không bịa số liệu, ngày, giá: thiếu thông tin thì để trống.
- Mỗi lần chỉnh sửa ghi một dòng vào log của dự án.
- File MP4 trong `renders/` chỉ lưu trên máy, không đưa lên GitHub.
