# #Môn học(IDMonHoc(String), TenMonHoc(String), DeCuong(URL))
# class MonHoc:
#     def __init__(self, ten: str, de_cuong: str):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.ten = ten
#         self.de_cuong = de_cuong
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , Integer
import uuid
class MonHocORM(Base):
    __tablename__ = "mon_hoc"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda : str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    ten = Column(String)                   # cột tên môn học, kiểu String
    de_cuong = Column(String)              # cột đề cương, kiểu String
    tin_chi=Column(Integer)