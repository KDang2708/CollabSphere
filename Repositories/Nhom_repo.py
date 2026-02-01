from datetime import datetime
from Models.Nhom.Nhom_Model import Nhom
from Models.Mon_Hoc.Mon_Hoc_Model import MonHoc
from config.database import db

class Nhom_repo:
    
    def tao_nhom(self, ten_nhom, mon_hoc_id, truong_nhom_id=None, **kwargs):
        """Tạo một nhóm mới"""
        try:
            # Tạo ID tự động
            id_nhom = f"NH_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            nhom_moi = Nhom(
                id_nhom=id_nhom,
                ten_nhom=ten_nhom,
                mon_hoc_id=mon_hoc_id,
                truong_nhom_id=truong_nhom_id,
                **kwargs
            )
            
            db.session.add(nhom_moi)
            db.session.commit()
            return nhom_moi
        except Exception as err:
            db.session.rollback()
            print(f"Lỗi khi tạo nhóm: {err}")
            return None
    
    def lay_nhom_theo_id(self, id_nhom):
        """Lấy thông tin nhóm theo ID"""
        try:
            nhom = Nhom.query.get(id_nhom)
            return nhom
        except Exception as err:
            print(f"Lỗi khi lấy nhóm: {err}")
            return None
    
    def lay_nhom_theo_mon_hoc(self, mon_hoc_id):
        """Lấy danh sách nhóm theo môn học"""
        try:
            nhoms = Nhom.query.filter_by(mon_hoc_id=mon_hoc_id).all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi lấy nhóm theo môn học: {err}")
            return []
    
    def cap_nhat_nhom(self, id_nhom, **kwargs):
        """Cập nhật thông tin nhóm"""
        try:
            nhom = Nhom.query.get(id_nhom)
            if not nhom:
                return False
            
            for key, value in kwargs.items():
                if hasattr(nhom, key) and value is not None:
                    setattr(nhom, key, value)
            
            db.session.commit()
            return True
        except Exception as err:
            db.session.rollback()
            print(f"Lỗi khi cập nhật nhóm: {err}")
            return False
    
    def xoa_nhom(self, id_nhom):
        """Đánh dấu nhóm đã kết thúc"""
        try:
            nhom = Nhom.query.get(id_nhom)
            if not nhom:
                return False
            
            nhom.trang_thai = 'da_ket_thuc'
            db.session.commit()
            return True
        except Exception as err:
            db.session.rollback()
            print(f"Lỗi khi xóa nhóm: {err}")
            return False
    
    def lay_nhom_theo_truong_nhom(self, truong_nhom_id):
        """Lấy nhóm theo trưởng nhóm"""
        try:
            nhoms = Nhom.query.filter_by(truong_nhom_id=truong_nhom_id).all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi lấy nhóm theo trưởng nhóm: {err}")
            return []
    
    def lay_nhom_dang_hoat_dong(self):
        """Lấy danh sách nhóm đang hoạt động"""
        try:
            nhoms = Nhom.query.filter_by(trang_thai='dang_hoat_dong').all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi lấy nhóm đang hoạt động: {err}")
            return []
    
    def lay_nhom_da_ket_thuc(self):
        """Lấy danh sách nhóm đã kết thúc"""
        try:
            nhoms = Nhom.query.filter_by(trang_thai='da_ket_thuc').all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi lấy nhóm đã kết thuc: {err}")
            return []
    
    def tim_kiem_nhom(self, tu_khoa, mon_hoc_id=None):
        """Tìm kiếm nhóm theo từ khóa"""
        try:
            query = Nhom.query.filter(
                (Nhom.ten_nhom.ilike(f"%{tu_khoa}%")) |
                (Nhom.mo_ta.ilike(f"%{tu_khoa}%"))
            )
            
            if mon_hoc_id:
                query = query.filter_by(mon_hoc_id=mon_hoc_id)
            
            nhoms = query.all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi tìm kiếm nhóm: {err}")
            return []
    
    def lay_thong_ke_nhom(self, id_nhom):
        """Lấy thống kê của nhóm"""
        try:
            nhom = Nhom.query.get(id_nhom)
            if not nhom:
                return {}
            
            # Tính số thành viên (nếu có quan hệ thanh_vien)
            so_thanh_vien = 0
            if hasattr(nhom, 'thanh_vien') and nhom.thanh_vien:
                so_thanh_vien = len(nhom.thanh_vien)
            
            # Lấy thông tin môn học
            ten_mon_hoc = None
            if nhom.mon_hoc:
                ten_mon_hoc = nhom.mon_hoc.ten_mon_hoc
            
            return {
                'so_thanh_vien': so_thanh_vien,
                'trang_thai': nhom.trang_thai,
                'ten_mon_hoc': ten_mon_hoc,
                'ten_truong_nhom': nhom.truong_nhom.ho_ten if nhom.truong_nhom else None
            }
        except Exception as err:
            print(f"Lỗi khi lấy thống kê nhóm: {err}")
            return {}
    
    def cap_nhat_truong_nhom(self, id_nhom, new_leader_id):
        """Cập nhật trưởng nhóm mới"""
        try:
            nhom = Nhom.query.get(id_nhom)
            if not nhom:
                return False
            
            nhom.truong_nhom_id = new_leader_id
            db.session.commit()
            return True
        except Exception as err:
            db.session.rollback()
            print(f"Lỗi khi cập nhật trưởng nhóm: {err}")
            return False
    
    def kiem_tra_ten_nhom_trung(self, ten_nhom, mon_hoc_id=None):
        """Kiểm tra tên nhóm đã tồn tại chưa"""
        try:
            query = Nhom.query.filter_by(ten_nhom=ten_nhom)
            if mon_hoc_id:
                query = query.filter_by(mon_hoc_id=mon_hoc_id)
            
            nhom = query.first()
            return nhom is not None
        except Exception as err:
            print(f"Lỗi khi kiểm tra tên nhóm: {err}")
            return False
    
    def dem_so_nhom(self):
        """Đếm tổng số nhóm"""
        try:
            count = Nhom.query.count()
            return count
        except Exception as err:
            print(f"Lỗi khi đếm số nhóm: {err}")
            return 0
    
    def dem_so_nhom_theo_mon(self, mon_hoc_id):
        """Đếm số nhóm theo môn học"""
        try:
            count = Nhom.query.filter_by(mon_hoc_id=mon_hoc_id).count()
            return count
        except Exception as err:
            print(f"Lỗi khi đếm số nhóm theo môn: {err}")
            return 0
    
    def phan_trang_nhom(self, page=1, per_page=10, mon_hoc_id=None):
        """Lấy nhóm theo phân trang"""
        try:
            query = Nhom.query
            
            if mon_hoc_id:
                query = query.filter_by(mon_hoc_id=mon_hoc_id)
            
            nhoms = query.paginate(page=page, per_page=per_page, error_out=False)
            return nhoms
        except Exception as err:
            print(f"Lỗi khi phân trang nhóm: {err}")
            return None
    
    def lay_nhom_theo_trang_thai(self, trang_thai):
        """Lấy nhóm theo trạng thái"""
        try:
            nhoms = Nhom.query.filter_by(trang_thai=trang_thai).all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi lấy nhóm theo trạng thái: {err}")
            return []
    
    def lay_nhom_moi_nhat(self, limit=10):
        """Lấy các nhóm mới nhất"""
        try:
            nhoms = Nhom.query.order_by(Nhom.ngay_tao.desc()).limit(limit).all()
            return nhoms
        except Exception as err:
            print(f"Lỗi khi lấy nhóm mới nhất: {err}")
            return []