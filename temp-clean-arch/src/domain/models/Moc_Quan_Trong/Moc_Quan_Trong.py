#Mốc quan trọng(IDMocQuanTrong(String), NoiDungMocQuanTrong(String), IDMonHoc(String), LoaiMoc(String))
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
class MocQuanTrong:
    def __init__(
            self, 
            noi_dung: str, 
            mon_hoc: MonHoc, 
            loai_moc: str
        ):
        self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.noi_dung = noi_dung
        self.mon_hoc = mon_hoc
        self.loai_moc = loai_moc