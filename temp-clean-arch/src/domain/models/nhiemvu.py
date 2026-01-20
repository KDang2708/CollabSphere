class NhiemVu:
    def __init__(
        self,
        ten_nhiem_vu: str,
        id_du_an: str,
        mo_ta: str = None,
        trang_thai: str = "MOI_TAO",
        nguoi_thuc_hien: str = None
    ):
        # DB tự sinh id khi lưu nhiệm vụ
        self.IdNhiemVu = None

        self.ten_nhiem_vu = ten_nhiem_vu
        self.id_du_an = id_du_an
        self.mo_ta = mo_ta
        self.trang_thai = trang_thai
        self.nguoi_thuc_hien = nguoi_thuc_hien
