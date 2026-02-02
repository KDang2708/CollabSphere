from fastapi import APIRouter, Depends

from api.controllers.Admin_controller import AdminController
from services.Doc_Bao_Cao import DocBaoCaoUseCase
from services.Phan_Hoi_Nguoi_Dung import PhanHoiUseCase
from api.schemas.responses.Bao_cao import BaoCaoResponse
from api.schemas.responses.Phan_Hoi import PhanHoiResponse
from api.schemas.requests.Phan_Hoi import PhanHoiRequest
from api.schemas.responses.Tai_Khoan import TaiKhoanResponse
from infrastructure.security.dependency import get_current_user
from api.schemas.requests.Huy_Kich_Hoat import HuyKichHoatRequest
from api.schemas.requests.Tai_Kich_Hoat import TaiKichHoatRequest
from services.Huy_Kich_Hoat import HuyKichHoatUseCase
from services.Tai_Kich_Hoat import TaiKichHoatUseCase
from services.Xem_Tai_Khoan import XemTaiKhoanUseCase
from services.Tim_Kiem_Tai_Khoan import TimKiemTaiKhoanUseCase

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_admin_controller():
    return AdminController(
        doc_bao_cao = DocBaoCaoUseCase(),
        phan_hoi = PhanHoiUseCase(),
        xem_tai_khoan = XemTaiKhoanUseCase() ,
        huy_kich_hoat = HuyKichHoatUseCase() , 
        tai_kich_hoat = TaiKichHoatUseCase() , 
        tim_kiem_tai_khoan = TimKiemTaiKhoanUseCase()
    )


@router.get("/doc_bao_cao", response_model = list[BaoCaoResponse] , status_code= 200 )
def doc_bao_cao(
    user = Depends(get_current_user),
    controller : AdminController = Depends(get_admin_controller)
):
    return controller.lay_danh_sach_bao_cao()

@router.put("/phan_hoi_nguoi_dung", response_model=PhanHoiResponse,status_code = 200)
def phan_hoi_nguoi_dung(
    phan_hoi : PhanHoiRequest,
    user = Depends(get_current_user), # tham số ko có giá trị mặc định đứng sau tham số có giá trị mặc định
    controller : AdminController = Depends(get_admin_controller)
):
    return controller.phan_hoi_nguoi_dung(phan_hoi)
@router.get("/xem_tai_khoan" , response_model=list[TaiKhoanResponse], status_code= 200)
def xem_tai_khoan(user = Depends(get_current_user) , controller : AdminController = Depends(get_admin_controller)):
    return controller.xem_tai_khoan()
@router.patch("/huy_kich_hoat", status_code=200)
def huy_kich_hoat( huy_kich_hoat : HuyKichHoatRequest , user = Depends(get_current_user) , controller : AdminController = Depends(get_admin_controller) ):
    return controller.huy_kich_hoat(huy_kich_hoat)
@router.patch("/tai_kich_hoat",status_code=200)
def tai_kich_hoat(tai_kich_hoat : TaiKichHoatRequest , user = Depends(get_current_user), controller : AdminController = Depends(get_admin_controller)):
    return controller.tai_kich_hoat(tai_kich_hoat)
