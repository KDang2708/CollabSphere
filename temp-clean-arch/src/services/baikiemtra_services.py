from datetime import datetime
from infrastructure.models.baikiemtra_models import BaiKiemTraModel
from infrastructure.repositories.baikiemtra_repositories import BaiKiemTraRepository


class BaiKiemTraService:
    """
    Service xử lý nghiệp vụ Bài Kiểm Tra
    """

    def __init__(self, repository: BaiKiemTraRepository):
        self.repository = repository

    # ===============================
    # TẠO BÀI KIỂM TRA
    # ===============================
    def tao_bai_kiem_tra(self, du_lieu) -> BaiKiemTraModel:
        du_lieu.trang_thai = du_lieu.trang_thai or "MOI_TAO"
        return self.repository.them_bai_kiem_tra(du_lieu)

    # ===============================
    # LẤY THEO ID
    # ===============================
    def lay_theo_id(self, id_bai_kiem_tra: str) -> BaiKiemTraModel:
        bai_kt = self.repository.lay_theo_id(id_bai_kiem_tra)
        if not bai_kt:
            raise ValueError("Không tìm thấy bài kiểm tra")
        return bai_kt

    # ===============================
    # DANH SÁCH THEO DỰ ÁN
    # ===============================
    def danh_sach_theo_du_an(self, id_du_an: str):
        return self.repository.danh_sach_theo_du_an(id_du_an)

    # ===============================
    # CẬP NHẬT
    # ===============================
    def cap_nhat(self, du_lieu) -> BaiKiemTraModel:
        return self.repository.cap_nhat_bai_kiem_tra(du_lieu)

    # ===============================
    # ĐÓNG BÀI KIỂM TRA
    # ===============================
    def dong_bai_kiem_tra(self, id_bai_kiem_tra: str):
        bai_kt = self.lay_theo_id(id_bai_kiem_tra)
        bai_kt.trang_thai = "DA_DONG"
        return self.repository.cap_nhat_bai_kiem_tra(bai_kt)

    # ===============================
    # XÓA
    # ===============================
    def xoa(self, id_bai_kiem_tra: str):
        self.repository.xoa_bai_kiem_tra(id_bai_kiem_tra)
