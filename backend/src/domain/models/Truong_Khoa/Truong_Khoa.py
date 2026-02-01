# from domain.models.Du_An.Du_An import DuAn #Lấy lớp Dự Án để sử dụng trong phương thức của Trưởng Khoa
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class TruongKhoa:
    def __init__(self,id : str | None, ten: str , tai_khoan: TaiKhoan):
        self.id = id
        self.ten = ten
        self.tai_khoan = tai_khoan