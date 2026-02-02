# #Nhóm(IDNhom(String), IDLopHoc(String), DanhSachSinhVien(List<IDSinhVien))
# from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
# class Nhom:
#     def __init__(self, lop_hoc: LopHoc, danh_sach_hoc_sinh: list[HocSinh]):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.lop_hoc = lop_hoc
#         self.danh_sach_hoc_sinh = danh_sach_hoc_sinh
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class NhomORM(Base):
    __tablename__ = "nhom"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))        # cột ID, kiểu String, là khóa chính
    id_lop_hoc = Column(String , ForeignKey("lop_hoc"))                   # cột ID lớp học liên kết, kiểu String