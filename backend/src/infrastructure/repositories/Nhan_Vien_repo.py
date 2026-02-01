from domain.models.Nhan_Vien.Nhan_Vien import NhanVien
from domain.models.Nhan_Vien.iNhan_Vien import INhanVienRepository
from infrastructure.models.Nhan_Vien_Model import NhanVienORM
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from sqlalchemy.orm import Session

class NhanVienRepository(INhanVienRepository):
    def __init__(self , session : Session ,tai_khoan : ITaiKhoanRepository):
        self.session = session
        self.repo_tai_khoan = tai_khoan
    def add(self, nhan_vien : NhanVien)->NhanVien:
        orm = NhanVienORM(
            ten = nhan_vien.ten,
            id_tai_khoan = nhan_vien.tai_khoan.id
        )
        self.session.add(orm)
        self.session.flush()
        nhan_vien.id = orm.id
        self.session.commit()
        return nhan_vien
    def get_by_id(self, id_nhan_vien : str)->NhanVien:
        orm = self.session.query(NhanVienORM).filter(NhanVienORM.id == id_nhan_vien).first()
        tai_khoan = self.repo_tai_khoan.get_by_id(orm.id_tai_khoan)
        return NhanVien(
            id=orm.id,
            ten=orm.ten,
            Tai_khoan=tai_khoan
        )

    #     id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    # ten = Column(String)                   # cột tên sinh viên, kiểu String
    # id_tai_khoan = Column(String)  