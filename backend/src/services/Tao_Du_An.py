from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository

class TaoDuAnUseCase():
    def __init__(self , du_an : IDuAn , giang_vien : IGiangVienRepository):
        self.repo_du_an = du_an
        self.repo_giang_vien = giang_vien
    def execute(self , noi_dung : str , id_giang_vien : str)->DuAn:
        giang_vien = self.repo_giang_vien.get_by_id(id_giang_vien)
        du_an = DuAn( noi_dung= noi_dung , nguoi_tao= giang_vien)
        du_an = self.repo_du_an.add(du_an)
        return du_an
