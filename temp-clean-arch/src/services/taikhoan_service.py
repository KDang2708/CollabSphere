from domain.taikhoan.model import TaiKhoan
from domain.taikhoan.repository import TaiKhoanRepository


class TaiKhoanService:
    def __init__(self, tai_khoan_repository: TaiKhoanRepository):
        self.tai_khoan_repository = tai_khoan_repository

    def tao_tai_khoan(
        self,
        ten_dang_nhap: str,
        mat_khau: str,
        vai_tro: str,
        trang_thai: bool = True
    ) -> TaiKhoan:

        tai_khoan = TaiKhoan(
            ten_dang_nhap=ten_dang_nhap,
            mat_khau=mat_khau,
            vai_tro=vai_tro,
            trang_thai=trang_thai
        )

        self.tai_khoan_repository.save(tai_khoan)
        return tai_khoan

    def lay_tai_khoan_theo_username(self, username: str) -> TaiKhoan:
        return self.tai_khoan_repository.get_by_username(username)
