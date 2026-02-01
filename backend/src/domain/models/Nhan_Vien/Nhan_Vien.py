#Nhân Viên (IdNhanVien(String) , TenNhanVien(String))
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class NhanVien:
    def __init__(self,id :str |None, ten: str,Tai_khoan: TaiKhoan | None = None):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.tai_khoan = Tai_khoan
        self.ten = ten