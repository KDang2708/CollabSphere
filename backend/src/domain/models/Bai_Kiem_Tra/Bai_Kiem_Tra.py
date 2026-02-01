#Bài kiểm tra(IDBaiKiemTra(String), DeKiemTra(String), IDMonHoc(String) )
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
class BaiKiemTra:
    def __init__(self,id : str | None, de_kiem_tra: str, tieu_de : str, mon_hoc: MonHoc ):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.tieu_de = tieu_de
        self.de_kiem_tra = de_kiem_tra
        self.mon_hoc = mon_hoc
        