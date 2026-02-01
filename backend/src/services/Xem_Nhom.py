from domain.models.Nhom.Nhom import Nhom
from domain.models.Nhom.iNhom import INhomRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
# Luôn luôn trả về cho api là 1 đối tượng

class XemNhomUseCase():
    def __init__(self, nhom : INhomRepository , sinh_vien : ISinhVienRepository):
        self.repo_nhom = nhom
        self.repo_sinh_vien = sinh_vien
    def execute(self, nhom : Nhom)->Nhom:
        list_id_sinh_vien = self.repo_nhom.get_list_id_sinh_vien(nhom)
        nhom.danh_sach_hoc_sinh=[self.repo_sinh_vien.get_by_id(id) for id in list_id_sinh_vien]
        return nhom