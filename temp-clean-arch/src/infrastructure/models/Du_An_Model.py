# #Dự án(IDDuAn(String), NoiDungDuAn(String), TrangThai(Bool), IDNguoiTao(String))
# from domain.models.Giang_Vien.Giang_Vien import GiangVien
# from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
# class DuAn():
#     def __init__(
#             self,
#             id : str , 
#             noi_dung: str, 
#             nguoi_tao: GiangVien, 
#             lop_hoc : LopHoc, 
#             trang_thai : bool 
#         ):#hàm khởi tạo
#         self.id = id
#         self.noi_dung = noi_dung
#         self.trang_thai = trang_thai
#         self.nguoi_tao = nguoi_tao
#         self.lop_hoc = lop_hoc
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, ForeignKey, Boolean
import uuid
class DuAnORM(Base):
    __tablename__ = "du_an"
   

    id = Column(
        String(36), 
        primary_key=True,
        default=lambda : str(uuid.uuid4())
    )
    noidung = Column(
        String(255),
        nullable=False
    )
    # False = chưa duyệt, True = đã duyệt 
    trang_thai = Column(
        Boolean(1),
        nullable=False,#đảm bảo không tồn tại trạng thái mơ hồ
        default=False  #đảm bảo dự án mới tạo luôn ở trạng thái “chưa duyệt”
    )
    id_nguoi_tao = Column(
        String(10),
        ForeignKey("giang_vien"),
        nullable=False
    )