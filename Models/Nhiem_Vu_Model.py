from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class NhiemVu(db.Model):
    __tablename__ = 'nhiem_vu'
    
    # Các trường cơ bản
    id = db.Column(db.String(50), primary_key=True)
    ten_nhiem_vu = db.Column(db.String(200), nullable=False)
    mo_ta = db.Column(db.Text)
    
    # Thời gian
    ngay_giao = db.Column(db.DateTime, default=datetime.utcnow)
    ngay_het_han = db.Column(db.DateTime, nullable=False)
    ngay_hoan_thanh = db.Column(db.DateTime)
    
    # Trạng thái và độ ưu tiên
    trang_thai = db.Column(db.String(20), default='cho_xu_ly')  # cho_xu_ly, dang_thuc_hien, hoan_thanh, qua_han
    do_uu_tien = db.Column(db.Integer, default=1)  # 1: Cao, 2: Trung bình, 3: Thấp
    ti_le_hoan_thanh = db.Column(db.Integer, default=0)  # 0-100
    
    # Liên kết
    nhan_vien_id = db.Column(db.String(50), db.ForeignKey('nhan_vien.id'))
    nhom_id = db.Column(db.String(50), db.ForeignKey('nhom.id'))
    nguoi_giao_id = db.Column(db.String(50), db.ForeignKey('nhan_vien.id'))
    
    # Thông tin bổ sung
    ghi_chu = db.Column(db.Text)
    ket_qua = db.Column(db.Text)
    ngay_cap_nhat = db.Column(db.DateTime, onupdate=datetime.utcnow)
    
    # Quan hệ
    nhan_vien = db.relationship('NhanVien', foreign_keys=[nhan_vien_id], backref='nhiem_vu_duoc_giao')
    nguoi_giao = db.relationship('NhanVien', foreign_keys=[nguoi_giao_id], backref='nhiem_vu_da_giao')
    nhom = db.relationship('Nhom', backref='nhiem_vu')
    danh_sach_phan_hoi = db.relationship('PhanHoi', backref='nhiem_vu', lazy=True, cascade='all, delete-orphan')
    
    def __init__(self, id_nhiem_vu: str, ten_nhiem_vu: str, ngay_het_han: datetime, **kwargs):
        self.id = id_nhiem_vu
        self.ten_nhiem_vu = ten_nhiem_vu
        self.ngay_het_han = ngay_het_han
        
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __repr__(self):
        return f'<NhiemVu {self.id}: {self.ten_nhiem_vu}>'
    
    # Phương thức quản lý nhiệm vụ
    def cap_nhat_trang_thai(self, trang_thai_moi, ti_le_hoan_thanh=None):
        """Cập nhật trạng thái nhiệm vụ"""
        trang_thai_hop_le = ['cho_xu_ly', 'dang_thuc_hien', 'hoan_thanh', 'qua_han']
        
        if trang_thai_moi in trang_thai_hop_le:
            self.trang_thai = trang_thai_moi
            
            if trang_thai_moi == 'hoan_thanh':
                self.ngay_hoan_thanh = datetime.utcnow()
                self.ti_le_hoan_thanh = 100
            elif ti_le_hoan_thanh is not None:
                self.ti_le_hoan_thanh = max(0, min(100, ti_le_hoan_thanh))
            
            self.ngay_cap_nhat = datetime.utcnow()
            return True
        return False
    
    def tinh_so_ngay_con_lai(self):
        """Tính số ngày còn lại đến hạn"""
        if not self.ngay_het_han:
            return None
        
        ngay_con_lai = (self.ngay_het_han - datetime.utcnow()).days
        return ngay_con_lai
    
    def kiem_tra_qua_han(self):
        """Kiểm tra nhiệm vụ có quá hạn không"""
        if self.trang_thai == 'hoan_thanh':
            return False
        
        ngay_con_lai = self.tinh_so_ngay_con_lai()
        return ngay_con_lai is not None and ngay_con_lai < 0
    
    def cap_nhat_ti_le(self, ti_le_moi):
        """Cập nhật tỷ lệ hoàn thành"""
        ti_le_moi = max(0, min(100, ti_le_moi))
        self.ti_le_hoan_thanh = ti_le_moi
        
        if ti_le_moi == 100:
            self.trang_thai = 'hoan_thanh'
            self.ngay_hoan_thanh = datetime.utcnow()
        elif ti_le_moi > 0:
            self.trang_thai = 'dang_thuc_hien'
        
        self.ngay_cap_nhat = datetime.utcnow()
        return self
    
    def them_phan_hoi(self, noi_dung, nguoi_gui_id):
        """Thêm phản hồi cho nhiệm vụ"""
        from Models.Phan_Hoi.Phan_Hoi_Model import PhanHoi
        
        phan_hoi_moi = PhanHoi(
            noi_dung=noi_dung,
            nguoi_gui_id=nguoi_gui_id,
            nhiem_vu_id=self.id
        )
        self.danh_sach_phan_hoi.append(phan_hoi_moi)
        return phan_hoi_moi
    
    def to_dict(self, chi_tiet=False):
        data = {
            'id': self.id,
            'ten_nhiem_vu': self.ten_nhiem_vu,
            'trang_thai': self.trang_thai,
            'ti_le_hoan_thanh': self.ti_le_hoan_thanh,
            'do_uu_tien': self.do_uu_tien,
            'ngay_het_han': self.ngay_het_han.isoformat() if self.ngay_het_han else None,
            'ngay_con_lai': self.tinh_so_ngay_con_lai(),
            'qua_han': self.kiem_tra_qua_han(),
            'nhan_vien_id': self.nhan_vien_id,
            'nguoi_giao_id': self.nguoi_giao_id,
            'nhom_id': self.nhom_id
        }
        
        if chi_tiet:
            data.update({
                'mo_ta': self.mo_ta,
                'ngay_giao': self.ngay_giao.isoformat() if self.ngay_giao else None,
                'ngay_hoan_thanh': self.ngay_hoan_thanh.isoformat() if self.ngay_hoan_thanh else None,
                'ngay_cap_nhat': self.ngay_cap_nhat.isoformat() if self.ngay_cap_nhat else None,
                'ghi_chu': self.ghi_chu,
                'ket_qua': self.ket_qua,
                'so_phan_hoi': len(self.danh_sach_phan_hoi),
                'ten_nhan_vien': self.nhan_vien.ten_nhan_vien if self.nhan_vien else None,
                'ten_nguoi_giao': self.nguoi_giao.ten_nhan_vien if self.nguoi_giao else None
            })
        
        return data

    @classmethod
    def tim_theo_id(cls, id_nhiem_vu):
        return cls.query.get(id_nhiem_vu)
    
    @classmethod
    def lay_theo_nhan_vien(cls, nhan_vien_id, trang_thai=None):
        query = cls.query.filter_by(nhan_vien_id=nhan_vien_id)
        if trang_thai:
            query = query.filter_by(trang_thai=trang_thai)
        return query.order_by(cls.do_uu_tien, cls.ngay_het_han).all()
    
    @classmethod
    def lay_qua_han(cls):
        return cls.query.filter(
            cls.trang_thai != 'hoan_thanh',
            cls.ngay_het_han < datetime.utcnow()
        ).all()
    
    @classmethod
    def lay_theo_do_uu_tien(cls, do_uu_tien):
        return cls.query.filter_by(do_uu_tien=do_uu_tien, trang_thai='dang_thuc_hien').all()
    
    @classmethod
    def tao_moi(cls, id_nhiem_vu, ten_nhiem_vu, ngay_het_han, **kwargs):
        nhiem_vu_moi = cls(
            id_nhiem_vu=id_nhiem_vu,
            ten_nhiem_vu=ten_nhiem_vu,
            ngay_het_han=ngay_het_han,
            **kwargs
        )
        db.session.add(nhiem_vu_moi)
        db.session.commit()
        return nhiem_vu_moi
    
    @classmethod
    def dem_theo_trang_thai(cls, nhan_vien_id=None):
        from sqlalchemy import func
        query = db.session.query(cls.trang_thai, func.count(cls.id))
        
        if nhan_vien_id:
            query = query.filter_by(nhan_vien_id=nhan_vien_id)
        
        query = query.group_by(cls.trang_thai)
        ket_qua = query.all()
        
        return {trang_thai: so_luong for trang_thai, so_luong in ket_qua}