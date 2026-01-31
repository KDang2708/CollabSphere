# #Môn học(IDMonHoc(String), TenMonHoc(String), DeCuong(URL))
# class MonHoc:
#     def __init__(
#             self, 
#             ten: str, 
#             de_cuong: str
#         ):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.ten = ten
#         self.de_cuong = de_cuong
from infrastructure.databases.base import Base
from sqlalchemy import Column, String
import uuid
class MonHocORM(Base):
    __tablename__ = "mon_hoc"  # tên bảng trong cơ sở dữ liệu
     

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    ten = Column(
        String(50),
        nullable=False
    )

 # URL đề cương (link file / cloud)
    de_cuong = Column(
        String(500),
        nullable=False
    )