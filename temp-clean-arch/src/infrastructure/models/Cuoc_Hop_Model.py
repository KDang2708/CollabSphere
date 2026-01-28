from sqlalchemy import Column, String, DateTime
from infrastructure.databases.base import Base

class CuocHopORM(Base):
    __tablename__ = "cuoc_hop"

    id = Column(String, primary_key=True)
    thoi_gian = Column(DateTime, nullable=False)
    noi_dung = Column(String, nullable=False)
