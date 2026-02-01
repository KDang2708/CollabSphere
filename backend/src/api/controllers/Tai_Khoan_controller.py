from fastapi import HTTPException, status

from api.schemas.requests.Dang_Ki import DangKiRequest
from api.schemas.responses.Dang_Ki import DangKiResponse
from api.schemas.requests.Dang_Nhap import DangNhapRequset
from api.schemas.responses.Dang_Nhap import DangNhapResponse
from services.Dang_Ki import DangKiUseCase
from services.Dang_Nhap import DangNhapUseCase


class TaiKhoanController:

    def __init__(self, dang_ki : DangKiUseCase , dang_nhap : DangNhapUseCase):
        self.ser_dang_ki = dang_ki
        self.ser_dang_nhap = dang_nhap

    def dang_ki(self, request : DangKiRequest) -> DangKiResponse:
        try:
            tai_khoan = self.ser_dang_ki.execute(
                ten_dang_nhap=request.ten_dang_nhap,
                mat_khau=request.mat_khau,
                vai_tro=request.vai_tro.value
            )

            return DangKiResponse(
                id_tai_khoan=tai_khoan.id,
                ten_dang_nhap=tai_khoan.ten_dang_nhap,
                vai_tro=tai_khoan.vai_tro,
                trang_thai= tai_khoan.trang_thai
            )

        except ValueError as e:
            raise HTTPException(
                ma_loi=status.HTTP_400_BAD_REQUEST,
                chi_tiet=str(e)
            )
    def dang_nhap(self , request : DangNhapRequset ) -> DangNhapResponse:
        try:
            token = self.ser_dang_nhap.execute(
                ten_dang_nhap=request.ten_dang_nhap,
                mat_khau = request.mat_khau
            )
            return DangNhapResponse(
                access_token=token
            )
        except ValueError as e:
            raise HTTPException(
                ma_loi=status.HTTP_400_BAD_REQUEST,
                chi_tiet=str(e)
            )