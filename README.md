# CNPM
Dự án CNPM
dự án CNPM intern-management-system/

intern-management-system/

├── app/                       # Source code chính

│   ├── api/

│   │   ├── routers/           # Routers cho từng actor

│   │   │   ├── auth.py

│   │   │   ├── hr.py

│   │   │   ├── coordinator.py

│   │   │   ├── mentor.py

│   │   │   ├── intern.py

│   │   │   ├── admin.py

│   │   │   └── dashboard.py

│   │   └── dependencies/      # Hàm phụ trợ (auth, role-based access…)

│   │       └── deps.py

│   │

│   ├── core/                  # Cấu hình cốt lõi

│   │   ├── config.py          # Config hệ thống

│   │   ├── security.py        # JWT, password hashing

│   │   └── logging.py         # Logging setup

│   │

│   ├── db/                    # Tầng kết nối CSDL

│   │   ├── base.py

│   │   └── session.py

│   │

│   ├── models/                # Database models

│   │   ├── user.py

│   │   ├── recruitment.py

│   │   ├── training.py

│   │   ├── ops.py

│   │   └── settings.py

│   │

│   ├── schemas/               # Pydantic schemas

│   │   ├── auth.py

│   │   ├── user.py

│   │   ├── recruitment.py

│   │   ├── training.py

│   │   ├── ops.py

│   │   └── settings.py

│   │

│   ├── repositories/          # CRUD logic

│   │   ├── user_repo.py

│   │   ├── campaign_repo.py

│   │   ├── job_repo.py

│   │   ├── application_repo.py

│   │   ├── interview_repo.py

│   │   ├── program_repo.py

│   │   ├── course_repo.py

│   │   ├── enrollment_repo.py

│   │   ├── daily_log_repo.py

│   │   ├── kpi_repo.py

│   │   ├── assessment_repo.py

│   │   ├── feedback_repo.py

│   │   ├── message_repo.py

│   │   └── setting_repo.py

│   │

│   ├── services/              # Business logic

│   │   ├── auth_service.py

│   │   ├── recruitment_service.py

│   │   ├── training_service.py

│   │   ├── ops_service.py

│   │   └── admin_service.py

│   │

│   ├── middleware/            # Middleware

│   │   └── logging.py

│   │

│   └── tests/                 # Unit test & integration test

│

├── main.py                    # Entry point FastAPI

├── requirements.txt           # Dependencies

├── README.md                  # Project overview



---

##  Mục tiêu

Hệ thống giúp doanh nghiệp quản lý toàn diện thực tập sinh:
- Quản lý chiến dịch tuyển dụng và phỏng vấn
- Xây dựng chương trình đào tạo
- Theo dõi tiến độ và đánh giá năng lực
- Giao tiếp mentor ↔ intern hiệu quả

---

# IMS API (FastAPI) - Complete

## Quick start





