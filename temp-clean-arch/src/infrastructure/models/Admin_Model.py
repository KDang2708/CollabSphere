# from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
# class Admin:
#     def __init__(self, ten: str, tai_khoan: TaiKhoan):
#         self.id = None
#         self.ten = ten
#         self.tai_khoan = tai_khoan
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class AdminORM(Base):
    __tablename__ = "admin"  # tên bảng trong cơ sở dữ liệu
    __table_args__ = {'extend_existing': True} # cho phép mở rộng bảng nếu nó đã tồn tại
    
    id = Column(String, primary_key=True , default = lambda : str(uuid.uuid()))  # cột ID, kiểu String, là khóa chính
    ten = Column(String)                   # cột tên admin, kiểu String
    id_tai_khoan = Column(String , ForeignKey("tai_khoan.id"))          # cột ID tài khoản liên kết, kiểu String
