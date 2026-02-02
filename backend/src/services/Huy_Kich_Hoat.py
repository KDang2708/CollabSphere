from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository

class HuyKichHoatUseCase():
    def __init__(self, tai_khoan : ITaiKhoanRepository):
        self.repo_tai_khoan = tai_khoan
    def execute(self, tai_khoan : TaiKhoan)->TaiKhoan:
        temp = self.repo_tai_khoan.get_by_id(tai_khoan)
        if temp.trang_thai==True:
            temp.khoa()
        else:
            raise Exception("Tài khoản đã bị khóa trước đó ! ")
        self.repo_tai_khoan.update(temp)
        return temp
        