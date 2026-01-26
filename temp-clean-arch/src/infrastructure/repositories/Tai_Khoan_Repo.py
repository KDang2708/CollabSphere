from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
from infrastructure.models.Tai_Khoan_Model import TaiKhoanORM
from domain.models.Tai_Khoan.Vai_Tro import VaiTro
from sqlalchemy.orm import Session
class TaiKhoanRepository(ITaiKhoanRepository):
    def __init__(self, session:Session):
        self.session = session

    def _to_domain(self, orm: TaiKhoanORM) -> TaiKhoan | None:
        return TaiKhoan(
            id=orm.id,
            ten_dang_nhap=orm.ten_dang_nhap,
            mat_khau=orm.mat_khau,
            vai_tro=VaiTro(orm.vai_tro),
            trang_thai=orm.trang_thai  
        )
    # chuyển từ orm sang domain

    def get_by_id(self, tai_khoan : TaiKhoan) -> TaiKhoan | None:
        orm = self.session.query(TaiKhoanORM).filter_by(id=tai_khoan.id).first()
        if orm is None:
            raise Exception("Tài khoản không tồn tại trên CSDL !")
        return self._to_domain(orm) if orm else None
    

    def add(self, tai_khoan: TaiKhoan) -> TaiKhoan:
        orm = TaiKhoanORM(
                            id=tai_khoan.id, 
                            ten_dang_nhap=tai_khoan.ten_dang_nhap,
                            mat_khau=tai_khoan.mat_khau,
                            vai_tro=tai_khoan.vai_tro.value,
                            trang_thai=tai_khoan.trang_thai
                        )
        self.session.add(orm)
        self.session.commit() # Lưu thay đổi vào cơ sở dữ liệu
        return self._to_domain(orm) # Trả về đối tượng domain đã được lưu để sử dụng tiếp
    def get_all(self)->list[TaiKhoan]:
        orm_list : list[TaiKhoanORM]= self.session.query(TaiKhoanORM).all()
        return [
            self._to_domain(orm)
            for orm in orm_list
        ]

    def update(self, tai_khoan: TaiKhoan) -> None:
        orm : TaiKhoan = (
            self.session
            .query(TaiKhoanORM)
            .filter_by(id=tai_khoan.id)
            .first()
        )

        if orm is None:
            raise Exception("Tài khoản không tồn tại")

        # map Domain -> ORM
        orm.ten_dang_nhap = tai_khoan.ten_dang_nhap
        orm.mat_khau = tai_khoan.mat_khau
        orm.vai_tro = tai_khoan.vai_tro
        orm.trang_thai = tai_khoan.trang_thai

        self.session.commit()