from domain.models.Bao_Cao.Bao_Cao import BaoCao
from domain.models.Bao_Cao.iBao_Cao import IBaoCaoRepository
from domain.models.Tai_Khoan.Vai_Tro import VaiTro


class DocBaoCaoUseCase:
    def __init__(self, bao_cao_repository: IBaoCaoRepository):
        self.bao_cao_repository = bao_cao_repository

    def execute(self, vai_tro: VaiTro) -> list[BaoCao]:
        if vai_tro != VaiTro.ADMIN:
            raise PermissionError("Chỉ Admin mới được đọc báo cáo")

        return self.bao_cao_repository.get_all()
