from sqlalchemy import Column, String, Date
from infrastructure.databases.base import Base


class NhiemVuModel(Base):
    __tablename__ = "nhiemvu"
    __table_args__ = {"extend_existing": True}

    # IDNhiemVu - Khóa chính
    id = Column("IDNhiemVu", String(10), primary_key=True)

    # IDNguoiThucHien - Khóa ngoại
    id_nguoi_thuc_hien = Column("IDNguoiThucHien", String(10), nullable=False)

    # NgayBatDau
    ngay_bat_dau = Column("NgayBatDau", Date, nullable=True)

    # NgayKetThuc
    ngay_ket_thuc = Column("NgayKetThuc", Date, nullable=True)

    # IDNguoiTao - Khóa ngoại
    id_nguoi_tao = Column("IDNguoiTao", String(10), nullable=False)
