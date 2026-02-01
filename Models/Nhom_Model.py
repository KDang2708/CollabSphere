from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class Nhom(db.Model):
    __tablename__ = 'nhom'
    
    id = db.Column(db.String(50), primary_key=True)
    ten_nhom = db.Column(db.String(100), nullable=False)
    mo_ta = db.Column(db.Text)
    trang_thai = db.Column(db.String(20), default='dang_hoat_dong')
    ngay_tao = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    # Quan hệ
    truong_nhom_id = db.Column(db.String(50), db.ForeignKey('nhan_vien.id'))
    mon_hoc_id = db.Column(db.String(50), db.ForeignKey('mon_hoc.id'))
    
    # Quan hệ ngược
    truong_nhom = db.relationship('NhanVien', backref='nhom_lam_truong')
    mon_hoc = db.relationship('MonHoc', backref='nhom')
    thanh_vien = db.relationship('NhomHocSinh', backref='nhom', cascade='all, delete-orphan')
    nhiem_vu = db.relationship('NhiemVu', backref='nhom_assigned')
    
    def __init__(self, id_nhom: str, ten_nhom: str, **kwargs):
        self.id = id_nhom
        self.ten_nhom = ten_nhom
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def tinh_so_thanh_vien(self):
        return len([tv for tv in self.thanh_vien if tv.trang_thai == 'dang_tham_gia'])
    
    def to_dict(self):
        return {
            'id': self.id,
            'ten_nhom': self.ten_nhom,
            'so_thanh_vien': self.tinh_so_thanh_vien(),
            'trang_thai': self.trang_thai,
            'truong_nhom_id': self.truong_nhom_id
        }