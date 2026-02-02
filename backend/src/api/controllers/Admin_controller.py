from fastapi import HTTPException, status

from services.Doc_Bao_Cao import DocBaoCaoUseCase
from api.schemas.responses.Bao_cao import BaoCaoResponse
from api.schemas.responses.Phan_Hoi import PhanHoiResponse
from api.schemas.requests.Phan_Hoi import PhanHoiRequest
from api.schemas.responses.Tai_Khoan import TaiKhoanResponse
from services.Phan_Hoi_Nguoi_Dung import PhanHoiUseCase
from services.Xem_Tai_Khoan import XemTaiKhoanUseCase
from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
from api.schemas.requests.Huy_Kich_Hoat import HuyKichHoatRequest
from services.Huy_Kich_Hoat import HuyKichHoatUseCase
from api.schemas.requests.Tai_Kich_Hoat import TaiKichHoatRequest
from services.Tai_Kich_Hoat import TaiKichHoatUseCase
from api.schemas.requests.Tim_Kiem_Tai_Khoan import TimKiemTaiKhoanRequest
from services.Tim_Kiem_Tai_Khoan import TimKiemTaiKhoanUseCase



class AdminController:
    def __init__(self , doc_bao_cao : DocBaoCaoUseCase , phan_hoi : PhanHoiUseCase , xem_tai_khoan : XemTaiKhoanUseCase , huy_kich_hoat : HuyKichHoatUseCase , tai_kich_hoat : TaiKichHoatUseCase , tim_kiem_tai_khoan : TimKiemTaiKhoanUseCase):
          self.ser_doc_bao_cao = doc_bao_cao
          self.ser_phan_hoi = phan_hoi
          self.ser_xem_tai_khoan = xem_tai_khoan
          self.ser_huy_kich_hoat = huy_kich_hoat
          self.ser_tai_kich_hoat = tai_kich_hoat
          self.ser_tim_kiem_tai_khoan = tim_kiem_tai_khoan

    def lay_danh_sach_bao_cao(self) ->list[BaoCaoResponse]:
        dsBC = self.ser_doc_bao_cao.execute()
        return [
            BaoCaoResponse(
                id_bao_cao= BC.id,
                ten_nguoi_gui=BC.nguoi_gui.ten_dang_nhap, # UC sẽ trả về tài khoản 
                id_nguoi_gui=BC.nguoi_gui.id,
                noi_dung=BC.noi_dung,
                ngay_gui=BC.ngay_gui,
                phan_hoi=BC.phan_hoi.noi_dung if BC.phan_hoi else None
            )
            for BC in dsBC
        ]
    def phan_hoi_nguoi_dung(self , request : PhanHoiRequest)->PhanHoiResponse:
        try:
            phan_hoi : PhanHoi = self.ser_phan_hoi.execute(
                noi_dung=request.noi_dung,
                bao_cao=request.id_bao_cao
            )
            return PhanHoiResponse(
                id_phan_hoi=phan_hoi.id,
                noi_dung=phan_hoi.noi_dung,
                ngay_gui=phan_hoi.ngay_gui,
                id_bao_cao=phan_hoi.bao_cao.id
            ) 
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def xem_tai_khoan(self)->list[TaiKhoanResponse]:
        try:
            dsTK : list[TaiKhoan] = self.ser_xem_tai_khoan()
            return  [
                TaiKhoanResponse(
                    id_tai_khoan=TK.id,
                    ten_dang_nhap=TK.ten_dang_nhap,
                    vai_tro=TK.vai_tro,
                    trang_thai=TK.trang_thai
                )
                for TK in dsTK
            ]
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
    def huy_kich_hoat(self , request : HuyKichHoatRequest):
        try:
            self.ser_huy_kich_hoat.execute(request.id_tai_khoan)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_428_PRECONDITION_REQUIRED,
                detail=str(e)
            )
    def tai_kich_hoat(self , request : TaiKichHoatRequest ):
        try:
            self.ser_tai_kich_hoat.execute(request.id_tai_khoan)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_428_PRECONDITION_REQUIRED,
                detail=str(e)
            ) 
    def tim_kiem_tai_khoan(self , request : TimKiemTaiKhoanRequest ):
        try:
            self.ser_tim_kiem_tai_khoan.execute(request.id_tai_khoan)
        except ValueError as e :
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
