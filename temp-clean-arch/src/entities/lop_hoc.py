from typing import List
from .Sinh_vien import SinhVien


class LopHoc:
    def __init__(self, ma_lop: str, ten_lop: str):
        self.ma_lop = ma_lop
        self.ten_lop = ten_lop
        self.sinh_vien: List[SinhVien] = []

    def them_sinh_vien(self, sinh_vien: SinhVien):
        self.sinh_vien.append(sinh_vien)
