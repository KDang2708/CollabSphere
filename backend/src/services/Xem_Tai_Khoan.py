from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository

class XemTaiKhoanUseCase():
    def __init__(self, tai_khoan : ITaiKhoanRepository):
        self.repo_tai_khoan=tai_khoan
    def execute(self)-> list[TaiKhoan]:
        return self.repo_tai_khoan.get_all()
