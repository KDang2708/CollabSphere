from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan

class SinhVien:
    def __init__(self, ten: str, tai_khoan: TaiKhoan | None = None):
        self.id: int | None = None   # ID sẽ được gán khi lưu vào CSDL
        self.ten: str = ten
        self.tai_khoan: TaiKhoan | None = tai_khoan
