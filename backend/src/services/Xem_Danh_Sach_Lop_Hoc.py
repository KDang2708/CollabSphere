from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien

class XemDanhSachLopHocUseCase():
    def __init__(self, lop_hoc : ILopHocRepository ):
        self.repo_lop_hoc = lop_hoc
    def execute(self , sinh_vien : SinhVien )->list[LopHoc]:
        return self.repo_lop_hoc.get_lop_by_sinh_vien(sinh_vien)
    