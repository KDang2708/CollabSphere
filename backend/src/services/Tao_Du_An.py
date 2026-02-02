from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from domain.models.Giang_Vien.Giang_Vien import GiangVien

class TaoDuAnUseCase():
    def __init__(self , du_an : IDuAn):
        self.repo_du_an = du_an
    def execute(self , noi_dung : str , giang_vien : GiangVien)->DuAn:
        du_an = DuAn( noi_dung= noi_dung , nguoi_tao= giang_vien)
        du_an = self.repo_du_an.add(du_an)
        return du_an
