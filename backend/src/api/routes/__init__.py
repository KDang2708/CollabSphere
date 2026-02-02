from fastapi import FastAPI
from api.routes.Tai_Khoan_route import router
from api.routes.Admin_route import router as admin_router
from api.routes.Nhan_Vien_route import router as nhan_vien_router
from api.routes.Giang_Vien_route import router as giang_vien_router
from api.routes.Sinh_Vien_route import router as sinh_vien_router
from api.routes.Truong_Khoa_route import router as truong_khoa_router

def register_routes(app: FastAPI):
    app.include_router(router)
    app.include_router(admin_router)
    app.include_router(nhan_vien_router)
    app.include_router(giang_vien_router)
    app.include_router(sinh_vien_router)
    app.include_router(truong_khoa_router)