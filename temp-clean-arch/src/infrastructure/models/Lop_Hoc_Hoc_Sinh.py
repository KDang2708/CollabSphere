from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
# 1 Lớp học có nhiều Sinh viên 
# 1 Sinh viên có thể học nhiều Lớp
class LopHocHocSinhORM(Base):
    __tablename__ = "lop_hoc_hoc_sinh"  # tên bảng trong cơ sở dữ liệu
    
    id_lop_hoc = Column(
        String(36), 
        ForeignKey("lop_hoc.id"),
        primary_key=True 
    )            
    id_hoc_sinh = Column(
        String(36), 
        ForeignKey("sinh_vien.id"),
        primary_key=True
    )           