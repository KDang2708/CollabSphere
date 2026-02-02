from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Bai_Kiem_Tra.iBai_Kiem_Tra import IBaiKiemTraRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
class ThucHienKiemTraUseCase():
    def __init__(self , lop_hoc : ILopHocRepository , bai_kiem_tra : IBaiKiemTraRepository , sinh_vien : ISinhVienRepository):
        self.repo_lop_hoc = lop_hoc
        self.repo_bai_kiem_tra = bai_kiem_tra
        self.repo_sinh_vien = sinh_vien
    def execute(self , id_sinh_vien : str)->list[BaiKiemTra]: 
        # lấy ra danh sách lớp học , lấy ra danh sách mon học , từ danh sách môn học tìm ra danh sách bài kiểm tra
        sinh_vien = self.repo_sinh_vien.get_by_id(id_sinh_vien)
        dsLH = self.repo_lop_hoc.get_lop_by_sinh_vien(sinh_vien)
        dsMH = [
            LH.mon_hoc
            for LH in dsLH
        ]
        dsBKT: list[BaiKiemTra] = []
        for MH in dsMH:
            dsBKT.extend(
                self.repo_bai_kiem_tra.get_by_mon_hoc(MH)
            )
        return dsBKT
