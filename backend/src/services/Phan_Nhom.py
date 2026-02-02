from domain.models.Nhom.Nhom import Nhom
from domain.models.Nhom.iNhom import INhomRepository
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from domain.models.Nhom.iNhom import INhomRepository
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
class PhanNhomUseCase():
    def __init__(self, nhom : INhomRepository , sinh_vien : ISinhVienRepository , lop_hoc : ILopHocRepository):
        self.repo_nhom = nhom
        self.repo_sinh_vien = sinh_vien
        self.repo_lop_hoc = lop_hoc
    def execute(self, id_lop_hoc : str)->Nhom:
        lop_hoc = self.repo_lop_hoc.get_by_id(id_lop_hoc)
        nhom = Nhom(lop_hoc=lop_hoc)
        return self.repo_nhom.add(nhom)
    def them_sinh_vien(self, id_sinh_vien : str , id_nhom : str )->bool:
        sinh_vien = self.repo_sinh_vien.get_by_id(id_sinh_vien)
        nhom = self.repo_nhom.get_by_id(id_nhom)
        return self.repo_nhom.add_sinh_vien(sinh_vien,nhom)
