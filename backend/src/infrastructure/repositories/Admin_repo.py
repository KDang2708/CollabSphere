from domain.models.Admin.Admin import Admin
from domain.models.Admin.iAdmin import IAdminRepository
from infrastructure.models.Admin_Model import AdminORM
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from sqlalchemy.orm import Session

class AdminRepository(IAdminRepository):
    def __init__(self , session : Session , tai_khoan : ITaiKhoanRepository):
        self.session = session
        self.repo_tai_khoan =tai_khoan
    def add(self, admin : Admin)->Admin:
        orm = AdminORM(
            ten = admin.ten,
            id_tai_khoan = admin.tai_khoan.id
        )
        self.session.add(orm)
        self.session.flush()
        admin.id = orm.id
        self.session.commit()
        return admin
    def get_by_id(self, id_admin : str)->Admin:
        orm = self.session.query(AdminORM).filter(AdminORM.id == id_admin).first()
        return Admin(
            id=orm.id,
            ten=orm.ten,
            tai_khoan=self.repo_tai_khoan.get_by_id(orm.id_tai_khoan)
        )
    #  id = Column(String, primary_key=True , default = lambda : str(uuid.uuid()))  # cột ID, kiểu String, là khóa chính
    # ten = Column(String)                   # cột tên admin, kiểu String
    # id_tai_khoan = Column(String , ForeignKey("tai_khoan"))  