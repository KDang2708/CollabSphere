# #Bài Làm(IDBaiKiemTra(String), NoiDungBaiLam(String), IDSinhVienThucHien(String))
# from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
# from domain.models.Nhiem_Vu.Nhiem_Vu import NhiemVu
# from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# class BaiLam:
#     def __init__(self, noi_dung_bai_lam: str, bai_kiem_tra: BaiKiemTra | NhiemVu, sinh_vien_thuc_hien: HocSinh):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung_bai_lam = noi_dung_bai_lam
#         self.bai_kiem_tra = bai_kiem_tra
#         self.sinh_vien_thuc_hien = sinh_vien_thuc_hien
from infrastructure.databases.base import Base
from sqlalchemy import Column, String , ForeignKey
import uuid
class BaiLamORM(Base):
    __tablename__ = "bai_lam"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))              # cột ID, kiểu String, là khóa chính
    noi_dung_bai_lam = Column(String)                  # cột nội dung bài làm, kiểu String
    loai_bai_lam = Column(String)    # 0 là bài kiểm tra, 1 là nhiệm vụ
    id_bai_kiem_tra = Column(String , ForeignKey("bai_kiem_tra.id"))               # cột ID bài kiểm tra hoặc nhiệm vụ liên kết, kiểu String
    id_sinh_vien_thuc_hien = Column(String, ForeignKey("sinh_vien.id"))           # cột ID sinh viên thực hiện, kiểu String