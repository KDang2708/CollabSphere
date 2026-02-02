# from domain.models.Du_An.Du_An import DuAn #Lấy lớp Dự Án để sử dụng trong phương thức của Trưởng Khoa

# class TruongKhoa:
#     def __init__(self, ten: str):
#         self.id = None
#         self.ten = ten
#         self.tai_khoan = tai_khoan
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class TruongKhoaORM(Base):
    __tablename__ = "truong_khoa"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    ten = Column(String)                   # cột tên trưởng khoa, kiểu String
    id_tai_khoan = Column(String , ForeignKey("tai_khoan"))          # cột ID tài khoản liên kết, kiểu String