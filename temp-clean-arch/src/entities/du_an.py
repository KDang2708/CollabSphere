from datetime import datetime


class DuAn:
    TRANG_THAI_DANG_THUC_HIEN = "DANG_THUC_HIEN"
    TRANG_THAI_DA_DONG = "DA_DONG"

    def __init__(self, id, ten_du_an, mo_ta="", trang_thai=None,
                 created_at=None, updated_at=None):
        self.id = id
        self.ten_du_an = ten_du_an
        self.mo_ta = mo_ta
        self.trang_thai = trang_thai or self.TRANG_THAI_DANG_THUC_HIEN
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def dong_du_an(self):
        if self.trang_thai == self.TRANG_THAI_DA_DONG:
            raise ValueError("Dự án đã đóng")
        self.trang_thai = self.TRANG_THAI_DA_DONG
        self.updated_at = datetime.utcnow()

    def mo_lai(self):
        self.trang_thai = self.TRANG_THAI_DANG_THUC_HIEN
        self.updated_at = datetime.utcnow()
