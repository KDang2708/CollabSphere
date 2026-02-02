#Mốc quan trọng(IDMocQuanTrong(String), NoiDungMocQuanTrong(String), IDMonHoc(String), LoaiMoc(String))
# from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
# class MocQuanTrong:
#     def __init__(self, noi_dung: str, mon_hoc: MonHoc, loai_moc: str):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung = noi_dung
#         self.mon_hoc = mon_hoc
#         self.loai_moc = loai_moc
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class MocQuanTrongORM(Base):
    __tablename__ = "moc_quan_trong"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))      # cột ID, kiểu String, là khóa chính
    noi_dung = Column(String)                   # cột nội dung mốc quan trọng, kiểu String
    id_mon_hoc = Column(String, ForeignKey("mon_hoc") )                 # cột ID môn học liên kết, kiểu String
    loai_moc = Column(String)                   # cột loại mốc quan trọng, kiểu String
    