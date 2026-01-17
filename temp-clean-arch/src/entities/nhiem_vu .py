from datetime import datetime


class NhiemVu:
    TRANG_THAI_MOI_TAO = "MOI_TAO"
    TRANG_THAI_DANG_LAM = "DANG_LAM"
    TRANG_THAI_HOAN_THANH = "HOAN_THANH"

    def __init__(self, id, id_du_an, ten_nhiem_vu, mo_ta="",
                 trang_thai=None, nguoi_thuc_hien=None,
                 created_at=None, updated_at=None):
        self.id = id
        self.id_du_an = id_du_an
        self.ten_nhiem_vu = ten_nhiem_vu
        self.mo_ta = mo_ta
        self.trang_thai = trang_thai or self.TRANG_THAI_MOI_TAO
        self.nguoi_thuc_hien = nguoi_thuc_hien
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def phan_cong(self, nguoi):
        self.nguoi_thuc_hien = nguoi
        self.trang_thai = self.TRANG_THAI_DANG_LAM
        self.updated_at = datetime.utcnow()

    def cap_nhat_trang_thai(self, trang_thai):
        self.trang_thai = trang_thai
        self.updated_at = datetime.utcnow()

    def hoan_thanh(self):
        self.trang_thai = self.TRANG_THAI_HOAN_THANH
        self.updated_at = datetime.utcnow()
