#Nhiệm vụ(IDNhiemVu(String), IDNguoiThucHien(String),
#NgayKetThuc(Date), NgayBatDau(Date), IDNguoiTao(String))
from datetime import datetime
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
class NhiemVu:
    def __init__(self,id : str | None,noi_dung : str , nguoi_thuc_hien: HocSinh, ngay_bat_dau: datetime , ngay_ket_thuc: datetime  , nguoi_tao: GiangVien | HocSinh):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.noi_dung = noi_dung
        self.nguoi_thuc_hien = nguoi_thuc_hien # sinh viên thực hiện 
        self.ngay_bat_dau = ngay_bat_dau
        self.ngay_ket_thuc = ngay_ket_thuc
        self.nguoi_tao = nguoi_tao 