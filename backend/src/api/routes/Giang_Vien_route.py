from fastapi import APIRouter , Depends

from infrastructure.security.dependency import get_current_user
from api.controllers.Giang_Vien_controller import GiangVienController
from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from api.schemas.responses.Tao_Nhom import TaoNhomResponse
from api.schemas.requests.Tao_Nhom import TaoNhomRequest
from services.Phan_Nhom import PhanNhomUseCase
from api.schemas.requests.Them_Sinh_Vien_Nhom import ThemSinhVienNhomRequest
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.responses.Xem_Nhom import XemNhomResponse
from api.schemas.requests.Xem_Nhom import XemNhomRequest
from services.Tao_Du_An import TaoDuAnUseCase
from api.schemas.requests.Tao_Du_An import TaoDuAnRequest
from api.schemas.responses.Tao_Du_An import TaoDuAnRespone
from services.Giao_Du_An import GiaoDuAnUseCase
from api.schemas.requests.Giao_Du_An import GiaoDuAnRequest
from api.schemas.responses.Xem_Du_An import XemDuAnResponse
from services.Xem_Du_An import XemDuAnUseCase
from api.schemas.requests.Nhan_Xet import NhanXetRequest
from services.Nhan_Xet import NhanXetUseCase
from services.Tao_Bai_Kiem_Tra import TaoBaiKiemTraUseCase
from api.schemas.requests.Tao_Bai_Kiem_Tra import TaoBaiKiemTraRequest
from services.Tao_Moc_Quan_Trong import TaoMocQuanTrongUseCase
from api.schemas.requests.Tao_Moc_Quan_Trong import TaoMocQuanTrongRequest
from services.Tao_Nhiem_Vu import TaoNhiemVuUseCase
from api.schemas.requests.Tao_Nhiem_Vu import TaoNhiemVuRequest
from services.Tro_Chuyen import TroChuyenLopUseCase
from api.schemas.responses.Xem_Tin_Lop import TinNhanResponse
from api.schemas.requests.Xem_Tin_Nhan_Lop import XemTinNhanLopRequest
from api.schemas.requests.Nhan_Tin import NhanTinRequest
from api.schemas.responses.Nhan_Tin import NhanTinResponse

router = APIRouter(prefix="/giang_vien",tags=["GiangVien"])

def get_giang_vien_controller():
    return GiangVienController(
        xem_lop_hoc = XemLopHocUseCase(),
        phan_nhom= PhanNhomUseCase(),
        xem_nhom= XemNhomUseCase(),
        tao_du_an=TaoDuAnUseCase(),
        giao_du_an=GiaoDuAnUseCase(),
        xem_du_an= XemDuAnUseCase(),
        nhan_xet=NhanXetUseCase(),
        tao_bai_kiem_tra= TaoBaiKiemTraUseCase(),
        tao_moc_quan_trong=TaoMocQuanTrongUseCase(),
        tao_nhiem_vu=TaoNhiemVuUseCase(),
        tro_chuyen=TroChuyenLopUseCase(),
    )

@router.get("/xem_lop_hoc", response_model=list[XemLopHocResponse],status_code=200)
def xem_lop_hoc(
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.xem_lop_hoc()
@router.put("/tao_nhom",response_model=TaoNhomResponse , status_code=201)
def tao_nhom(
    request = TaoNhomRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.tao_nhom(request)
@router.put("/them_sinh_vien_nhom",status_code=200)
def them_sinh_vien_nhom(
    request : ThemSinhVienNhomRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.them_sinh_vien_vao_nhom(request)
@router.get("/xem_nhom",response_model=XemNhomResponse,status_code=200)
def xem_nhom(
    request : XemNhomRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.xem_nhom(request)
@router.put("/tao_du_an", response_model=TaoDuAnRespone , status_code=201)
def tao_du_an(
    request : TaoDuAnRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.tao_du_an(request)
@router.put("/giao_du_an",status_code=200)
def giao_du_an(
    request : GiaoDuAnRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.giao_du_an(request)
@router.get("/xem_du_an",response_model=list[XemDuAnResponse],status_code=200)
def xem_du_an(
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.xem_du_an()
@router.post("/nhan_xet",status_code=201)
def nhan_xet(
    request : NhanXetRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.nhan_xet(request)
@router.post("/tao_bai_kiem_tra", status_code=201)
def tao_bai_kiem_tra(
    request : TaoBaiKiemTraRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.tao_bai_kiem_tra(request)
@router.post("/tao_moc_quan_trong",status_code=201)
def tao_moc_quan_trong(
    request : TaoMocQuanTrongRequest , 
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.tao_moc_quan_trong(request)
@router.post("/tao_nhiem_vu",status_code=201)
def tao_nhiem_vu(
    request : TaoNhiemVuRequest,
    user = Depends(get_current_user),
    controller : GiangVienController=Depends(get_giang_vien_controller)
):
    return controller.tao_nhiem_vu(request)
@router.get("/xem_tin_lop",response_model=list[TinNhanResponse],status_code=200)
def xem_tin_lop(
    request : XemTinNhanLopRequest,
    user =Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.xem_tin_nhan_lop(request)
@router.post("/nhan_tin",response_model=NhanTinResponse , status_code=201)
def nhan_tin(
    request : NhanTinRequest,
    user = Depends(get_current_user),
    controller : GiangVienController = Depends(get_giang_vien_controller)
):
    return controller.nhan_tin(request)
    
#     from api.schemas.requests.Nhan_Tin import NhanTinRequest
# from api.schemas.responses.Nhan_Tin import NhanTinResponse