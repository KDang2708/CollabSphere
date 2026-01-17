class BaiLam:
    def __init__(self, ma_bai_lam, sinh_vien, bai_kiem_tra, noi_dung):
        self.ma_bai_lam = ma_bai_lam
        self.sinh_vien = sinh_vien
        self.bai_kiem_tra = bai_kiem_tra
        self.noi_dung = noi_dung
        self.nhan_xet = None

    def them_nhan_xet(self, nhan_xet):
        self.nhan_xet = nhan_xet
