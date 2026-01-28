from datetime import datetime
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class TinNhan:
    def __init__(self, id : str | None, nguoi_gui: TaiKhoan , thoi_gian_gui: datetime | None, lop_hoc: LopHoc , nhom: Nhom | None):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.nguoi_gui = nguoi_gui
        self.thoi_gian_gui = thoi_gian_gui
        self.lop_hoc = lop_hoc
        self.nhom = nhom