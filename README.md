# CNPM
Dự án CNPM
dự án CNPM intern-management-system/

├── app/

│  ├── pycache/ # Cache tạm của Python

│  ├── api/ # Route và controller xử lý yêu cầu HTTP

│  ├── models/ # Định nghĩa schema & ORM (SQLAlchemy, v.v.)

│  ├── repositories/ # Tầng truy xuất dữ liệu

│  ├── schemas/ # Pydantic schemas / DTOs (request & response)

│  ├── services/ # Logic xử lý nghiệp vụ

│  └── init.py # Khởi tạo app module

├── tests/ # Unit test cho các chức năng chính

├── config.py # Thiết lập cấu hình hệ thống

├── run.py # Entry point để khởi chạy Flask app

├── requirements.txt # Danh sách thư viện Python cần cài

└── README.md # Tài liệu hướng dẫn dự án

---

##  Mục tiêu

Hệ thống giúp doanh nghiệp quản lý toàn diện thực tập sinh:
- Quản lý chiến dịch tuyển dụng và phỏng vấn
- Xây dựng chương trình đào tạo
- Theo dõi tiến độ và đánh giá năng lực
- Giao tiếp mentor ↔ intern hiệu quả

---

##  Khởi chạy dự án

```bash
# 1. Cài đặt thư viện cần thiết
pip install -r requirements.txt

# 2. Chạy ứng dụng Flask
python run.py

