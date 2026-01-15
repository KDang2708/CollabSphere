from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base

class LopHocModel(Base):
    __tablename__ = 'lophoc'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(String(50), primary_key=True)
    id_mon_hoc = Column(String(50), nullable=False)
    si_so = Column(Integer, default=0)
    id_giang_vien = Column(String(50))
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 