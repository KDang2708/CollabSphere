#Nhận xét(IDBaiLam(String), NoiDungNhanXet(String), IDGiangVienNhanXet(String))
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Bai_Lam.Bai_Lam import BaiLam
class NhanXet:
    def __init__(self,id : str |None, noi_dung_nhan_xet: str, giang_vien_nhan_xet: GiangVien, bai_lam: BaiLam):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.noi_dung_nhan_xet = noi_dung_nhan_xet
        self.giang_vien_nhan_xet = giang_vien_nhan_xet
        self.bai_lam = bai_lam