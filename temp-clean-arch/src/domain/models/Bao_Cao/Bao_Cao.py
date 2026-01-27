#Báo cáo(IDBaoCao(String), NoiDung(String), NgayGui(Date) , IDNguoiGui(String))
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
from time import date
class BaoCao:
    def __init__(self, noi_dung: str, ngay_gui: date, nguoi_gui: TaiKhoan,phan_hoi:PhanHoi):
        if not noi_dung or not noi_dung.strip():
            raise ValueError("Nội dung báo cáo không được rỗng")
        self.id = None
        self.noi_dung = noi_dung
        self.ngay_gui = ngay_gui
        self.nguoi_gui = nguoi_gui
        self.phan_hoi = phan_hoi
    