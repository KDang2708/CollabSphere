from domain.models.Bai_Lam.Bai_Lam import BaiLam
from domain.models.Bai_Lam.iBai_Lam import IBaiLamRepository
from infrastructure.models.Bai_Lam_Model import BaiLamORM
from sqlalchemy.orm import Session

class BaiLamRepository(IBaiLamRepository):
    def __init__(self , session : Session):
        self.session = session
    def add(self , bai_lam : BaiLam)->BaiLam:
        orm = BaiLamORM(
            noi_dung_bai_lam=bai_lam.noi_dung_bai_lam,
            loai_bai_lam = bai_lam.loai_bai_lam,
            id_bai_kiem_tra = bai_lam.bai_kiem_tra.id,
            id_sinh_vien_thuc_hien = bai_lam.sinh_vien_thuc_hien.id
        )
        self.session.add(orm)
        self.session.flush()
        bai_lam.id = orm.id
        self.session.commit()
        return bai_lam






# from infrastructure.databases.base import Base
# from sqlalchemy import Column, String
# class BaiLamORM(Base):
#     __tablename__ = "bai_lam"  # tên bảng trong cơ sở dữ liệu

#     id = Column(String, primary_key=True)              # cột ID, kiểu String, là khóa chính
#     noi_dung_bai_lam = Column(String)                  # cột nội dung bài làm, kiểu String
#     loai_bai_lam = Column(int)    # 0 là bài kiểm tra, 1 là nhiệm vụ
#     id_bai_kiem_tra = Column(String)               # cột ID bài kiểm tra hoặc nhiệm vụ liên kết, kiểu String
#     id_sinh_vien_thuc_hien = Column(String)           # cột ID sinh viên thực hiện, kiểu String