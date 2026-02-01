from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from infrastructure.models.Giang_Vien_Model import GiangVienORM
from sqlalchemy.orm import Session
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository

class GiangVienRepository(IGiangVienRepository):
    def __init__(self , sesion : Session , tai_khoan : ITaiKhoanRepository ):
        self.session = sesion
        self.repo_tai_khoan = tai_khoan
    def get_by_id(self, id_giang_vien : str)->GiangVien:
        orm = self.session.query(GiangVienORM).filter(GiangVienORM.id == id_giang_vien).first()
        tai_khoan = self.repo_tai_khoan.get_by_id(orm.id_tai_khoan)
        return GiangVien(
            id=orm.id,
            ten=orm.ten,
            tai_khoan=tai_khoan
        )
    def add(self, giang_vien : GiangVien)->GiangVien:
        orm = GiangVienORM(
            ten = giang_vien.ten,
            id_tai_khoan = giang_vien.tai_khoan.id
        )
        self.session.add(orm)
        self.session.flush()
        giang_vien.id = orm.id
        self.session.commit()
        return giang_vien


    #        id = Column(String, primary_key=True , default=lambda : str(uuid.uuid4))  # cột ID, kiểu String, là khóa chính
    # ten = Column(String)                   # cột tên giảng viên, kiểu String
    # id_tai_khoan = Column(String) 