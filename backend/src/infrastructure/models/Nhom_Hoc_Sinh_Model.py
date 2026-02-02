from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
class NhomHocSinhORM(Base):
    __tablename__ = "nhom_hoc_sinh"  # tên bảng trong cơ sở dữ liệu

    id_nhom = Column(String, ForeignKey("nhom.id"), primary_key=True )  # cột ID nhóm, kiểu String, là khóa chính
    id_sinh_vien = Column(String,ForeignKey("sinh_vien.id"),primary_key=True)                 # cột ID học sinh, kiểu String