from .du_an import DuAn
from .bai_kiem_tra import BaiKiemTra
from .bai_lam import BaiLam


class GiangVien:
    def __init__(self, ma_gv: str, ten_gv: str):
        self.ma_gv = ma_gv
        self.ten_gv = ten_gv

    def tao_du_an(self, ma_da: str, ten_da: str, mo_ta: str) -> DuAn:
        return DuAn(ma_da, ten_da, mo_ta)

    def tao_bai_kiem_tra(self, ma_bkt: str, tieu_de: str) -> BaiKiemTra:
        return BaiKiemTra(ma_bkt, tieu_de)

    def cham_bai(self, bai_lam: BaiLam, diem: float):
        bai_lam.cham_diem(diem)
