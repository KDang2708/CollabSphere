from sqlalchemy import Column, String, DateTime, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
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
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Một dự án có nhiều nhiệm vụ
    nhiem_vu = relationship(
        "NhiemVuModel",
        back_populates="du_an",
        cascade="all, delete-orphan"
    )

    # Một dự án có nhiều bài kiểm tra
    bai_kiem_tra = relationship(
        "BaiKiemTraModel",
        back_populates="du_an",
        cascade="all, delete-orphan"
    )


class NhiemVuModel(Base):
    __tablename__ = "nhiemvu"
    __table_args__ = {"extend_existing": True}

    id = Column(String(50), primary_key=True)
    id_du_an = Column(String(50), ForeignKey("duan.id"), nullable=False)
    ten_nhiem_vu = Column(String(255), nullable=False)
    mo_ta = Column(String(500))
    trang_thai = Column(String(50), default="MOI_TAO")
    nguoi_thuc_hien = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Nhiệm vụ thuộc về một dự án
    du_an = relationship(
        "DuAnModel",
        back_populates="nhiem_vu"
    )


class BaiKiemTraModel(Base):
    __tablename__ = "baikiemtra"
    __table_args__ = {"extend_existing": True}

    id = Column(String(50), primary_key=True)
    id_du_an = Column(String(50), ForeignKey("duan.id"), nullable=False)
    ten_bai_kiem_tra = Column(String(255), nullable=False)
    mo_ta = Column(String(500))
    thoi_gian_lam_bai = Column(Integer)
    trang_thai = Column(String(50), default="CHUA_MO")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Bài kiểm tra thuộc về một dự án
    du_an = relationship(
        "DuAnModel",
        back_populates="bai_kiem_tra"
    )
