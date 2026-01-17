from typing import List
from .du_an import DuAn
from .bai_lam import BaiLam


class SinhVien:
    def __init__(self, ma_sv: str, ten_sv: str):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv
        self.du_an: List[DuAn] = []
        self.bai_lam: List[BaiLam] = []

    def tham_gia_du_an(self, du_an: DuAn):
        self.du_an.append(du_an)

    def nop_bai(self, ma_bkt: str, noi_dung: str) -> BaiLam:
        bai_lam = BaiLam(ma_bkt, self.ma_sv, noi_dung)
        self.bai_lam.append(bai_lam)
        return bai_lam
