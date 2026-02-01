Dưới đây là phiên bản **README.md hoàn chỉnh** đã được chỉnh sửa dựa trên nội dung bạn vừa cung cấp, với các thay đổi sau:

- **Bỏ hoàn toàn Docker** (xóa badge Docker, xóa phần Getting Started bằng Docker, xóa docker compose, xóa Dockerfile nếu có ngầm hiểu)
- Giữ nguyên cấu trúc thư mục bạn gửi (không thêm alembic/, tests/, .env.example…)
- Sửa phần cài đặt backend/frontend cho phù hợp hơn với nội dung bạn đưa (dùng `python app.py` thay uvicorn, dùng `npm` thay pnpm, thêm lệnh Windows activate)
- Xóa các phần không cần thiết hoặc lỗi nhỏ (ví dụ FLASK_ENV không phù hợp với FastAPI, port 9999 → giữ 8000 chuẩn FastAPI)
- Giữ nguyên ngôn ngữ, emoji, và phong cách bạn đã dùng

```markdown
# CollabSphere (COSRE)  
**Hệ thống hỗ trợ học tập theo phương pháp Project-Based Learning (PBL)**  
**A Unified Real-time Collaboration & Project Management Platform for Education**

<p align="center">
  <img src="https://via.placeholder.com/1200x400.png?text=CollabSphere+Banner" alt="CollabSphere Banner" width="800"/>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python 3.11"></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-0.115-success" alt="FastAPI"></a>
  <a href="https://reactjs.org/"><img src="https://img.shields.io/badge/React-18-blue" alt="React 18"></a>
</p>

**CollabSphere** là nền tảng **all-in-one** dành cho giáo dục, giúp sinh viên và giảng viên quản lý, thực hiện đồ án môn học theo phương pháp **Project-Based Learning (PBL)** mà không cần chuyển đổi liên tục giữa nhiều công cụ rời rạc (Zoom, Trello, Miro, Google Docs, Slack…).

Tất cả tính năng thiết yếu được tích hợp trong **một nơi duy nhất**, hỗ trợ làm việc nhóm thời gian thực.

## ✨ Tính năng nổi bật

- Video call + Screen sharing (WebRTC)
- Chat nhóm & chat trong phòng họp
- Bảng trắng (Whiteboard) cộng tác real-time
- Task board Kanban + Sprint + Subtask + Checkpoint
- Quản lý milestone, contribution tracking
- Đánh giá chéo (peer review) & feedback chi tiết từ giảng viên
- AI hỗ trợ gợi ý ý tưởng, tự động sinh milestone
- Import dữ liệu lớp học, sinh viên, môn học từ Excel
- Thông báo real-time (bell icon) & email
- Upload/download tài liệu nhóm & lớp

## 🎯 Các vai trò trong hệ thống

| Vai trò              | Mô tả chính                                      |
|----------------------|--------------------------------------------------|
| **Admin**            | Quản trị toàn hệ thống, cấu hình chung           |
| **Staff**            | Nhập dữ liệu môn học, lớp, tài khoản bằng Excel  |
| **Head Department**  | Duyệt đề tài, phân bổ đề tài cho lớp             |
| **Lecturer**         | Tạo đề tài, quản lý nhóm, chấm điểm, feedback    |
| **Student**          | Làm việc nhóm, cập nhật tiến độ, đánh giá chéo   |

## 🛠️ Tech Stack

### Backend
- Python 3.11 + **FastAPI**
- PostgreSQL (database)
- Redis (real-time, cache, pub/sub)
- SQLAlchemy + Alembic (ORM & migration)
- JWT + OAuth2 (authentication)

### Frontend
- React 18 + TypeScript
- Vite + TailwindCSS
- Zustand / TanStack Query (state & data fetching)
- Socket.IO client (real-time)
- WebRTC + simple-peer (video call & screen sharing)

### Real-time & Communication
- Socket.IO (chat, whiteboard, notification)
- WebRTC (peer-to-peer video)
- Optional: TURN/STUN server

### DevOps
- GitHub Actions (CI/CD)
- Nginx (serve frontend static files in production)

## 📂 Cấu trúc thư mục dự án

```
CollabSphere/
├── backend/                      # FastAPI backend (Clean Architecture)
│   ├── src/
│   │   ├── api/                  # HTTP layer
│   │   │   ├── controllers/      # Business logic handlers
│   │   │   ├── routes/           # APIRouter definitions
│   │   │   ├── schemas/          # Pydantic models (request/response)
│   │   │   ├── middleware.py
│   │   │   └── swagger.py
│   │   │
│   │   ├── domain/               # Core business logic (independent)
│   │   │   ├── models/           # Entities & Value Objects
│   │   │   ├── sinhvien/         # Domain modules
│   │   │   ├── taikhoan/
│   │   │   ├── constants.py
│   │   │   └── exceptions.py
│   │   │
│   │   ├── infrastructure/       # External integrations
│   │   │   ├── databases/        # DB session, connection
│   │   │   └── repositories/     # Data access (CRUD)
│   │   │
│   │   ├── services/             # Application services / use-cases
│   │   │
│   │   ├── main.py               # FastAPI app entry
│   │   ├── config.py
│   │   └── dependencies.py
│
├── frontend/                     # React + Vite + TypeScript
│   ├── public/
│   ├── src/
│   │   ├── assets/               # Static files (images, icons…)
│   │   ├── components/           # Reusable UI components
│   │   │   ├── common/           # Button, Input, Card, Modal…
│   │   │   └── layout/           # Header, Sidebar, Footer…
│   │   │
│   │   ├── pages/                # Main views / routes
│   │   ├── hooks/                # Custom React hooks
│   │   ├── stores/               # Zustand stores (nếu dùng)
│   │   ├── services/             # API client (axios/fetch)
│   │   ├── utils/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   
├── .github/workflows/            # CI/CD pipelines (optional)
├── .gitignore
└── README.md
```

## 🚀 Getting Started (Development mode)

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL (chạy local hoặc cloud như Supabase)
- Redis (chạy local hoặc cloud)

### Backend

```bash
cd backend

