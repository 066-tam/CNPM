Intern Management System (IMS) – Tài liệu tổng quan hệ thống
1. Giới thiệu
Intern Management System (IMS) là một nền tảng quản lý thực tập sinh được triển khai trên nền tảng điện toán đám mây. Hệ thống giúp doanh nghiệp tối ưu hóa toàn bộ vòng đời của chương trình thực tập, từ tuyển dụng đến đào tạo, giám sát và đánh giá hiệu quả.
________________________________________
2. Đối tượng sử dụng (Actors)
Actor	Mô tả ngắn
HR Managers	Quản lý tuyển dụng và hồ sơ thực tập sinh
Internship Coordinators	Lên lịch phỏng vấn, thiết lập chương trình đào tạo
Mentors	Theo dõi và đánh giá tiến trình thực tập sinh
Interns	Sử dụng dashboard cá nhân, phản hồi chương trình
Admin	Quản trị hệ thống, cấu hình, hỗ trợ kỹ thuật
________________________________________
3. Chức năng theo từng vai trò
HR Managers
•	Recruitment Management
Tạo, quản lý các chiến dịch tuyển thực tập sinh; thu thập hồ sơ và xử lý ứng viên.
•	Intern Profile Management
Lưu trữ và quản lý thông tin cá nhân, học vấn, kinh nghiệm làm việc của thực tập sinh. Có khả năng tìm kiếm nâng cao.
•	Reporting and Analytics
Tự động tạo báo cáo theo kỳ, đánh giá hiệu quả chương trình thực tập dựa trên dữ liệu thực tế. Gợi ý cải thiện quy trình.
________________________________________
Internship Coordinators
•	Interview Scheduling
Hệ thống tự động gửi lịch phỏng vấn qua email/SMS cho ứng viên và người phỏng vấn.
•	Training Program Setup
Xây dựng nội dung đào tạo phù hợp với từng kỹ năng cần phát triển.
•	Performance Tracking
Theo dõi tiến độ của từng intern theo KPI định sẵn và các đợt đánh giá định kỳ.
________________________________________
Mentors
•	Daily Progress Monitoring
Ghi nhận hoạt động hằng ngày của intern và đưa ra nhận xét trực tiếp.
•	Skill Assessment
Đánh giá định kỳ về kỹ năng, năng lực, khả năng cải thiện của intern.
•	Communication Tools
Tích hợp hệ thống nhắn tin trực tiếp để mentor hỗ trợ intern kịp thời.
________________________________________
Interns
•	Personal Dashboard
Xem lịch trình, nhiệm vụ, tài liệu học tập và nhận phản hồi từ mentor.
•	Feedback Submission
Gửi nhận xét về chất lượng đào tạo và mentor, giúp hệ thống cải tiến liên tục.
•	Skill Development Tracking
Theo dõi tiến độ phát triển kỹ năng của bản thân. Nhận gợi ý cải thiện dựa trên dữ liệu hiệu suất.
________________________________________
Admin
•	System Configuration and Maintenance
Cài đặt hệ thống, phân quyền truy cập, kiểm soát bảo mật.
•	Technical Support
Hỗ trợ người dùng xử lý lỗi kỹ thuật, đảm bảo hệ thống vận hành liên tục.
________________________________________
4. Kiến trúc đề xuất (gợi ý)
•	Backend: Flask (Python) – Clean Architecture
•	Frontend: React.js / Tailwind CSS
•	Database: PostgreSQL / MongoDB
•	Authentication: JWT + Role-Based Access
•	CI/CD: GitHub Actions / Render / Railway
________________________________________
5. Lợi ích mang lại
•	Tự động hóa toàn bộ quy trình thực tập
•	Nâng cao trải nghiệm và hiệu suất của thực tập sinh
•	Giúp HR và mentor tiết kiệm thời gian quản lý
•	Báo cáo rõ ràng, phân tích hiệu quả chương trình dễ dàng
________________________________________
Tài liệu liên quan (gợi ý tạo thêm)
•	api-design.md: Thiết kế REST API
•	database-schema.md: Cấu trúc cơ sở dữ liệu
•	user-role-mapping.md: Phân quyền người dùng
•	use-cases.md: Các tình huống sử dụng cụ thể

