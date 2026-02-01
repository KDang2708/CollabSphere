from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class GiangVien:
    def __init__(self,id : str|None, ten: str, tai_khoan: TaiKhoan ):
        self.id = id # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.ten = ten
        self.tai_khoan = tai_khoan
  