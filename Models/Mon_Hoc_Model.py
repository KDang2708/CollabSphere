from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MonHoc(db.Model):
    __tablename__ = 'mon_hoc'
    
    # Các trường cơ bản
    id = db.Column(db.String(50), primary_key=True)
    ten_mon_hoc = db.Column(db.String(100), nullable=False)
    ma_mon_hoc = db.Column(db.String(20), unique=True, nullable=False)
    so_tin_chi = db.Column(db.Integer, default=3)
    mo_ta = db.Column(db.Text)
    
    # Thông tin bổ sung
    hoc_ky = db.Column(db.String(20))
    nam_hoc = db.Column(db.String(9))
    trang_thai = db.Column(db.String(20), default='dang_mo')  # dang_mo, dang_hoc, da_ket_thuc
    loai_mon = db.Column(db.String(30))  # co_ban, chuyen_nganh, tu_chon
    
    # Thời gian
    ngay_bat_dau = db.Column(db.DateTime)
    ngay_ket_thuc = db.Column(db.DateTime)
    ngay_tao = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Liên kết
    giang_vien_phu_trach_id = db.Column(db.String(50), db.ForeignKey('giang_vien.id'))
    
    # Quan hệ
    giang_vien_phu_trach = db.relationship('GiangVien', backref='mon_hoc_phu_trach')
    danh_sach_lop_hoc = db.relationship('LopHoc', backref='mon_hoc', lazy=True)
    danh_sach_nhom = db.relationship('Nhom', backref='mon_hoc', lazy=True)
    
    def __init__(self, id_mon_hoc: str, ten_mon_hoc: str, ma_mon_hoc: str, **kwargs):
        self.id = id_mon_hoc
        self.ten_mon_hoc = ten_mon_hoc
        self.ma_mon_hoc = ma_mon_hoc
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f'<MonHoc {self.ma_mon_hoc}: {self.ten_mon_hoc}>'
    
    # Phương thức quản lý
    def them_lop_hoc(self, ten_lop, si_so_toi_da=40, phong_hoc=None):
        """Thêm lớp học cho môn học"""
        from Models.Lop_Hoc.Lop_Hoc_Model import LopHoc
        
        lop_hoc_moi = LopHoc(
            id_lop=f"{self.ma_mon_hoc}_{ten_lop}",
            ten_lop=ten_lop,
            si_so_toi_da=si_so_toi_da,
            phong_hoc=phong_hoc,
            id_mon_hoc=self.id
        )
        return lop_hoc_moi
    
    def them_nhom_hoc_tap(self, ten_nhom, mo_ta=None):
        """Thêm nhóm học tập cho môn học"""
        from Models.Nhom.Nhom_Model import Nhom
        
        nhom_moi = Nhom(
            id_nhom=f"{self.ma_mon_hoc}_{ten_nhom}",
            ten_nhom=ten_nhom,
            mo_ta=mo_ta,
            mon_hoc_id=self.id
        )
        return nhom_moi
    
    def tinh_so_luong_lop_hoc(self):
        """Tính số lượng lớp học"""
        return len(self.danh_sach_lop_hoc)
    
    def tinh_so_luong_nhom(self):
        """Tính số lượng nhóm học tập"""
        return len(self.danh_sach_nhom)
    
    def kiem_tra_dang_mo(self):
        """Kiểm tra môn học còn mở không"""
        return self.trang_thai == 'dang_mo'
    
    def cap_nhat_trang_thai(self, trang_thai_moi):
        """Cập nhật trạng thái môn học"""
        trang_thai_hop_le = ['dang_mo', 'dang_hoc', 'da_ket_thuc']
        if trang_thai_moi in trang_thai_hop_le:
            self.trang_thai = trang_thai_moi
            return True
        return False

    def to_dict(self, chi_tiet=False):
        data = {
            'id': self.id,
            'ten_mon_hoc': self.ten_mon_hoc,
            'ma_mon_hoc': self.ma_mon_hoc,
            'so_tin_chi': self.so_tin_chi,
            'trang_thai': self.trang_thai,
            'loai_mon': self.loai_mon,
            'hoc_ky': self.hoc_ky,
            'nam_hoc': self.nam_hoc,
            'so_lop_hoc': self.tinh_so_luong_lop_hoc(),
            'so_nhom': self.tinh_so_luong_nhom(),
            'giang_vien_phu_trach_id': self.giang_vien_phu_trach_id,
            'dang_mo': self.kiem_tra_dang_mo()
        }
        
        if chi_tiet:
            data.update({
                'mo_ta': self.mo_ta,
                'ngay_bat_dau': self.ngay_bat_dau.isoformat() if self.ngay_bat_dau else None,
                'ngay_ket_thuc': self.ngay_ket_thuc.isoformat() if self.ngay_ket_thuc else None,
                'ngay_tao': self.ngay_tao.isoformat() if self.ngay_tao else None,
                'ten_giang_vien': self.giang_vien_phu_trach.ten_giang_vien if self.giang_vien_phu_trach else None
            })
        
        return data

    @classmethod
    def tim_theo_id(cls, id_mon_hoc):
        return cls.query.get(id_mon_hoc)
    
    @classmethod
    def tim_theo_ma_mon(cls, ma_mon_hoc):
        return cls.query.filter_by(ma_mon_hoc=ma_mon_hoc).first()
    
    @classmethod
    def lay_theo_hoc_ky(cls, hoc_ky, nam_hoc=None):
        query = cls.query.filter_by(hoc_ky=hoc_ky)
        if nam_hoc:
            query = query.filter_by(nam_hoc=nam_hoc)
        return query.all()
    
    @classmethod
    def lay_theo_giang_vien(cls, giang_vien_id):
        return cls.query.filter_by(giang_vien_phu_trach_id=giang_vien_id).all()
    
    @classmethod
    def lay_theo_loai_mon(cls, loai_mon):
        return cls.query.filter_by(loai_mon=loai_mon).all()
    
    @classmethod
    def tao_moi(cls, id_mon_hoc, ten_mon_hoc, ma_mon_hoc, **kwargs):
        mon_hoc_moi = cls(
            id_mon_hoc=id_mon_hoc,
            ten_mon_hoc=ten_mon_hoc,
            ma_mon_hoc=ma_mon_hoc,
            **kwargs
        )
        db.session.add(mon_hoc_moi)
        db.session.commit()
        return mon_hoc_moi