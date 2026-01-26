# from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
# class GiangVien:
#     def __init__(self, ten: str, tai_khoan: TaiKhoan ):
#         self.id = None # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.ten = ten
#         self.tai_khoan = tai_khoan
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, ForeignKey
import uuid
class GiangVienORM(Base):
    __tablename__ = "giang_vien"  # tên bảng trong cơ sở dữ liệu
     

    id = Column(
        String(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
    )  
    ten = Column(String(50),nullable=False)                  
    id_tai_khoan = Column(
        String(36),
        ForeignKey("tai_khoan"),
        nullable=False,
        unique=True
    )          