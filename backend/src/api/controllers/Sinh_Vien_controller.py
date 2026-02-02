from fastapi import HTTPException , status

from services.Xem_Lop_Hoc import XemLopHocUseCase
from api.schemas.responses.Xem_Lop_hoc import XemLopHocResponse
from api.schemas.requests.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocRequest
from api.schemas.responses.Xem_Chi_Tiet_Lop_Hoc import XemChiTietLopHocResponse , SinhVienResponse
from api.schemas.requests.Xem_Nhom_SV import XemNhomSVRequest
from api.schemas.responses.Xem_Nhom_SV import XemNhomSVResponse , SinhVienResponse
from services.Xem_Nhom import XemNhomUseCase
from api.schemas.requests.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocRequest
from api.schemas.responses.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocResponse , LopHocResponse , MocQuanTrongResponse , BaiKiemTraResponse
from services.Xem_Thong_Tin_Lop_Hoc import XemThongTinLopHocUseCase
from api.schemas.requests.Nop_Bai import NopBaiRequest
from services.Nop_Bai_Nop_Ket_Qua import NopBaiUseCase
from api.schemas.requests.Thuc_Hien_Kiem_Tra import ThucHienKiemTraRequest
from api.schemas.responses.Thuc_Hien_Kiem_Tra import BaiKiemTraResponse
from services.Thuc_Hien_Kiem_Tra import ThucHienKiemTraUseCase
from api.schemas.requests.Tao_Nhiem_Vu import TaoNhiemVuRequest
from services.Tao_Nhiem_Vu import TaoNhiemVuUseCase
from api.schemas.requests.Xem_Tin_Nhan_Lop import XemTinNhanLopRequest
from api.schemas.responses.Xem_Tin_Lop import TinNhanResponse
from services.Tro_Chuyen import TroChuyenLopUseCase
from api.schemas.requests.Xem_Tin_Nhom import XemTinNhomRequest
from api.schemas.requests.Nhan_Tin import NhanTinRequest
from api.schemas.responses.Nhan_Tin import NhanTinResponse


class SinhVienController:
    def __init__(self , tro_chuyen : TroChuyenLopUseCase , tao_nhiem_vu : TaoNhiemVuUseCase , thuc_hien_kiem_tra : ThucHienKiemTraUseCase ,nop_bai : NopBaiUseCase , xem_lop_hoc : XemLopHocUseCase, xem_nhom : XemNhomUseCase , xem_thong_tin_lop_hoc : XemThongTinLopHocUseCase):
        self.ser_xem_lop_hoc = xem_lop_hoc
        self.ser_xem_nhom = xem_nhom
        self.ser_xem_thong_tin_lop_hoc = xem_thong_tin_lop_hoc
        self.ser_nop_bai = nop_bai
        self.ser_thuc_hien_kiem_tra = thuc_hien_kiem_tra
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
                    id_giang_vien=LH.giang_vien.id,
                    ten_giang_vien=LH.giang_vien.ten

                )
                for LH in dsLH
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def xem_chi_tiet_lop_hoc(self , request : XemChiTietLopHocRequest)->XemChiTietLopHocResponse:
        try:
            lop_hoc=self.ser_xem_lop_hoc.xem_chi_tiet(request.id_lop_hoc)
            return XemChiTietLopHocResponse(
                id_lop_hoc=lop_hoc.id,
                id_mon_hoc=lop_hoc.mon_hoc.id,
                ten_mon_hoc=lop_hoc.mon_hoc.ten,
                de_cuong=lop_hoc.mon_hoc.de_cuong,
                id_giang_vien=lop_hoc.giang_vien.id,
                ten_giang_vien=lop_hoc.giang_vien.ten,
                danh_sach_sinh_vien= [
                    SinhVienResponse(
                        SV.id,
                        SV.ten
                    )
                    for SV in lop_hoc.danh_sach_hoc_sinh
                ]
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def xem_nhom_sinh_vien(self , request : XemNhomSVRequest)->XemNhomSVResponse:
        try:
            nhom = self.ser_xem_nhom.execute(request.id_nhom)
            return XemNhomSVResponse(
                id_nhom=nhom.id,
                danh_sach_sinh_vien= [
                    SinhVienResponse(
                        id_sinh_vien=SV.id,
                        ten_sinh_vien=SV.ten
                    )
                    for SV in nhom.danh_sach_hoc_sinh
                ]
            )
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def xem_thong_tin_lop_hoc(self , request : XemThongTinLopHocRequest )->XemThongTinLopHocResponse:
        try:
            result = self.ser_xem_thong_tin_lop_hoc.execute(request.id_lop_hoc)

            return XemThongTinLopHocResponse(
                lop_hoc=LopHocResponse.from_orm(result["lop_hoc"]),

                ds_moc_quan_trong=[
                    MocQuanTrongResponse.from_orm(mq)
                    for mq in result["ds_moc_quan_trong"]
                ],

                ds_bai_kiem_tra=[
                    BaiKiemTraResponse.from_orm(bkt)
                    for bkt in result["ds_bai_kiem_tra"]
                ],
            )
        except HTTPException as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def nop_bai_lam(self, request : NopBaiRequest):
        try:
            self.ser_nop_bai.execute(request.noi_dung_bai_lam , request.loai_bai_lam , request.id_bai_kiem_tra , request.id_sinh_vien)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def thuc_hien_kiem_tra( self , request : ThucHienKiemTraRequest )->list[BaiKiemTraResponse]:
        try:
            dsBKT = self.ser_thuc_hien_kiem_tra.execute(request.id_sinh_vien)
            return [
                BaiKiemTraResponse(
                    id_bai_kiem_tra=BKT.id,
                    tieu_de=BKT.tieu_de,
                    de_kiem_tra=BKT.de_kiem_tra
                )
                for BKT in dsBKT
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
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
    def xem_tin_nhom(self , request : XemTinNhomRequest)->list[TinNhanResponse]:
        try:
            dsTN = self.ser_tro_chuyen.xem_tin_nhom(request.id_lop_hoc , request.id_lop_hoc)
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