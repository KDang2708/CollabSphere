from fastapi import FastAPI
from api.routes.Tai_Khoan_route import router
def register_routes(app: FastAPI):
    app.include_router(router)