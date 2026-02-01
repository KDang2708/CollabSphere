#Nhân Viên (IdNhanVien(String) , TenNhanVien(String))
# from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
# class NhanVien:
#     def __init__(self, ten: str,Tai_khoan: TaiKhoan | None = None):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.tai_khoan = Tai_khoan
#         self.ten = ten
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class NhanVienORM(Base):
    __tablename__ = "nhan_vien"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda :str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    ten = Column(String)                   # cột tên nhân viên, kiểu String
    id_tai_khoan = Column(String , ForeignKey("tai_khoan.id"))          # cột ID tài khoản liên kết, kiểu String