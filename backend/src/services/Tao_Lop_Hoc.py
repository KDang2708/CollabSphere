from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan

class TaoLopHocUseCase():
    def __init__(self, lop_hoc : ILopHocRepository):
        self.repo_lop_hoc = lop_hoc

    def execute(self, mon_hoc : MonHoc , giang_vien : TaiKhoan )->LopHoc:
        lop_hoc = LopHoc(mon_hoc=mon_hoc,giang_vien=giang_vien)
        return self.repo_lop_hoc.add(lop_hoc)
        