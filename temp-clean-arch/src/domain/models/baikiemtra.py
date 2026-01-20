class BaiKiemTra:
    def __init__(
        self,noi_dung_bai_kiem_tra: str,de_kiem_tra: str, id_mon_hoc: str):
        self.IdBaiKiemTra = None                  # DB tự sinh id khi lưu bài kiểm tra
        self.noi_dung_bai_kiem_tra = noi_dung_bai_kiem_tra
        self.de_kiem_tra = de_kiem_tra
        self.id_mon_hoc = id_mon_hoc
    