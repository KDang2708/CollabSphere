from domain.models.Tai_Khoan.ITai_Khoan import ITaiKhoanRepository
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan , VaiTro

class RegisterUseCase:
    def __init__(self, repo: ITaiKhoanRepository):
        self.repo = repo

    def execute(self, ten_dang_nhap: str, mat_khau: str, vai_tro : VaiTro) -> TaiKhoan:
        tai_khoan = TaiKhoan(ten_dang_nhap=ten_dang_nhap, mat_khau=mat_khau)
        tai_khoan =  self.repo.add(tai_khoan)
        return tai_khoan