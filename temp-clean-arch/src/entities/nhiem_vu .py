class NhiemVu:
    def __init__(self, tieu_de: str, mo_ta: str):
        self.tieu_de = tieu_de
        self.mo_ta = mo_ta
        self.hoan_thanh = False

    def danh_dau_hoan_thanh(self):
        self.hoan_thanh = True
