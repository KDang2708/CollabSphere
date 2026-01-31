from domain.taikhoan.repository import TaiKhoanRepository
from domain.taikhoan.model import TaiKhoan
from infrastructure.models.taikhoan_orm import TaiKhoanORM
from infrastructure.database.db import db

class TaiKhoanRepositoryImpl(TaiKhoanRepository):

    def save(self, tai_khoan: TaiKhoan):
        orm = TaiKhoanORM(
            ten_dang_nhap=tai_khoan.ten_dang_nhap,
            mat_khau=tai_khoan.mat_khau,
            vai_tro=tai_khoan.vai_tro,
            trang_thai=tai_khoan.trang_thai
        )
        db.session.add(orm)
        db.session.commit()

    def get_by_username(self, username: str) -> TaiKhoan:
        orm = TaiKhoanORM.query.get(username)
        if not orm:
            return None
        return TaiKhoan(
            orm.ten_dang_nhap,
            orm.mat_khau,
            orm.vai_tro,
            orm.trang_thai
        )
