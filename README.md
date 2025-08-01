# CNPM
Dự án CNPM
dự án CNPM intern-management-system/

ims/
├── app.py
├── config.py
├── models.py
├── routes/
│   ├── auth.py
│   ├── interns.py
│   ├── hr.py
│   ├── mentors.py
│   └── coordinator.py
├── templates/
│   └── base.html
├── static/
│   └── style.css
└── requirements.txt

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

