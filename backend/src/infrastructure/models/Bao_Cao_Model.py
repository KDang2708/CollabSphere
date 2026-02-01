#Báo cáo(IDBaoCao(String), NoiDung(String), NgayGui(Date) , IDNguoiGui(String))
from sqlalchemy import Column, String, DateTime , func ,ForeignKey
from infrastructure.databases.base import Base
import uuid
class BaoCaoORM(Base):
    __tablename__ = "bao_cao"

    id = Column(String, primary_key=True, default=lambda:str(uuid.uuid4()))
    noi_dung = Column(String, nullable=False)
    ngay_gui = Column(DateTime , server_default=func.now())
    id_nguoi_gui = Column(String)
    vai_tro_nguoi_gui = Column(String)
    id_phan_hoi = Column(String , ForeignKey("phan_hoi.id") , nullable=True  )

