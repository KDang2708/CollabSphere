from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Nhom.iNhom import INhomRepository
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository

class XemLopHocUseCase():
    def __init__(self , lop_hoc : ILopHocRepository, nhom : INhomRepository, mon_hoc : IMonHocRepository):
        self.repo_lop_hoc=lop_hoc
        self.repo_nhom = nhom
        self.repo_mon_hoc = mon_hoc
    def execute(self)->list[LopHoc]:
        return self.repo_lop_hoc.get_all()
    def xem_chi_tiet(self, lop_hoc : LopHoc)->LopHoc:
        lop_hoc.danh_sach_hoc_sinh = self.repo_lop_hoc.get_sinh_vien(lop_hoc) # tra về danh sách sinh viên
        # lop_hoc.danh_sach_nhom = self.repo_nhom.get_nhom_theo_lop(lop_hoc) # trả về danh sách nhóm của lớp
        return lop_hoc