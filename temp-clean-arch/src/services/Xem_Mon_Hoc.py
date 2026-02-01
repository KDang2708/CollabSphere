from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository

class XemMonHocUseCase():
    def __init__(self, mon_hoc:IMonHocRepository):
        self.repo_mon_hoc = mon_hoc
    def execute(self)->list[MonHoc]:
        return self.repo_mon_hoc.get_all()
