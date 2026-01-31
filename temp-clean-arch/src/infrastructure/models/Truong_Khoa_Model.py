# from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
# class TruongKhoa:
#     def __init__(
#             self,id : str | None, 
#             ten: str , 
#             tai_khoan: TaiKhoan
#         ):
#         self.id = id
#         self.ten = ten
#         self.tai_khoan = tai_khoan
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, ForeignKey
import uuid
class TruongKhoaORM(Base):
    __tablename__ = "truong_khoa"  # tên bảng trong cơ sở dữ liệu

    id = Column(
        String(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
    )  # cột ID, kiểu String, là khóa chính
    ten = Column(String(50),nullable=False)                  
    id_tai_khoan = Column(
        String(36),
        ForeignKey("tai_khoan"),
        nullable=False,
        unique=True
    )          