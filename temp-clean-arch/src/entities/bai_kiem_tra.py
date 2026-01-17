from datetime import datetime


class BaiKiemTra:
    TRANG_THAI_CHUA_MO = "CHUA_MO"
    TRANG_THAI_DANG_MO = "DANG_MO"
    TRANG_THAI_DA_DONG = "DA_DONG"

    def __init__(self, id, id_du_an, ten_bai_kiem_tra, mo_ta="",
                 thoi_gian_lam_bai=0, trang_thai=None,
                 created_at=None, updated_at=None):
        self.id = id
        self.id_du_an = id_du_an
        self.ten_bai_kiem_tra = ten_bai_kiem_tra
        self.mo_ta = mo_ta
        self.thoi_gian_lam_bai = thoi_gian_lam_bai
        self.trang_thai = trang_thai or self.TRANG_THAI_CHUA_MO
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def mo_bai_kiem_tra(self):
        if self.trang_thai != self.TRANG_THAI_CHUA_MO:
            raise ValueError("Bài kiểm tra không thể mở")
        self.trang_thai = self.TRANG_THAI_DANG_MO
        self.updated_at = datetime.utcnow()

    def dong_bai_kiem_tra(self):
        self.trang_thai = self.TRANG_THAI_DA_DONG
        self.updated_at = datetime.utcnow()
