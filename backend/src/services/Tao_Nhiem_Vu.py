from domain.models.Nhiem_Vu.Nhiem_Vu import NhiemVu
from domain.models.Nhiem_Vu.iNhiem_Vu import INhiemVuRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from datetime import datetime

class TaoNhiemVuUseCase:
    def __init__(self, nhiem_vu: INhiemVuRepository):
        self.repo_nhiem_vu = nhiem_vu

    def execute(
        self,
        noi_dung: str,
        sinh_vien: SinhVien,
        nguoi_tao: GiangVien | SinhVien,
        ngay_bat_dau: datetime,
        ngay_ket_thuc: datetime
    ) -> NhiemVu:
        nhiem_vu = NhiemVu(
            noi_dung=noi_dung,
            nguoi_thuc_hien=sinh_vien,      # sinh viên thực hiện nhiệm vụ
            nguoi_tao=nguoi_tao,            # người tạo (giảng viên hoặc sinh viên)
            ngay_bat_dau=ngay_bat_dau,
            ngay_ket_thuc=ngay_ket_thuc
        )
        nhiem_vu = self.repo_nhiem_vu.add(nhiem_vu)
        return nhiem_vu