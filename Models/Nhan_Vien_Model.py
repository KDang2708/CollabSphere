from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class NhanVien(db.Model):
    __tablename__ = 'nhan_vien'
    
    # Các trường cơ bản
    id = db.Column(db.String(50), primary_key=True)
    ten_nhan_vien = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    so_dien_thoai = db.Column(db.String(15))
    chuc_vu = db.Column(db.String(50))  # nhan_vien, quan_ly, giam_doc
    
    # Thông tin bổ sung
    ngay_vao_lam = db.Column(db.DateTime, default=datetime.utcnow)
    trang_thai = db.Column(db.String(20), default='dang_lam_viec')
    phong_ban = db.Column(db.String(100))
    luong_co_ban = db.Column(db.Float)
    
    # Quan hệ
    danh_sach_nhiem_vu = db.relationship('NhiemVu', backref='nhan_vien', lazy=True)
    danh_sach_nhan_xet = db.relationship('NhanXet', backref='nhan_vien', lazy=True)
    nhom_tham_gia = db.relationship('NhomNhanVien', backref='nhan_vien', lazy=True)
    
    def __init__(self, id_nhan_vien: str, ten_nhan_vien: str, email: str, **kwargs):
        self.id = id_nhan_vien
        self.ten_nhan_vien = ten_nhan_vien
        self.email = email
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f'<NhanVien {self.id}: {self.ten_nhan_vien}>'
    
    # Phương thức quản lý
    def them_nhiem_vu(self, ten_nhiem_vu, mo_ta, ngay_het_han, do_uu_tien=1):
        """Thêm nhiệm vụ mới cho nhân viên"""
        from Models.Nhiem_Vu.Nhiem_Vu_Model import NhiemVu
        
        nhiem_vu_moi = NhiemVu(
            ten_nhiem_vu=ten_nhiem_vu,
            mo_ta=mo_ta,
            ngay_het_han=ngay_het_han,
            do_uu_tien=do_uu_tien,
            nhan_vien_id=self.id
        )
        return nhiem_vu_moi
    
    def tinh_so_nhiem_vu(self, trang_thai=None):
        """Tính số nhiệm vụ"""
        if trang_thai:
            return len([nv for nv in self.danh_sach_nhiem_vu if nv.trang_thai == trang_thai])
        return len(self.danh_sach_nhiem_vu)
    
    def tinh_hieu_suat(self):
        """Tính hiệu suất làm việc"""
        tong_nhiem_vu = len(self.danh_sach_nhiem_vu)
        if tong_nhiem_vu == 0:
            return 0
        
        nhiem_vu_hoan_thanh = sum(1 for nv in self.danh_sach_nhiem_vu if nv.trang_thai == 'hoan_thanh')
        return round((nhiem_vu_hoan_thanh / tong_nhiem_vu) * 100, 2)
    
    def cap_nhat_thong_tin(self, **kwargs):
        """Cập nhật thông tin nhân viên"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self
    
    def to_dict(self, chi_tiet=False):
        data = {
            'id': self.id,
            'ten_nhan_vien': self.ten_nhan_vien,
            'email': self.email,
            'so_dien_thoai': self.so_dien_thoai,
            'chuc_vu': self.chuc_vu,
            'phong_ban': self.phong_ban,
            'trang_thai': self.trang_thai,
            'so_nhiem_vu': self.tinh_so_nhiem_vu(),
            'hieu_suat': self.tinh_hieu_suat()
        }
        
        if chi_tiet:
            data.update({
                'ngay_vao_lam': self.ngay_vao_lam.isoformat() if self.ngay_vao_lam else None,
                'luong_co_ban': self.luong_co_ban,
                'so_nhiem_vu_dang_thuc_hien': self.tinh_so_nhiem_vu('dang_thuc_hien'),
                'so_nhiem_vu_hoan_thanh': self.tinh_so_nhiem_vu('hoan_thanh'),
                'so_nhiem_vu_qua_han': self.tinh_so_nhiem_vu('qua_han')
            })
        
        return data
    
    @classmethod
    def tim_theo_id(cls, id_nhan_vien):
        return cls.query.get(id_nhan_vien)
    
    @classmethod
    def tim_theo_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def lay_theo_phong_ban(cls, phong_ban):
        return cls.query.filter_by(phong_ban=phong_ban).all()
    
    @classmethod
    def lay_theo_chuc_vu(cls, chuc_vu):
        return cls.query.filter_by(chuc_vu=chuc_vu).all()
    
    @classmethod
    def tao_moi(cls, id_nhan_vien, ten_nhan_vien, email, **kwargs):
        nhan_vien_moi = cls(
            id_nhan_vien=id_nhan_vien,
            ten_nhan_vien=ten_nhan_vien,
            email=email,
            **kwargs
        )
        db.session.add(nhan_vien_moi)
        db.session.commit()
        return nhan_vien_moi