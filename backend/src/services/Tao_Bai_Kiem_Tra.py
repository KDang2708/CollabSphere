from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
from domain.models.Bai_Kiem_Tra.iBai_Kiem_Tra import IBaiKiemTraRepository
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc

class TaoBaiKiemTraUseCase():
    def __init__(self, bai_kiem_tra : IBaiKiemTraRepository):
        self.repo_bai_kiem_tra = bai_kiem_tra
    def execute(self , tieu_de :str , de_kiem_tra : str , mon_hoc : MonHoc)->BaiKiemTra:
        bai_kiem_tra = BaiKiemTra(
            tieu_de=tieu_de,
            de_kiem_tra=de_kiem_tra,
            id=mon_hoc.id
        )
        bai_kiem_tra = self.repo_bai_kiem_tra.add(bai_kiem_tra)
        

# from infrastructure.databases.base import Base
# from sqlalchemy import Column, String , ForeignKey
# import uuid
# class BaiKiemTraORM(Base):
#     __tablename__ = "bai_kiem_tra"  # tên bảng trong cơ sở dữ liệu

#     id = Column(String, primary_key=True , default=lambda : str(uuid.uuid4()))      # cột ID, kiểu String, là khóa chính
#     tieu_de = Column(String, nullable = False)
#     de_kiem_tra = Column(String)                # cột đề kiểm tra, kiểu String
#     id_mon_hoc = Column(String , ForeignKey("mon_hoc"))