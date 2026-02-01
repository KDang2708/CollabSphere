# from domain.models.Giang_Vien.Giang_Vien import GiangVien

# class DuAn():
#     def __init__(self, noi_dung: str, nguoi_tao: GiangVien):#hàm khởi tạo
#         self.id = None
#         self.noi_dung = noi_dung
#         self.trang_thai = False
#         self.nguoi_tao = nguoi_tao
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, Boolean , ForeignKey
import uuid
class DuAnORM(Base):
    __tablename__ = "du_an"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))      # cột ID, kiểu String, là khóa chính
    noi_dung = Column(String)                   # cột nội dung dự án, kiểu String
    trang_thai = Column(Boolean , default=False)                # cột trạng thái dự án, kiểu Boolean
    id_nguoi_tao = Column(String , ForeignKey("giang_vien.id"))               # cột ID người tạo dự án, kiểu String
    id_lop_hoc = Column(String, nullable=True)