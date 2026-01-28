from sqlalchemy import Column, String, ForeignKey
from infrastructure.databases.base import Base

class BaiLamORM(Base):
    __tablename__ = "bai_lam"

    id = Column(String, primary_key=True)
    bai_kiem_tra_id = Column(
        String,
        ForeignKey("bai_kiem_tra.id"),
        nullable=False
    )
    nguoi_nop_id = Column(String, nullable=False)
    noi_dung = Column(String, nullable=False)
