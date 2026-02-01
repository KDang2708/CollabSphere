from domain.models.Truong_Khoa.Truong_Khoa import TruongKhoa
from domain.models.Truong_Khoa.iTruong_Khoa import ITruongKhoaRepository
from infrastructure.models.Truong_Khoa_Model import TruongKhoaORM
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from sqlalchemy.orm import Session

class TruongKhoaRepository(ITruongKhoaRepository):
    def __init__(self , session : Session , tai_khoan : ITaiKhoanRepository):
        self.session = session
        self.repo_tai_khoan = tai_khoan
    def add(self, truong_khoa : TruongKhoa)->TruongKhoa:
        orm = TruongKhoaORM(
            ten = truong_khoa.ten,
            id_tai_khoan = truong_khoa.tai_khoan.id
        )
        self.session.add(orm)
        self.session.flush()
        truong_khoa.id = orm.id
        self.session.commit()
        return truong_khoa
    
    def get_by_id(self, id_truong_khoa : str)->TruongKhoa:
        orm = self.session.query(TruongKhoaORM).filter(TruongKhoaORM.id == id_truong_khoa).first()
        tai_khoan = self.repo_tai_khoan.get_by_id(orm.id_tai_khoan)
        return TruongKhoa(
            id=orm.id,
            ten=orm.ten,
            tai_khoan=tai_khoan
        )
    


    # id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    # ten = Column(String)                   # cột tên trưởng khoa, kiểu String
    # id_tai_khoan = Column(String)    