from domain.models.Bao_Cao.Bao_Cao import BaoCao
from domain.models.Bao_Cao.iBao_Cao import IBaoCaoRepository

class DocBaoCaoUseCase:
    def __init__(self, bao_cao_repository: IBaoCaoRepository ):
        self.bao_cao_repository = bao_cao_repository

    def execute(self) -> list[BaoCao]:
        return self.bao_cao_repository.get_all()
