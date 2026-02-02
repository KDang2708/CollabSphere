from domain.models.Moc_Quan_Trong.Moc_Quan_Trong import MocQuanTrong
from domain.models.Moc_Quan_Trong.iMoc_Quan_trong import IMocQuanTrongRepository
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository

class TaoMocQuanTrongUseCase():
    def __init__(self , moc_quan_trong : IMocQuanTrongRepository , mon_hoc : IMonHocRepository):
        self.repo_moc_quan_trong = moc_quan_trong
        self.repo_mon_hoc = mon_hoc
    def execute(self , noi_dung : str , id_mon_hoc : str , loai_moc : str )->MocQuanTrong:
        mon_hoc = self.repo_mon_hoc = mon_hoc
        moc_quan_trong = MocQuanTrong(
            noi_dung=noi_dung,
            mon_hoc=mon_hoc,
            loai_moc=loai_moc
        )
        moc_quan_trong = self.repo_moc_quan_trong.add(moc_quan_trong) # viết hàm add cho mốc quan trọng 
        return moc_quan_trong






    #     class MocQuanTrong:
    # def __init__(self,id : str|None, noi_dung: str, mon_hoc: MonHoc, loai_moc: str):
    #     self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
    #     self.noi_dung = noi_dung
    #     self.mon_hoc = mon_hoc
    #     self.loai_moc = loai_moc