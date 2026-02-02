from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository

class GiaoDuAnUseCase():
    def __init__(self , du_an : IDuAn , lop_hoc : ILopHocRepository):
        self.repo_du_an = du_an
        self.repo_lop_hoc = lop_hoc
    def execute(self , id_du_an : str , id_lop_hoc : LopHoc  )->DuAn:
        du_an= self.repo_du_an.get_by_id(id_du_an)
        lop_hoc = self.repo_lop_hoc.get_by_id(id_lop_hoc)
        du_an= self.repo_du_an.set_lop( du_an , lop_hoc) 
