from fastapi import HTTPException , status

from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from services.Phan_Nhom import PhanNhomUseCase
from api.schemas.requests.Tao_Nhom import TaoNhomRequest
from api.schemas.responses.Tao_Nhom import TaoNhomResponse
from api.schemas.requests.Them_Sinh_Vien_Nhom import ThemSinhVienNhomRequest
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.requests.Xem_Nhom import XemNhomRequest
from api.schemas.responses.Xem_Nhom import XemNhomResponse , SinhVien
from api.schemas.requests.Tao_Du_An import TaoDuAnRequest
from api.schemas.responses.Tao_Du_An import TaoDuAnRespone
from services.Tao_Du_An import TaoDuAnUseCase
from services.Giao_Du_An import GiaoDuAnUseCase
from api.schemas.requests.Giao_Du_An import GiaoDuAnRequest
from services.Giao_Du_An import GiaoDuAnUseCase
from services.Xem_Du_An import XemDuAnUseCase
from api.schemas.responses.Xem_Du_An import XemDuAnResponse
from api.schemas.requests.Nhan_Xet import NhanXetRequest
from services.Nhan_Xet import NhanXetUseCase
from api.schemas.requests.Tao_Bai_Kiem_Tra import TaoBaiKiemTraRequest
from services.Tao_Bai_Kiem_Tra import TaoBaiKiemTraUseCase
from api.schemas.requests.Tao_Moc_Quan_Trong import TaoMocQuanTrongRequest
from services.Tao_Moc_Quan_Trong import TaoMocQuanTrongUseCase
from api.schemas.requests.Tao_Nhiem_Vu import TaoNhiemVuRequest
from services.Tao_Nhiem_Vu import TaoNhiemVuUseCase
from api.schemas.responses.Xem_Tin_Lop import TinNhanResponse
from services.Tro_Chuyen import TroChuyenLopUseCase
from api.schemas.requests.Xem_Tin_Nhan_Lop import XemTinNhanLopRequest
from api.schemas.requests.Nhan_Tin import NhanTinRequest
from api.schemas.responses.Nhan_Tin import NhanTinResponse


