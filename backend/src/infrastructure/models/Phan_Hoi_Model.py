# from time import date
# class PhanHoi:
#     def __init__(self, noi_dung: str, ngay_gui: date):
#         self.id = None
#         self.noi_dung = noi_dung
#         self.ngay_gui = ngay_gui
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, DateTime , func , ForeignKey
import uuid
class PhanHoiORM(Base):
    __tablename__ = "phan_hoi"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    noi_dung = Column(String)               # cột nội dung phản hồi, kiểu String
    ngay_gui = Column(DateTime , server_default=func.now() )                 # cột ngày gửi, kiểu Date
    id_bao_cao = Column(String, ForeignKey("bao_cao.id")) 