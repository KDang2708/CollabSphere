from sqlalchemy import Column, String, ForeignKey
from infrastructure.databases.base import Base

class AdminORM(Base):
    __tablename__ = "admin"

    id = Column(String, primary_key=True)
    ten = Column(String, nullable=False)
    tai_khoan_id = Column(String, ForeignKey("tai_khoan.id"), nullable=False)
