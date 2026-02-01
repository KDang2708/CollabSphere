#Tin nhắn(IDTinNhan(String), IDNguoiGui(String), ThoiGianGui(Date + time), 
# IDLopHoc(String), IDNhom(String))
# from datetime import datetime
# from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
# from domain.models.Nhom.Nhom import Nhom
# from domain.models.Giang_Vien.Giang_Vien import GiangVien
# from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# class TinNhan:
#     def __init__(self, nguoi_gui: HocSinh|GiangVien , thoi_gian_gui: datetime, lop_hoc: LopHoc , nhom: Nhom | None = None):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.nguoi_gui = nguoi_gui
#         self.thoi_gian_gui = thoi_gian_gui
#         self.lop_hoc = lop_hoc
#         self.nhom = nhom
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, DateTime , func , ForeignKey
import uuid
class TinNhanORM(Base):
    __tablename__ = "tin_nhan"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))            # cột ID, kiểu String, là khóa chính
    noi_dung = Column(String)
    id_nguoi_gui = Column(String)                     # cột ID người gửi, kiểu String
    vai_tro_nguoi_gui = Column(String)
    thoi_gian_gui = Column(DateTime, server_default=func.now())                  # cột thời gian gửi, kiểu DateTime
    id_lop_hoc = Column(String , ForeignKey("lop_hoc.id"))                       # cột ID lớp học liên kết, kiểu String
    id_nhom = Column(String, ForeignKey("nhom.id"), nullable=True )           # cột ID nhóm liên kết, kiểu String, có thể null