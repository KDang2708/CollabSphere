from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base
from datetime import datetime

class NhiemVuModel(Base):
    __tablename__ = "nhiemvu"
    __table_args__ = {"extend_existing": True}

    id = Column(String(50), primary_key=True)
    id_du_an = Column(String(50), ForeignKey("duan.id"), nullable=False)  # Khóa ngoại
    ten_nhiem_vu = Column(String(255), nullable=False)
    mo_ta = Column(String(500))
    trang_thai = Column(String(50), default="MOI_TAO")
    nguoi_thuc_hien = Column(String(50))

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Liên kết đến DuAnModel
    du_an = relationship("DuAnModel", back_populates="nhiem_vu")
    # liên kết nguợc lại nhiệm vụ
    nhiem_vu = relationship("NhiemVuModel", back_populates="du_an", cascade="all, delete-orphan")
