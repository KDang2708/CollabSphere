from infrastructure.databases.base import Base
from sqlalchemy import Column, String, ForeignKey
import uuid

class SinhVienORM(Base):
    __tablename__ = "sinh_vien"  
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ten = Column(String)
    
    # Thêm ForeignKey để liên kết với bảng tai_khoan
    id_tai_khoan = Column(String, ForeignKey("tai_khoan.id"))