from domain.models.Nhom.Nhom import Nhom
from domain.models.Nhom.iNhom import INhomRepository
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
class PhanNhomUseCase():
    def __init__(self, nhom : INhomRepository):
        self.repo_nhom = nhom
    def execute(self, lop_hoc : LopHoc)->Nhom:
        nhom = Nhom(lop_hoc=lop_hoc)
        return self.repo_nhom.add(nhom)
    def them_sinh_vien(self, sinh_vien : SinhVien, nhom : Nhom )->bool:
        return self.repo_nhom.add_sinh_vien(sinh_vien,nhom)
