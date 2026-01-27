from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan

class TruongKhoa:
    def __init__(self, ten: str, tai_khoan: TaiKhoan):
        self.id: str | None = None   # ID sẽ được gán khi lưu vào CSDL
        self.ten: str = ten
        self.tai_khoan: TaiKhoan = tai_khoan
