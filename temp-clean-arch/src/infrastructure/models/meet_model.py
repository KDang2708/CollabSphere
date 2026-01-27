from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base

class MeetingModel(Base):
    __tablename__ = 'meetings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(DateTime, nullable=False)
    created_at = Column(String(10), nullable=False)  # IDNguoiTao
    class_id = Column(String(10), nullable=False)  # IDLopHoc
    group_id = Column(String(10), nullable=False)  # IDNhom