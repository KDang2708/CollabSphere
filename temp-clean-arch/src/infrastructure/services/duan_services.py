from infrastructure.repositories.duan_repository import DuAnRepository
from infrastructure.models.duan_model import DuAnModel


class DuAnService:
    """
    Service xử lý nghiệp vụ Dự Án
    """

    def __init__(self, repository: DuAnRepository):
        self.repository = repository

    # ===============================
    # TẠO DỰ ÁN
    # ===============================
    def tao_du_an(self, du_lieu) -> DuAnModel:
        du_lieu.trang_thai = du_lieu.trang_thai or "MOI_TAO"
        return self.repository.them_du_an(du_lieu)

    # ===============================
    # LẤY THEO ID
    # ===============================
    def lay_theo_id(self, id_du_an: str) -> DuAnModel:
        du_an = self.repository.lay_du_an_theo_id(id_du_an)
        if not du_an:
            raise ValueError("Không tìm thấy dự án")
        return du_an

    # ===============================
    # DANH SÁCH DỰ ÁN
    # ===============================
    def danh_sach_du_an(self):
        return self.repository.lay_danh_sach_du_an()

    # ===============================
    # CẬP NHẬT
    # ===============================
    def cap_nhat(self, du_lieu) -> DuAnModel:
        return self.repository.cap_nhat_du_an(du_lieu)

    # ===============================
    # ĐÓNG DỰ ÁN
    # ===============================
    def dong_du_an(self, id_du_an: str):
        self.repository.dong_du_an(id_du_an)

    # ===============================
    # XÓA
    # ===============================
    def xoa(self, id_du_an: str):
        self.repository.xoa_du_an(id_du_an)
