"""
Ứng dụng FastAPI - khởi động với: python app.py hoặc uvicorn app:app --reload
"""
from contextlib import asynccontextmanager
import os

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import register_routes


def _import_orm_models():
    """Import tất cả ORM models để Base.metadata có đủ bảng trước khi create_all."""
    from infrastructure import models  # noqa: F401
    models.import_all_models()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Khởi tạo DB khi start (nếu có cấu hình)."""
    _import_orm_models()
    try:
        from infrastructure.databases.factory_database import FactoryDatabase
        db = FactoryDatabase.get_database("POSTGRES")
        db.init_database(app)
    except Exception as e:
        print(f"[Warning] Không khởi tạo DB (kiểm tra .env POSTGRES_DATABASE_URL): {e}")
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="API",
        description="API quản lý",
        version="1.0.0",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_routes(app)

    @app.get("/")
    def root():
        return {"message": "API đang chạy", "docs": "/docs"}

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    import socket

    host = "0.0.0.0"
    port = 8888
    
    # Lấy địa chỉ IP thật của máy trong mạng nội bộ (optional)
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = "127.0.0.1"

    print("\n" + "="*50)
    print(f"🚀 API đang khởi động!")
    print(f"🔗 Truy cập tại local: http://127.0.0.1:{port}")
    print(f"🔗 Truy cập tại docs:  http://127.0.0.1:{port}/docs")
    print(f"🌐 Truy cập qua mạng:  http://{local_ip}:{port}")
    print("="*50 + "\n")

    uvicorn.run(
        "app:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )
