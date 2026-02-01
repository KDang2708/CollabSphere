#Dự án(IDDuAn(String), NoiDungDuAn(String), TrangThai(Bool), IDNguoiTao(String))
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc

class DuAn():
    def __init__(self,id : str |None, noi_dung: str, nguoi_tao: GiangVien, lop_hoc : LopHoc | None , trang_thai : bool | None):#hàm khởi tạo
        self.id = id
        self.noi_dung = noi_dung
        self.trang_thai = trang_thai
        self.nguoi_tao = nguoi_tao
        self.lop_hoc = lop_hoc
