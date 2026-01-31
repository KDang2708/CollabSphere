# #Mốc quan trọng(IDMocQuanTrong(String), NoiDungMocQuanTrong(String), IDMonHoc(String), LoaiMoc(String))
# from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
# class MocQuanTrong:
#     def __init__(
#             self, 
#             noi_dung: str, 
#             mon_hoc: MonHoc, 
#             loai_moc: str
#         ):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung = noi_dung
#         self.mon_hoc = mon_hoc
#         self.loai_moc = loai_moc
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, ForeignKey
import uuid
class MocQuanTrongORM(Base):
    __tablename__ = "moc_quan_trong"  # tên bảng trong cơ sở dữ liệu

    id = Column(
        String(36), 
        primary_key=True,
        default=lambda :str(uuid.uuid4())
    )      
    noi_dung = Column(
        String(225),
        nullable=False
    )
    id_mon_hoc = Column(
        String(36),
        ForeignKey("mon_hoc"),
        nullable=False
    )
 # DEADLINE | MILESTONE | CHECKPOINT
    loai_moc = Column(
        String(20),
        nullable=False
    )