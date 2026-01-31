# from domain.models.Giang_Vien.Giang_Vien import GiangVien
# #from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# #from domain.models.Nhom.Nhom import Nhom
# from domain.models.Mon_Hoc.Mon_Hoc import MonHoc


# class LopHoc:
#     def __init__(
#             self,
#             mon_hoc: MonHoc,
#             giang_vien: GiangVien
#         ):
#         self.id = None
#         self.mon_hoc = mon_hoc
#         self.giang_vien = giang_vien
#         #self.danh_sach_hoc_sinh: list[HocSinh] = []
#         #self.danh_sach_nhom: list[Nhom] = []
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, ForeignKey, Integer
import uuid
class LopHocORM(Base):
    __tablename__ = "lop_hoc"  # tên bảng trong cơ sở dữ liệu
    

    id = Column(
        String(36), 
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )      
    id_mon_hoc = Column(
        String(10),
        ForeignKey("mon_hoc"),
        nullable=False
    )                 
    id_giang_vien = Column(
        String(36),
        ForeignKey("giang_vien"),
        nullable=False
    )
    si_so = Column(
        Integer,
        nullable=False
    )
    
