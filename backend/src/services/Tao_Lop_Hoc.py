from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository

class TaoLopHocUseCase():
    def __init__(self, lop_hoc : ILopHocRepository , mon_hoc : IMonHocRepository , giang_vien : IGiangVienRepository):
        self.repo_lop_hoc = lop_hoc
        self.repo_mon_hoc = mon_hoc
        self.repo_giang_vien = giang_vien
    def execute(self, id_mon_hoc : str , id_giang_vien : str)->LopHoc:
        mon_hoc = self.repo_mon_hoc.get_by_id(id_mon_hoc)
        giang_vien = self.repo_giang_vien.get_by_id(id_giang_vien)
        lop_hoc = LopHoc(mon_hoc=mon_hoc,giang_vien=giang_vien)
        return self.repo_lop_hoc.add(lop_hoc)
        