from domain.models.taikhoan import TaiKhoan

class Admin:
    def __init__(
        self,
        id: str,
        ten: str,
        tai_khoan: TaiKhoan
    ):
        self.id = id
        self.ten = ten
        self.tai_khoan = tai_khoan
