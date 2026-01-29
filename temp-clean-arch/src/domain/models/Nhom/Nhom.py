#Nhóm(IDNhom(String), IDLopHoc(String), DanhSachSinhVien(List<IDSinhVien))
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
class Nhom:
    def __init__(self, lop_hoc: LopHoc, danh_sach_hoc_sinh: list[HocSinh]):
        self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.lop_hoc = lop_hoc
        self.danh_sach_hoc_sinh = danh_sach_hoc_sinh
