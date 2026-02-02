from domain.models.Nhiem_Vu.Nhiem_Vu import NhiemVu
from domain.models.Nhiem_Vu.iNhiem_Vu import INhiemVuRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from datetime import datetime
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository

class TaoNhiemVuUseCase():
    def __init__(self , sinh_vien : ISinhVienRepository , nhiem_vu : INhiemVuRepository , giang_vien : IGiangVienRepository ):
        self.repo_nhiem_vu = nhiem_vu
        self.repo_sinh_vien = sinh_vien
        self.repo_giang_vien = giang_vien
    def execute(self , noi_dung : str , id_sinh_vien_thuc_hien : str , id_nguoi_tao : str  , vai_tro_nguoi_tao : int , ngay_bat_dau : datetime , ngay_ket_thuc : datetime )->NhiemVu:
        sinh_vien = self.repo_sinh_vien.get_by_id(id_sinh_vien_thuc_hien)
        if vai_tro_nguoi_tao==0:
            nguoi_tao = self.repo_sinh_vien.get_by_id(id_nguoi_tao)
        else:
            nguoi_tao = self.repo_giang_vien.get_by_id(id_nguoi_tao)
        nhiem_vu = NhiemVu(
            noi_dung=noi_dung,
            nguoi_thuc_hien=sinh_vien,
            ngay_bat_dau=nguoi_tao,
            ngay_bat_dau= ngay_bat_dau,
            ngay_ket_thuc= ngay_ket_thuc
        )
        nhiem_vu = self.repo_nhiem_vu.add(nhiem_vu)
        return nhiem_vu
# class NhiemVu:
#     def __init__(self,id : str | None,noi_dung : str , nguoi_thuc_hien: HocSinh, ngay_bat_dau: datetime | None,
#  ngay_ket_thuc: datetime | None , nguoi_tao: GiangVien | HocSinh):
#         self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung = noi_dung
#         self.nguoi_thuc_hien = nguoi_thuc_hien # sinh viên thực hiện 
#         self.ngay_bat_dau = ngay_bat_dau
#         self.nguoi_tao = nguoi_tao 