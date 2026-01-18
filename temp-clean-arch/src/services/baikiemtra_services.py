from datetime import datetime
from infrastructure.models.baikiemtra_model import BaiKiemTraModel
from infrastructure.repositories.baikiemtra_repository import BaiKiemTraRepository


class BaiKiemTraService:
    def __init__(self, repository: BaiKiemTraRepository = None):
        self.repository = repository or BaiKiemTraRepository()

    # 1. Tạo bài kiểm tra
    def create_bai_kiem_tra(self, data) -> BaiKiemTraModel:
        bai_kt = BaiKiemTraModel(
            id=data.id,
            id_du_an=data.id_du_an,
            ten_bai_kiem_tra=data.ten_bai_kiem_tra,
            mo_ta=data.mo_ta,
            thoi_gian_lam_bai=data.thoi_gian_lam_bai,
            trang_thai="MOI_TAO",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repository.them_bai_kiem_tra(bai_kt)

    # 2. Lấy bài kiểm tra theo ID
    def get_bai_kiem_tra(self, id: str) -> BaiKiemTraModel:
        bai_kt = self.repository.lay_theo_id(id)
        if not bai_kt:
            raise ValueError("Không tìm thấy bài kiểm tra")
        return bai_kt

    # 3. Danh sách bài kiểm tra theo dự án
    def get_by_du_an(self, id_du_an: str):
        return self.repository.danh_sach_theo_du_an(id_du_an)

    # 4. Cập nhật bài kiểm tra
    def update_bai_kiem_tra(self, id: str, data):
        bai_kt = self.repository.lay_theo_id(id)
        if not bai_kt:
            raise ValueError("Không tìm thấy bài kiểm tra")

        bai_kt.ten_bai_kiem_tra = data.ten_bai_kiem_tra
        bai_kt.mo_ta = data.mo_ta
        bai_kt.thoi_gian_lam_bai = data.thoi_gian_lam_bai
        bai_kt.trang_thai = data.trang_thai
        bai_kt.updated_at = datetime.utcnow()

        return self.repository.cap_nhat_bai_kiem_tra(bai_kt)

    # 5. Đóng bài kiểm tra
    def close_bai_kiem_tra(self, id: str):
        bai_kt = self.repository.lay_theo_id(id)
        if not bai_kt:
            raise ValueError("Không tìm thấy bài kiểm tra")

        bai_kt.trang_thai = "DA_DONG"
        bai_kt.updated_at = datetime.utcnow()
        return self.repository.cap_nhat_bai_kiem_tra(bai_kt)

    # 6. Xóa bài kiểm tra
    def delete_bai_kiem_tra(self, id: str):
        self.repository.xoa_bai_kiem_tra(id)
