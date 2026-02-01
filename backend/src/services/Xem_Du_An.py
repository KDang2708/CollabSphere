from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn

class XemDuAnUseCase():
    def __init__(self, du_an : IDuAn):
        self.redpo_du_an = du_an
    def execute(self)->list[DuAn]:
        return self.redpo_du_an.get_all()