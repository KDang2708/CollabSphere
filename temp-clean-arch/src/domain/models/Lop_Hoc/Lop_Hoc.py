from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
from domain.models.Nhom.Nhom import Nhom
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc

class LopHoc:
    def __init__(
        self,
        mon_hoc: MonHoc,
        giang_vien: GiangVien
    ):
        self.id = None
        self.mon_hoc = mon_hoc
        self.giang_vien = giang_vien
        self.danh_sach_hoc_sinh: list[HocSinh] = []
        self.danh_sach_nhom: list[Nhom] = []
