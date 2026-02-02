from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository

class PhanCongLopHocUseCase():
    def __init__(self, lop_hoc : ILopHocRepository , sinh_vien : ISinhVienRepository):
        self.repo_lop_hoc = lop_hoc
        self.repo_sinh_vien = sinh_vien
    def execute(self, id_lop_hoc : str , id_sinh_vien : str) ->LopHoc:
        lop_hoc = self.repo_lop_hoc.get_by_id(id_lop_hoc)
        sinh_vien = self.repo_sinh_vien.get_by_id(id_sinh_vien)
        self.repo_lop_hoc.add_sinh_vien( sinh_vien , lop_hoc )
        lop_hoc.danh_sach_hoc_sinh = self.repo_lop_hoc.get_sinh_vien(lop_hoc)
        return lop_hoc

    