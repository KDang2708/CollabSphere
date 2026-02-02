from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien

class PhanCongLopHocUseCase():
    def __init__(self, lop_hoc : ILopHocRepository):
        self.repo_lop_hoc = lop_hoc

    def execute(seft, lop_hoc : LopHoc , sinh_vien : SinhVien) ->LopHoc:
        seft.repo_lop_hoc.add_sinh_vien( sinh_vien , lop_hoc )
        lop_hoc.danh_sach_hoc_sinh = seft.repo_lop_hoc.get_sinh_vien(lop_hoc)
        return lop_hoc

    