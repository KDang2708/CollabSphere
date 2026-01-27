from datetime import datetime
from domain.models.Bao_Cao.Bao_Cao import BaoCao

class PhanHoi:
    def __init__(self, noi_dung: str, ngay_gui: datetime, bao_cao: BaoCao):
        self.id: str | None = None     # ID sẽ được gán khi lưu CSDL
        self.noi_dung: str = noi_dung
        self.ngay_gui: datetime = ngay_gui
        self.bao_cao: BaoCao = bao_cao
