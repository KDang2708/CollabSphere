from sqlalchemy import Column, String
from infrastructure.databases.base import Base

class BaiKiemTraORM(Base):
    __tablename__ = "bai_kiem_tra"

    id = Column(String, primary_key=True)
    ten = Column(String, nullable=False)
    mo_ta = Column(String)
