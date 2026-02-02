#Phản hồi(IDPhanHoi(String), NoiDungPhanHoi(String), NgayGui(Date))
from datetime import datetime
from domain.models.Bao_Cao.Bao_Cao import BaoCao
class PhanHoi:
    def __init__(self, id : str | None, noi_dung: str , ngay_gui: datetime | None, bao_cao : BaoCao ):
        self.id = id
        self.noi_dung = noi_dung
        self.ngay_gui = ngay_gui
        self.bao_cao = bao_cao