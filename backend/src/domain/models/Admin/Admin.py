from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class Admin:
    def __init__(self, id : str | None , ten: str, tai_khoan: TaiKhoan):
        self.id = id
        self.ten = ten
        self.tai_khoan = tai_khoan