class GiangVienController:
    def __init__(self, tro_chuyen : TroChuyenLopUseCase , tao_nhiem_vu : TaoNhiemVuUseCase ,tao_moc_quan_trong : TaoMocQuanTrongUseCase, tao_bai_kiem_tra : TaoBaiKiemTraUseCase ,nhan_xet : NhanXetUseCase, xem_du_an : XemDuAnUseCase, xem_lop_hoc : XemLopHocUseCase , phan_nhom : PhanNhomUseCase , xem_nhom : XemNhomUseCase , tao_du_an : TaoDuAnUseCase , giao_du_an : GiaoDuAnUseCase):
        self.ser_xem_lop_hoc = xem_lop_hoc
        self.ser_phan_nhom = phan_nhom
        self.ser_xem_nhom = xem_nhom
        self.ser_tao_du_an = tao_du_an
        self.ser_giao_du_an = giao_du_an
        self.ser_xem_du_an = xem_du_an
        self.ser_nhan_xet = nhan_xet
        self.ser_tao_bai_kiem_tra = tao_bai_kiem_tra
        self.ser_tao_moc_quan_trong = tao_moc_quan_trong
        self.ser_tao_nhiem_vu = tao_nhiem_vu
        self.ser_tro_chuyen = tro_chuyen

    def xem_lop_hoc(self)->list[XemLopHocResponse]:
        try:
            dsLH = self.ser_xem_lop_hoc.execute()
            return [
                XemLopHocResponse(
                    id_lop_hoc=LH.id,
                    id_mon_hoc=LH.mon_hoc.id,
                    ten_mon_hoc=LH.mon_hoc.ten,
                    id_giang_vien=LH.giang_vien.ten,
                )
                for LH in dsLH
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def tao_nhom(self , request :TaoNhomRequest )->TaoNhomResponse:
        try:
            self.ser_phan_nhom.execute(request.id_lop_hoc)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def them_sinh_vien_vao_nhom(self, request : ThemSinhVienNhomRequest):
        try:
            self.ser_phan_nhom.them_sinh_vien(request.id_sinh_vien , request.id_nhom)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def xem_nhom(self , request : XemNhomRequest)->XemNhomResponse:
        try:
            nhom = self.ser_xem_nhom.execute(request.id_nhom)
            return XemNhomResponse(
                id_nhom=nhom.id,
                danh_sach_sinh_vien = [
                    SinhVien(
                        id_sinh_vien=SV.id,
                        ten_sinh_vien=SV.ten
                    )
                    for SV in nhom.danh_sach_hoc_sinh
                ] 
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def tao_du_an(self , request : TaoDuAnRequest )->TaoDuAnRespone:
        try:
            du_an = self.ser_tao_du_an.execute(request.noi_dung , request.id_giang_vien)
            return TaoDuAnRespone(
                id_du_an=du_an.id,
                noi_dung=du_an.noi_dung,
                trang_thai=du_an.trang_thai,
                id_giang_vien=du_an.nguoi_tao.id,
                ten_giang_vien=du_an.nguoi_tao.ten
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def giao_du_an(self, request : GiaoDuAnRequest):
        try:
            self.ser_giao_du_an.execute(request.id_du_an , request.id_lop_hoc)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def xem_du_an(self)->list[XemDuAnResponse]:
        try:
            dsDA = self.ser_xem_du_an.execute()
            return [
                XemDuAnResponse(
                    id_du_an=DA.id,
                    noi_dung=DA.noi_dung,
                    trang_thai=DA.trang_thai,
                    id_giang_vien=DA.nguoi_tao.id,
                    ten_giang_vien=DA.nguoi_tao.ten
                )
                for DA in dsDA
            ]
        except ValueError as e :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def nhan_xet(self , request : NhanXetRequest ):
        try:
            self.ser_nhan_xet.execute(request.noi_dung_nhan_xet , request.id_giang_vien , request.id_bai_lam)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def tao_bai_kiem_tra(self , request : TaoBaiKiemTraRequest ):
        try:
            self.ser_tao_bai_kiem_tra.execute(request.tieu_de , request.de_kiem_tra , request.id_mon_hoc)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    
    def tao_moc_quan_trong(self , request : TaoMocQuanTrongRequest):
        try:
            self.ser_tao_moc_quan_trong.execute(request.noi_dung , request.id_mon_hoc , request.loai_moc)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def tao_nhiem_vu(self , request : TaoNhiemVuRequest):
        try:
            self.ser_tao_nhiem_vu.execute(request.noi_dung,request.id_sinh_vien_thuc_hien,request.id_nguoi_tao,request.vai_tro_nguoi_tao,request.ngay_bat_dau , request.ngay_ket_thuc)
        except ValueError as e :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def xem_tin_nhan_lop(self , request : XemTinNhanLopRequest)->list[TinNhanResponse]:
        try:
            dsTN = self.ser_tro_chuyen.xem_tin_lop(request.id_lop_hoc)
            return [
                TinNhanResponse(
                    id_tin_nhan=tn.id,
                    noi_dung=tn.noi_dung,
                    ten_nguoi_gui=tn.nguoi_gui.ten
                )
                for tn in dsTN
            ]
        except ValueError as e :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def nhan_tin(self, request: NhanTinRequest) -> NhanTinResponse:
        try:
            tin_nhan = self.ser_tro_chuyen.nhan_tin(
                request.noi_dung,
                request.vai_tro_nguoi_gui,
                request.id_nguoi_gui,
                request.id_lop_hoc,
                request.id_nhom
            )

            return NhanTinResponse(
                id_tin_nhan=tin_nhan.id,
                noi_dung=tin_nhan.noi_dung,
                ten_nguoi_gui=tin_nhan.nguoi_gui.ten,
                id_lop_hoc=tin_nhan.lop_hoc.id,
                id_nhom=tin_nhan.nhom.id if tin_nhan.nhom else None
            )
        except ValueError as e :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )