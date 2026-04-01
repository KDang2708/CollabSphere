from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class NhomHocSinh(db.Model):
    __tablename__ = 'nhom_hoc_sinh'
    
    # Khóa chính
    hoc_sinh_id = db.Column(db.String(50), db.ForeignKey('hoc_sinh.id'), primary_key=True)
    nhom_id = db.Column(db.String(50), db.ForeignKey('nhom.id'), primary_key=True)
    
    # Thông tin tham gia
    ngay_tham_gia = db.Column(db.DateTime, default=datetime.utcnow)
    vai_tro = db.Column(db.String(20), default='thanh_vien')  # thanh_vien, pho_nhom, truong_nhom
    trang_thai = db.Column(db.String(20), default='dang_tham_gia')
    
    def __init__(self, hoc_sinh_id: str, nhom_id: str, **kwargs):
        self.hoc_sinh_id = hoc_sinh_id
        self.nhom_id = nhom_id
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def to_dict(self):
        return {
            'hoc_sinh_id': self.hoc_sinh_id,
            'nhom_id': self.nhom_id,
            'vai_tro': self.vai_tro,
            'trang_thai': self.trang_thai
        }