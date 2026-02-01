# from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
# class BaiKiemTra:
#     def __init__(self, de_kiem_tra: list[str], mon_hoc: MonHoc):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.de_kiem_tra = de_kiem_tra
#         self.mon_hoc = mon_hoc
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class BaiKiemTraORM(Base):
    __tablename__ = "bai_kiem_tra"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda : str(uuid.uuid4()))      # cột ID, kiểu String, là khóa chính
    tieu_de = Column(String, nullable = False)
    de_kiem_tra = Column(String)                # cột đề kiểm tra, kiểu String
    id_mon_hoc = Column(String , ForeignKey("mon_hoc.id"))                 # cột ID môn học liên kết, kiểu String
    # id_lop_hoc = Column(String , ForeignKey("lop_hoc"))     # ko cần 