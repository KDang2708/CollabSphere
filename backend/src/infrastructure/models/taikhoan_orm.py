from infrastructure.database.db import db

class TaiKhoanORM(db.Model):
    __tablename__ = "tai_khoan"

    ten_dang_nhap = db.Column(db.String(30), primary_key=True)
    mat_khau = db.Column(db.String(64), nullable=False)
    vai_tro = db.Column(db.String(20), nullable=False)
    trang_thai = db.Column(db.Boolean, default=True)
