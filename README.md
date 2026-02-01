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
  <a href="https://docker.com"><img src="https://img.shields.io/badge/Docker-Ready-blue" alt="Docker Ready"></a>
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

## 🚀 Getting Started (Docker – cách nhanh nhất)

Yêu cầu: Docker & Docker Compose

```bash
git clone https://github.com/your-username/CollabSphere.git
cd CollabSphere

# Sao chép file môi trường
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Chỉnh sửa các biến cần thiết trong .env (DATABASE_URL, JWT_SECRET_KEY, REDIS_URL…)
FLASK_ENV=development
POSTGRES_DATABASE_URL=postgresql://postgres:collabsphere25@db.bliuqusdfagtmniwhpsy.supabase.co:5432/postgres
SECRET_KEY=dev_secret_key


# Khởi động toàn bộ hệ thống
docker compose up -d --build
```

Truy cập:
- Frontend: http://localhost:5173 (hoặc port bạn config)
- API docs (Swagger): http://localhost:9999/docs

## 🛠️ Cài đặt môi trường phát triển (Development)

### Backend

```bash
cd backend

python -m venv venv
Windows: .venv\Scripts\Activate.ps1

cd backend\src\
pip install -r requirements.txt
python app.py

```

### Frontend

```bash
cd frontend

npm install    

npm run dev       
```

Frontend mặc định chạy tại: http://localhost:5173

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

**Hướng dẫn sử dụng file này:**
- Thay `your-username/CollabSphere` bằng tên repo GitHub thật của bạn.
- Thêm ảnh chụp màn hình thực tế thay cho placeholder.
- Nếu bạn đã đổi tên thư mục backend từ `temp-clean-arch` thành `backend`, thì cấu trúc trên đã khớp.
- Nếu có thêm live demo (Vercel, Render, Railway…), hãy thêm link ở đầu file.
