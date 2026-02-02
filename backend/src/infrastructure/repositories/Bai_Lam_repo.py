from domain.models.Bai_Lam.Bai_Lam import BaiLam
from domain.models.Bai_Lam.iBai_Lam import IBaiLamRepository
from infrastructure.models.Bai_Lam_Model import BaiLamORM
from sqlalchemy.orm import Session
from domain.models.Bai_Kiem_Tra.iBai_Kiem_Tra import IBaiKiemTraRepository
from domain.models.Nhiem_Vu.iNhiem_Vu import INhiemVuRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository

class BaiLamRepository(IBaiLamRepository):
    def __init__(self , session : Session ,sinh_vien : ISinhVienRepository, bai_kiem_tra : IBaiKiemTraRepository , nhiem_vu : INhiemVuRepository):
        self.session = session
        self.repo_bai_kiem_tra = bai_kiem_tra
        self.repo_nhiem_vu = nhiem_vu
        self.repo_sinh_vien = sinh_vien

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
    def get_by_id(self, id_bai_lam : str)->BaiLam:
        orm = self.session.query(BaiLamORM).filter(BaiLamORM.id==id_bai_lam).first()
        if orm is None:
            raise Exception("Không tìm thấy bài làm")
        return BaiLam(
            id=orm.id,
            noi_dung_bai_lam= orm.noi_dung_bai_lam,
            loai_bai_lam=orm.loai_bai_lam,
            bai_kiem_tra=self.repo_bai_kiem_tra.get_by_id(orm.id_bai_kiem_tra) if orm.loai_bai_lam == 0 else self.repo_nhiem_vu.get_by_id(orm.id_bai_kiem_tra),
            sinh_vien_thuc_hien=self.repo_sinh_vien.get_by_id(orm.id_sinh_vien_thuc_hien)
        )
    





# from infrastructure.databases.base import Base
# from sqlalchemy import Column, String
# class BaiLamORM(Base):
#     __tablename__ = "bai_lam"  # tên bảng trong cơ sở dữ liệu

#     id = Column(String, primary_key=True)              # cột ID, kiểu String, là khóa chính
#     noi_dung_bai_lam = Column(String)                  # cột nội dung bài làm, kiểu String
#     loai_bai_lam = Column(int)    # 0 là bài kiểm tra, 1 là nhiệm vụ
#     id_bai_kiem_tra = Column(String)               # cột ID bài kiểm tra hoặc nhiệm vụ liên kết, kiểu String
#     id_sinh_vien_thuc_hien = Column(String)           # cột ID sinh viên thực hiện, kiểu String