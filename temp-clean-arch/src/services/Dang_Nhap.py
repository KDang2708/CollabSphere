from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan , VaiTro

class LoginUseCase:
    def __init__(self, repo: ITaiKhoanRepository):
        self.repo = repo

    def execute(self, ten_dang_nhap: str, mat_khau: str , vai_tro : VaiTro) -> TaiKhoan:
        tai_khoan = self.repo.get_by_ten_dang_nhap(ten_dang_nhap)
        if tai_khoan is None:
            return None
        if tai_khoan.trang_thai == False:
            return None
        if tai_khoan.mat_khau != mat_khau:
            return None
        if tai_khoan.vai_tro != vai_tro:
            return None
        return tai_khoan