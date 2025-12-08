# CollabSphere (COSRE)  
**Hệ thống hỗ trợ học tập theo phương pháp Project-Based Learning (PBL)**  
**A Unified Real-time Collaboration & Project Management Platform for Education**

<img src="https://via.placeholder.com/1200x400.png?text=CollabSphere+Banner" alt="CollabSphere Banner" />

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-success)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-blue)](https://reactjs.org)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://docker.com)

## Giới thiệu dự án
CollabSphere là hệ thống **all-in-one** giúp sinh viên và giảng viên quản lý, thực hiện đồ án môn học theo phương pháp **Project-Based Learning** mà không cần chuyển qua lại giữa nhiều công cụ rời rạc (Zoom, Trello, Miro, Google Docs, Slack…).

Tất cả trong một nơi:
- Video call + Screen sharing  
- Chat nhóm & chat trong meeting  
- Bảng trắng (Whiteboard) cộng tác real-time  
- Task board (Kanban) + Sprint + Subtask  
- Quản lý milestone & checkpoint  
- Đánh giá chéo (peer review) & góp ý từ giảng viên  
- AI hỗ trợ gợi ý ý tưởng & sinh milestone  
- Import Excel tự động (lớp, sinh viên, môn học…)

## Các vai trò trong hệ thống
| Vai trò            | Mô tả ngắn gọn                              |
|--------------------|---------------------------------------------|
| **Admin**          | Quản trị toàn hệ thống                      |
| **Staff**          | Nhập dữ liệu (môn, lớp, tài khoản) bằng Excel |
| **Head Department**| Duyệt đề tài, phân bổ đề tài cho lớp        |
| **Lecturer**       | Tạo đề tài, quản lý nhóm, chấm điểm         |
| **Student**        | Làm việc nhóm, cập nhật tiến độ, đánh giá chéo |

## Tính năng chính
| Module                              | Tính năng nổi bật                                                                 |
|-------------------------------------|------------------------------------------------------------------------------------|
| Subject & Class Management          | Import Excel → tự động tạo môn, lớp, tài khoản                                    |
| Project Management                  | Tạo đề tài + AI sinh milestone tự động + duyệt đề tài                             |
| Teams & Workspace                   | Kanban board, sprint, subtask, checkpoint, contribution tracking                 |
| Real-time Communication            | Video call (WebRTC), chat nhóm, lịch họp, thông báo real-time                     |
| Collaborative Tools                 | Whiteboard, đồng thời chỉnh sửa tài liệu                                         |
| Resource Management                 | Upload/download tài liệu lớp và nhóm                                              |
| Evaluation & Feedback               | Đánh giá nhóm/cá nhân, peer review, góp ý chi tiết                               |
| AI-Powered Assistant                | Chatbot hỗ trợ ý tưởng, sinh thông tin đề tài                                     |
| Notification System                 | Email + real-time notification (bell icon)                                        |

## Tech Stack

### Backend
- Python 3.11 + FastAPI
- PostgreSQL
- Redis (real-time)
- JWT + OAuth2
- SQLAlchemy + Alembic

### Frontend
- React 18 + TypeScript
- Vite + TailwindCSS
- Zustand / TanStack Query
- Socket.IO client
- WebRTC (peer-to-peer)

### Real-time & Communication
- Socket.IO (whiteboard, chat, notification)
- WebRTC + simple-peer (video call)
- Signal master (TURN/STUN server - optional)

### DevOps & Deployment
- Docker + Docker Compose
- GitHub Actions (CI/CD)
- Nginx (frontend static)

## Cấu trúc thư mục