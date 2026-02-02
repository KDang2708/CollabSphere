from fastapi import APIRouter , Depends

from api.controllers.Sinh_Vien_controller import SinhVienController
from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from infrastructure.security.dependency import get_current_user
from api.schemas.responses.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocResponse
from api.schemas.requests.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocRequest
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.responses.Xem_Nhom_SV import XemNhomSVResponse
from api.schemas.requests.Xem_Nhom_SV import XemNhomSVRequest
from services.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocUseCase
from api.schemas.responses.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocResponse
from api.schemas.requests.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocRequest
from services.Nop_Bai_Nop_Ket_Qua import NopBaiUseCase
from api.schemas.requests.Nop_Bai import NopBaiRequest
from services.Thuc_Hien_Kiem_Tra import ThucHienKiemTraUseCase
from api.schemas.responses.Thuc_Hien_Kiem_Tra import BaiKiemTraResponse
from api.schemas.requests.Thuc_Hien_Kiem_Tra import ThucHienKiemTraRequest
from services.Tao_Nhiem_Vu import TaoNhiemVuUseCase
from api.schemas.requests.Tao_Nhiem_Vu import TaoNhiemVuRequest
from services.Tro_Chuyen import TroChuyenLopUseCase
from api.schemas.responses.Xem_Tin_Lop import TinNhanResponse
from api.schemas.requests.Xem_Tin_Nhan_Lop import XemTinNhanLopRequest
from api.schemas.requests.Xem_Tin_Nhom import XemTinNhomRequest
from api.schemas.requests.Nhan_Tin import NhanTinRequest
from api.schemas.responses.Nhan_Tin import NhanTinResponse

router = APIRouter(prefix="/sinh_vien" , tags=["SinhVien"])

def get_sinh_vien_controller():
    return SinhVienController(
        xem_lop_hoc=XemLopHocUseCase(),
        xem_nhom=XemNhomUseCase(),
        xem_thong_tin_lop_hoc=XemThongTinLopHocUseCase(),
        nop_bai=NopBaiUseCase( ),
        thuc_hien_kiem_tra= ThucHienKiemTraUseCase(),
        tao_nhiem_vu=TaoNhiemVuUseCase(),
        tro_chuyen=TroChuyenLopUseCase(),
    )

@router.get("/xem_lop_hoc",response_model=list[XemLopHocResponse],status_code=200)
def xem_lop_hoc(
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_lop_hoc()
@router.get("/xem_chi_tiet_lop_hoc",response_model=XemChiTietLopHocResponse,status_code=200)
def xem_chi_tiet_lop_hoc(
    request : XemChiTietLopHocRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_chi_tiet_lop_hoc(request)
@router.get("/xem_nhom", response_model=XemNhomSVResponse , status_code=200)
def xem_nhom(
    request : XemNhomSVRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_nhom_sinh_vien(request)
@router.get("/xem_thong_tin_lop_hoc", response_model=XemThongTinLopHocResponse, status_code=200)
def xem_thong_tin_lop_hoc(
    request : XemThongTinLopHocRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.ser_xem_thong_tin_lop_hoc(request)
@router.post("/nop_bai",status_code=201)
def nop_bai(
    request : NopBaiRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
): 
    return controller.nop_bai_lam(request)
@router.get("/thuc_hien_kiem_tra",response_model=list[BaiKiemTraResponse],status_code=200)
def thuc_hien_kiem_tra(
    request : ThucHienKiemTraRequest,
    user =Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.thuc_hien_kiem_tra(request)
@router.post("/tao_nhiem_vu", status_code=201)
def tao_nhiem_vu(
    request : TaoNhiemVuRequest,
    user = Depends(get_current_user),
    controller : SinhVienController=Depends(get_sinh_vien_controller)
):
    return controller.tao_nhiem_vu(request)
@router.get("/xem_tin_lop",response_model=list[TinNhanResponse],status_code=200)
def xem_tin_lop(
    request : XemTinNhanLopRequest,
    user =Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_tin_nhan_lop(request)
@router.get("/xem_tin_nhom",response_model=list[TinNhanResponse],status_code=200)
def xem_tin_nhom(
    request : XemTinNhomRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.xem_tin_nhom(request)
@router.post("/nhan_tin",response_model=NhanTinResponse , status_code=201)
def nhan_tin(
    request : NhanTinRequest,
    user = Depends(get_current_user),
    controller : SinhVienController = Depends(get_sinh_vien_controller)
):
    return controller.nhan_tin(request)