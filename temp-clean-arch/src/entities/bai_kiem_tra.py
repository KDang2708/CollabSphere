from typing import List
from .bai_lam import BaiLam


class BaiKiemTra:
    def __init__(self, ma_bkt: str, tieu_de: str):
        self.ma_bkt = ma_bkt
        self.tieu_de = tieu_de
        self.bai_lam: List[BaiLam] = []

    def them_bai_lam(self, bai_lam: BaiLam):
        self.bai_lam.append(bai_lam)
