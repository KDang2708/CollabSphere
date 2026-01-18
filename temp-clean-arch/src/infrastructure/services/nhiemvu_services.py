from infrastructure.repositories.nhiemvu_repository import NhiemVuRepository
from infrastructure.models.nhiemvu_model import NhiemVuModel


class NhiemVuService:
    """
    Service xử lý nghiệp vụ Nhiệm Vụ
    """

    def __init__(self, repository: NhiemVuRepository):
        self.repository = repository

    # ===============================
    # TẠO NHIỆM VỤ
    # ===============================
    def tao_nhiem_vu(self, du_lieu) -> NhiemVuModel:
        du_lieu.trang_thai = du_lieu.trang_thai or "MOI_TAO"
        return self.repository.them_nhiem_vu(du_lieu)

    # ===============================
    # LẤY THEO ID
    # ===============================
    def lay_theo_id(self, id_nhiem_vu: str) -> NhiemVuModel:
        nhiem_vu = self.repository.lay_nhiem_vu_theo_id(id_nhiem_vu)
        if not nhiem_vu:
            raise ValueError("Không tìm thấy nhiệm vụ")
        return nhiem_vu

    # ===============================
    # DANH SÁCH THEO DỰ ÁN
    # ===============================
    def danh_sach_theo_du_an(self, id_du_an: str):
        return self.repository.lay_danh_sach_theo_du_an(id_du_an)

    # ===============================
    # CẬP NHẬT
    # ===============================
    def cap_nhat(self, du_lieu) -> NhiemVuModel:
        return self.repository.cap_nhat_nhiem_vu(du_lieu)

    # ===============================
    # PHÂN CÔNG
    # ===============================
    def phan_cong(self, id_nhiem_vu: str, nguoi_thuc_hien: str):
        self.repository.phan_cong_nhiem_vu(id_nhiem_vu, nguoi_thuc_hien)

    # ===============================
    # CẬP NHẬT TRẠNG THÁI
    # ===============================
    def cap_nhat_trang_thai(self, id_nhiem_vu: str, trang_thai: str):
        self.repository.cap_nhat_trang_thai(id_nhiem_vu, trang_thai)

    # ===============================
    # XÓA
    # ===============================
    def xoa(self, id_nhiem_vu: str):
        self.repository.xoa_nhiem_vu(id_nhiem_vu)
