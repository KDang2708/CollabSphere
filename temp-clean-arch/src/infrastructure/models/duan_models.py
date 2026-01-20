from sqlalchemy import Column, String, Boolean
from infrastructure.databases.base import Base


class DuAnModel(Base):
    __tablename__ = "duan"
    __table_args__ = {"extend_existing": True}

    # IDDuAn - Khóa chính
    id = Column("IDDuAn", String(10), primary_key=True)

    # NoiDungDuAn
    noi_dung_du_an = Column("NoiDungDuAn", String(255), nullable=True)

    # TrangThai - Boolean
    trang_thai = Column("TrangThai", Boolean, nullable=True)

    # IDNguoiTao - Khóa ngoại
    id_nguoi_tao = Column("IDNguoiTao", String(10), nullable=False)
