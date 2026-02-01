from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository
class TaoMonHocUseCase():
    def __init__(self, mon_hoc : IMonHocRepository):
        self.repo_mon_hoc = mon_hoc
    def execute(self,ten_mon_hoc : str, tin_chi : int ,de_cuong : str )->MonHoc:
        mon_hoc = MonHoc(ten=ten_mon_hoc,tin_chi=tin_chi,de_cuong=de_cuong)
        mon_hoc = self.repo_mon_hoc.add(mon_hoc)
        return mon_hoc
