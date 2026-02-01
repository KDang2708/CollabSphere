#Cuộc họp(ThoiGianBatDau(Date + Time), IDNguoiTao(String) , IDLopHoc(String), IDNhom(String))
from datetime import datetime
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Sinh_Vien.Sinh_Vien import HocSinh
class CuocHop:
    def __init__(self,id :str | None, thoi_gian_bat_dau: datetime , nguoi_tao: GiangVien|HocSinh, lop_hoc: LopHoc , nhom: Nhom | None):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.thoi_gian_bat_dau = thoi_gian_bat_dau
        self.nguoi_tao = nguoi_tao
        self.lop_hoc = lop_hoc
        self.nhom = nhom