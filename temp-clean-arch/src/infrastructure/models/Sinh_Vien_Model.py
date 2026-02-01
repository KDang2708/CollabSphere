# from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
# class SinhVien:
#     def __init__(self, ten: str, tai_khoan: TaiKhoan | None = None):
#         self.id = None # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.ten = ten
#         self.tai_khoan = tai_khoan
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class SinhVienORM(Base):
    __tablename__ = "sinh_vien"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    ten = Column(String)                   # cột tên sinh viên, kiểu String
    id_tai_khoan = Column(String , ForeignKey("tai_khoan.id"))          # cột ID tài khoản liên kết, kiểu String
