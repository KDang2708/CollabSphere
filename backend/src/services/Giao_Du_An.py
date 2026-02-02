from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc

class GiaoDuAnUseCase():
    def __init__(self , du_an : IDuAn ):
        self.repo_du_an = du_an
    def execute(self , du_an : DuAn , lop_hoc : LopHoc  )->DuAn:
        du_an= self.repo_du_an.set_lop( du_an , lop_hoc)
