from infrastructure.database.db import db

class SinhVienORM(db.Model):
    __tablename__ = "sinh_vien"

    id = db.Column(db.Integer, primary_key=True)
    ma_sv = db.Column(db.String(10), unique=True, nullable=False)
    ho_ten = db.Column(db.String(50), nullable=False)
