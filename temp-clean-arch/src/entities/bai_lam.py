from datetime import datetime


class BaiLam:
    def __init__(self, id, id_bai_kiem_tra, id_sinh_vien,
                 diem=None, thoi_diem_nop=None):
        self.id = id
        self.id_bai_kiem_tra = id_bai_kiem_tra
        self.id_sinh_vien = id_sinh_vien
        self.diem = diem
        self.thoi_diem_nop = thoi_diem_nop

    def nop_bai(self):
        self.thoi_diem_nop = datetime.utcnow()

    def cham_diem(self, diem):
        self.diem = diem
