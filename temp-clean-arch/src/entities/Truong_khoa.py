from .du_an import DuAn


class TruongKhoa:
    def __init__(self, ma_tk: str, ten_tk: str):
        self.ma_tk = ma_tk
        self.ten_tk = ten_tk

    def phe_duyet_du_an(self, du_an: DuAn):
        du_an.phe_duyet()
 