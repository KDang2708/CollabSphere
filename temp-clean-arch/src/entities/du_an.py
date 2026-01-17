from enum import Enum

# ==============================
# Enum trạng thái dự án
# ==============================
class TrangThaiDuAn(Enum):
    CHO_PHE_DUYET = "Chờ phê duyệt"
    DA_PHE_DUYET = "Đã phê duyệt"
    TU_CHOI = "Từ chối"


# ==============================
# Entity: Dự Án
# ==============================
class DuAn:
    def __init__(self, ma_du_an, ten_du_an, mo_ta, kinh_phi):
        self.ma_du_an = ma_du_an
        self.ten_du_an = ten_du_an
        self.mo_ta = mo_ta
        self.kinh_phi = kinh_phi
        self.trang_thai = TrangThaiDuAn.CHO_PHE_DUYET

    def phe_duyet(self):
        self.trang_thai = TrangThaiDuAn.DA_PHE_DUYET

    def tu_choi(self):
        self.trang_thai = TrangThaiDuAn.TU_CHOI

    def __str__(self):
        return f"{self.ma_du_an} - {self.ten_du_an} ({self.trang_thai.value})"


# ==============================
# Entity: Trưởng Khoa
# ==============================
class TruongKhoa:
    def __init__(self, ma_truong_khoa, ten_truong_khoa):
        self.ma_truong_khoa = ma_truong_khoa
        self.ten_truong_khoa = ten_truong_khoa

    def phe_duyet_du_an(self, du_an: DuAn):
        du_an.phe_duyet()

    def tu_choi_du_an(self, du_an: DuAn):
        du_an.tu_choi()


# ==============================
# Entity: Danh sách dự án
# ==============================
class DanhSachDuAn:
    def __init__(self):
        self.danh_sach = []

    def them_du_an(self, du_an: DuAn):
        self.danh_sach.append(du_an)

    def lay_danh_sach_cho_phe_duyet(self):
        return [
            da for da in self.danh_sach
            if da.trang_thai == TrangThaiDuAn.CHO_PHE_DUYET
        ]

    def tim_du_an(self, ma_du_an):
        for da in self.danh_sach:
            if da.ma_du_an == ma_du_an:
                return da
        return None

if __name__ == "__main__":
    ds = DanhSachDuAn()

    da1 = DuAn("DA01", "Hệ thống QLDA", "Quản lý dự án", 10000000)
    da2 = DuAn("DA02", "Website khoa", "Giới thiệu khoa", 5000000)

    ds.them_du_an(da1)
    ds.them_du_an(da2)

    tk = TruongKhoa("TK01", "Nguyễn Văn A")
    tk.phe_duyet_du_an(da1)

    for du_an in ds.danh_sach:
        print(du_an)
