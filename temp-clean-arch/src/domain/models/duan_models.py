from sqlalchemy import Column, String, DateTime, Text
from infrastructure.databases.base import Base
from datetime import datetime

class DuAnModel(Base):
    __tablename__ = "duan"
    __table_args__ = {"extend_existing": True}

    id = Column(String(50), primary_key=True)
    ten_du_an = Column(String(255), nullable=False)
    mo_ta = Column(Text)
    trang_thai = Column(String(50), default="MOI_TAO")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<DuAn {self.id} - {self.ten_du_an}>"
