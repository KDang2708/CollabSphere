#Tin nhắn(IDTinNhan(String), IDNguoiGui(String), ThoiGianGui(Date + time), 
# IDLopHoc(String), IDNhom(String))
from datetime import datetime
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
class TinNhan:
    def __init__(self, nguoi_gui: HocSinh|GiangVien , thoi_gian_gui: datetime, lop_hoc: LopHoc , nhom: Nhom | None = None):
        self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.nguoi_gui = nguoi_gui
        self.thoi_gian_gui = thoi_gian_gui
        self.lop_hoc = lop_hoc
        self.nhom = nhom