# Tạo và kích hoạt virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux/macOS:
# source venv/bin/activate

cd src
pip install -r ../requirements.txt

# Chạy ứng dụng (giả sử entry point là app.py hoặc main.py)
python app.py
```

→ API docs (Swagger): http://localhost:8000/docs (hoặc port bạn config trong app.py)

### Frontend

```bash
cd frontend

# Cài đặt dependencies
npm install

# Chạy dev server
npm run dev
```

→ Frontend chạy tại: http://localhost:5173

**Lưu ý**:  
- Cập nhật các biến môi trường trong file `.env` (hoặc `.env.local`) của backend, ví dụ:
  ```
  DATABASE_URL=postgresql://postgres:collabsphere25@db.bliuqusdfagtmniwhpsy.supabase.co:5432/postgres
  SECRET_KEY=dev_secret_key
  ```
- Đảm bảo backend đang chạy trước khi khởi động frontend.

## 📸 Demo & Screenshots

*(Thay placeholder bằng ảnh thật của dự án khi có)*

<p align="center">
  <img src="https://via.placeholder.com/800x450.png?text=Kanban+Board+Screenshot" alt="Kanban Board" width="600"/>
  <br/>
  <img src="https://via.placeholder.com/800x450.png?text=Real-time+Whiteboard" alt="Whiteboard" width="600"/>
</p>

## 🤝 Contributing

1. Fork dự án
2. Tạo branch feature: `git checkout -b feature/amazing-feature`
3. Commit thay đổi: `git commit -m 'Add some amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Mở Pull Request

## 📄 License

Distributed under the **MIT License**. Xem file [LICENSE](LICENSE) để biết chi tiết.

Cảm ơn bạn đã quan tâm đến **CollabSphere**!  
Hy vọng dự án sẽ hỗ trợ hiệu quả cho việc học tập theo dự án tại Việt Nam và quốc tế. 🌟
```
