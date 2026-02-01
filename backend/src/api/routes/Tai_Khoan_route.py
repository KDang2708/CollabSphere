from fastapi import APIRouter, Depends

from api.schemas.requests.Dang_Ki import DangKiRequest
from api.schemas.responses.Dang_Ki import DangKiResponse
from api.controllers.Tai_Khoan_controller import TaiKhoanController
from api.schemas.responses.Dang_Nhap import DangNhapResponse
from api.schemas.requests.Dang_Nhap import DangNhapRequset
from services.Dang_Ki import DangKiUseCase
from services.Dang_Nhap import DangNhapUseCase

router = APIRouter(prefix="/tai_khoan", tags=["TaiKhoan"])


def get_dang_ki_controller():
    service = DangKiUseCase()
    return TaiKhoanController(service)

def get_dang_nhap_controller():
    service = DangNhapUseCase()
    return TaiKhoanController(service)


@router.post("/dang_ki", response_model = DangKiResponse , status_code=201 )
def dang_ki(
    dang_ki : DangKiRequest, # ngầm đọc body và validate dữ liệu
    controller : TaiKhoanController = Depends(get_dang_ki_controller)
):
    return controller.dang_ki(dang_ki)
@router.get("/dang_nhap",response_model = DangNhapResponse , status_code= 200 )
def dang_nhap(
    dang_nhap : DangNhapRequset,
    controller : TaiKhoanController = Depends(get_dang_nhap_controller)
):
    return controller.dang_nhap(dang_nhap)