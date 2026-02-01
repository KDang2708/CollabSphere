# class NhanXet:
#     def __init__(self,id : str |None, noi_dung_nhan_xet: str, giang_vien_nhan_xet: GiangVien, bai_lam: BaiLam):
#         self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung_nhan_xet = noi_dung_nhan_xet
#         self.giang_vien_nhan_xet = giang_vien_nhan_xet
#         self.bai_lam = bai_lam

from infrastructure.databases.base import Base
from sqlalchemy import Column , String , ForeignKey
import uuid

class NhanXetORM(Base):
    __tablename__ = "nhan_xet"

    id = Column(String , primary_key=True , default=lambda : str(uuid.uuid4()))
    noi_dung_nhan_xet = Column(String)
    id_giang_vien = Column(String , ForeignKey("giang_vien.id"))
    id_bai_lam = Column(String, ForeignKey("bai_lam.id"))