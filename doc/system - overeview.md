migrations
scripts
├── run_postgres.sh

src
├── api
│   ├── controllers                # Controllers cho API (HR, Admin, Coordinator, Mentor, Intern)
│   ├── schemas                     # Marshmallow schemas
│   ├── middleware.py
│   ├── responses.py
│   ├── requests.py
│
├── infrastructure
│   ├── services                    # Services dùng thư viện bên thứ ba (email, SMS, analytics)
│   │   └── ...
│   ├── databases                   # Kết nối và khởi tạo database
│   │   └── ...
│   ├── repositories                # Repository tương tác với DB
│   │   └── ...
│   ├── models                      # Database models
│       └── ...
│
├── domain
│   ├── constants.py                 # Các hằng số hệ thống (roles, status codes)
│   ├── exceptions.py                # Ngoại lệ cho business logic
│   ├── models                       # Business logic models (HR, Admin, Intern, Training, KPI)
│   │   └── ...
│   ├── services                     # Business services (quản lý tuyển dụng, lịch phỏng vấn, chấm điểm)
│       └── ...
│
├── app.py
├── config.py
├── cors.py
├── create_app.py
├── dependency_container.py
├── error_handler.py

