from sqlalchemy import Column, String, Text
from infrastructure.databases.base import Base


class BaiKiemTraModel(Base):
    __tablename__ = "baikiemtra"
    __table_args__ = {"extend_existing": True}

    # IDBaiKiemTra - Str(10) - Khóa chính
    id = Column("IDBaiKiemTra", String(10), primary_key=True)

    # DeKiemTra - text - 900 chữ
    de_kiem_tra = Column("DeKiemTra", Text, nullable=True)

    # IDMonHoc - Str(10) - Khóa ngoại
    id_mon_hoc = Column("IDMonHoc", String(10), nullable=False)
