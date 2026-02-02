from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
# from services.Xem_Du_An import XemDuAnUseCase

class DuyetDuAnUseCase():
    def __init__(self, du_an : IDuAn):
        self.repo_du_an = du_an
    def xem_du_an(self)->list[DuAn]:
        return self.repo_du_an.get_all()
    def duyet_du_an(self , du_an : DuAn)->DuAn:
        du_an = self.repo_du_an.duyet_du_an(du_an)
        return du_an
    def huy_duyet_du_an(self , du_an : DuAn)->DuAn:
        du_an = self.repo_du_an.huy_duyet_du_an(du_an)
        return du_an
    