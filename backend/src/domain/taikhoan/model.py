class TaiKhoan:
    def __init__(
        self,
        ten_dang_nhap: str,
        mat_khau: str,
        vai_tro: str,
        trang_thai: bool = True
    ):
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.vai_tro = vai_tro
        self.trang_thai = trang_thai
