from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository

class TaiKichHoatUseCase( ):
    def __init__(self, tai_khoan : ITaiKhoanRepository):
        self.repo_tai_khoan = tai_khoan
    def execute(self, id_tai_khoan : str ) ->TaiKhoan:
        temp = self.repo_tai_khoan.get_by_id(id_tai_khoan) # nếu ko tìm thấy thì dưới repo báo lỗi
        if temp.trang_thai==False:
            temp.trang_thai=True
        else:
            raise Exception("Tài khoản đang hoạt động !")
        self.repo_tai_khoan.update(temp)
        return temp

