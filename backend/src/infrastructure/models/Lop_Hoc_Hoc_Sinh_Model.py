from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
class LopHocHocSinhORM(Base):
    __tablename__ = "lop_hoc_hoc_sinh"  # tên bảng trong cơ sở dữ liệu

    id_lop_hoc = Column(String, ForeignKey("lop_hoc.id"),primary_key=True )            # cột ID lớp học, kiểu String
    id_sinh_vien = Column(String, ForeignKey("sinh_vien.id"),primary_key=True )           # cột ID học sinh, kiểu String