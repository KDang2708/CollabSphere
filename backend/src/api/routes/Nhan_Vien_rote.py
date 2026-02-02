from fastapi import APIRouter , Depends

from api.controllers.Nhan_Vien_controller import NhanVienController
from services.Tao_Mon_Hoc import TaoMonHocUseCase
from services.Xem_Mon_Hoc import XemMonHocUseCase
from api.schemas.responses.Mon_Hoc import MonHocResponse
from api.schemas.requests.Tao_Mon_Hoc import TaoMonHocRequest
from infrastructure.security.dependency import get_current_user
from services.Tao_Lop_Hoc import TaoLopHocUseCase
from api.schemas.requests.Tao_Lop_hoc import TaoLopHocRequest
from api.schemas.responses.Tao_Lop_Hoc import TaoLopHocResponse
from services.Phan_Cong_Lop_Hoc import PhanCongLopHocUseCase
from api.schemas.requests.Phan_Cong_Lop_Hoc import PhanCongLopHocRequest
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse

router = APIRouter(prefix="/nhan_vien",tags=["NhanVien"])

def get_nhan_vien_controller():
    return NhanVienController(
        tao_mon_hoc = TaoMonHocUseCase(),
        xem_mon_hoc= XemMonHocUseCase(),
        tao_lop_hoc= TaoLopHocUseCase(),
        phan_cong_lop_hoc= PhanCongLopHocUseCase()
    )

@router.put("/tao_mon_hoc",response_model = MonHocResponse , status_code=201)
def tao_mon_hoc(
    request : TaoMonHocRequest,
    user = Depends(get_current_user),
    controller : NhanVienController = Depends(get_nhan_vien_controller)
):
    return controller.tao_mon_hoc(request)
@router.get("/xem_mon_hoc", response_model= MonHocResponse,status_code=200 )
def xem_mon_hoc(
    user = Depends(get_current_user),
    controller : NhanVienController = Depends(get_nhan_vien_controller)
):
    return controller.xem_mon_hoc()
@router.put("/tao_lop_hoc",response_model= TaoLopHocResponse, status_code=201)
def tao_lop_hoc(
    request : TaoLopHocRequest,
    user = Depends(get_current_user),
    controller : NhanVienController = Depends(get_nhan_vien_controller)
):
    return controller.tao_lop_hoc(request)
@router.post("/phan_cong_lop_hoc",status_code=200)
def phan_cong_lop_hoc(
    request : PhanCongLopHocRequest,
    user = Depends(get_current_user),
    controller : NhanVienController = Depends(get_nhan_vien_controller)
):
    return controller.phan_cong_lop_hoc(request)
@router.get("/xem_lop_hoc",response_model=list[XemLopHocResponse],status_code=200)
def xem_lop_hoc(
    user = Depends(get_current_user),
    controller : NhanVienController = Depends(get_nhan_vien_controller)
):
    return controller.xem_lop_hoc()