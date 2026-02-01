from fastapi import FastAPI

from api.routes.Tai_Khoan_route import router as tai_khoan_router
from api.routes.Admin_route import router as admin_router


def register_routes(app: FastAPI):
    app.include_router(tai_khoan_router)
    app.include_router(admin_router)