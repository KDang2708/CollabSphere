from sqlalchemy import Column, String, DateTime, Integer
from infrastructure.databases.base import Base
from datetime import datetime

class BaiKiemTraModel(Base):
    __tablename__ = "baikiemtra"
    __table_args__ = {"extend_existing": True}

    id = Column(String(50), primary_key=True)
    id_du_an = Column(String(50), nullable=False)
    ten_bai_kiem_tra = Column(String(255), nullable=False)
    mo_ta = Column(String(500))
    thoi_gian_lam_bai = Column(Integer)  # phút
    trang_thai = Column(String(50), default="CHUA_MO")
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
