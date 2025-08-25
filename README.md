# CNPM
Dự án CNPM
dự án CNPM intern-management-system/

intern-management-system/

├── backend/                  # API services (Express/Django/etc.)

│   ├── src/

│   │   ├── controllers/

│   │   ├── models/

│   │   ├── routes/

│   │   ├── services/

│   │   └── utils/

│   ├── .env

│   ├── app.js

│   └── package.json / manage.py

│

├── frontend/                 # (Optional) Frontend app (React/Vue/etc.)

│   ├── public/

│   ├── src/

│   │   ├── components/

│   │   ├── pages/

│   │   ├── services/

│   │   └── App.js

│   └── package.json

│

├── diagrams/                # All system design diagrams

│   ├── context-diagram.drawio

│   ├── ims_erd.drawio

│   ├── use-case.drawio

│   └── *.png / *.svg

│

├── docs/                    # Technical documentation

│   ├── system-design.md

│   └── api-guide.md

│

├── openapi_spec.yaml        # OpenAPI / Swagger spec

├── README.md                # Project overview

└── LICENSE                  # License file (MIT/GPL/etc.)

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

1. Create virtualenv and install:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

2. Copy `.env.example` -> `.env` and set SECRET_KEY.

3. Initialize sample data (creates DB and sample users):

```bash
python -m app.sample_data
```

4. Run server:

```bash
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Notes
- Uses SQLite by default (`ims.db`).
- Token auth: use `/api/token` (form data: username, password) to get Bearer token.

