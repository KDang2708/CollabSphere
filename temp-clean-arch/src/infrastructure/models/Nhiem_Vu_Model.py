# from datetime import date
# from domain.models.Giang_Vien.Giang_Vien import GiangVien
# from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# class NhiemVu:
#     def __init__(self, id_nguoi_thuc_hien: HocSinh, ngay_bat_dau: date, ngay_ket_thuc: date, id_nguoi_tao: GiangVien | HocSinh):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.id_nguoi_thuc_hien = id_nguoi_thuc_hien
#         self.ngay_bat_dau = ngay_bat_dau
#         self.ngay_ket_thuc = ngay_ket_thuc
#         self.id_nguoi_tao = id_nguoi_tao
from infrastructure.databases.base import Base
from sqlalchemy import Column, String, DateTime , func , ForeignKey
import uuid
class NhiemVuORM(Base):
    __tablename__ = "nhiem_vu"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))          # cột ID, kiểu String, là khóa chính
    noi_dung = Column(String)
    id_nguoi_thuc_hien = Column(String , ForeignKey("sinh_vien.id") )  # người thực hiện là sinh viên         # cột ID người thực hiện, kiểu String
    ngay_bat_dau = Column(DateTime )                    # cột ngày bắt đầu, kiểu Date
    ngay_ket_thuc = Column(DateTime )                   # cột ngày kết thúc, kiểu Date
    id_nguoi_tao = Column(String)                  # cột ID người tạo, kiểu String
    vai_tro_nguoi_tao = Column(String) # dựa vào đây xác định người tạo 
    # class NhiemVu:
    # def __init__(self,id : str | None,id_nguoi_thuc_hien: HocSinh, ngay_bat_dau: datetime | None, ngay_ket_thuc: datetime | None , vai_tro_nguoi_tao : str, id_nguoi_tao: GiangVien | HocSinh):
    #     self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
    #     self.id_nguoi_thuc_hien = id_nguoi_thuc_hien
    #     self.ngay_bat_dau = ngay_bat_dau
    #     self.ngay_ket_thuc = ngay_ket_thuc
    #     self.vai_tro_nguoi_tao = vai_tro_nguoi_tao
    #     self.id_nguoi_tao = id_nguoi_tao