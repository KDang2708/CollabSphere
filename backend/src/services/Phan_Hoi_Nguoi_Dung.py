from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
from domain.models.Phan_Hoi.iPhan_Hoi import IPhanHoiRepository
from domain.models.Bao_Cao.Bao_Cao import BaoCao
from domain.models.Bao_Cao.iBao_Cao import IBaoCaoRepository

class PhanHoiUseCase():
    def __init__(self, bao_cao : IBaoCaoRepository, phan_hoi : IPhanHoiRepository):
        self.repo_bao_cao = bao_cao
        self.repo_phan_hoi = phan_hoi
    
    def execute(self, bao_cao : BaoCao, noi_dung : str) -> PhanHoi:
        phan_hoi = PhanHoi(bao_cao=bao_cao,noi_dung=noi_dung)
        phan_hoi = self.repo_phan_hoi.add(phan_hoi)
        bao_cao = self.repo_bao_cao.set_phan_hoi(phan_hoi.id,bao_cao.id)
        return phan_hoi
