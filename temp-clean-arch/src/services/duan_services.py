from infrastructure.models.duan_model import DuAnModel
from infrastructure.repositories.duan_repository import DuAnRepository
from datetime import datetime

class DuAnService:
    def __init__(self, repo: DuAnRepository = None):
        self.repo = repo or DuAnRepository()

    # 1. Tạo dự án
    def create_du_an(self, data):
        duan = DuAnModel(
            id=data.id,
            ten_du_an=data.ten_du_an,
            mo_ta=data.mo_ta,
            trang_thai="MOI_TAO",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return self.repo.add(duan)

    # 2. Xem chi tiết dự án
    def get_du_an(self, duan_id: str):
        duan = self.repo.get_by_id(duan_id)
        if not duan:
            raise ValueError("Không tìm thấy dự án")
        return duan

    # 3. Danh sách dự án
    def get_all_du_an(self):
        return self.repo.list_all()

    # 4. Cập nhật dự án
    def update_du_an(self, duan_id: str, data):
        duan = self.repo.get_by_id(duan_id)
        if not duan:
            raise ValueError("Không tìm thấy dự án")

        duan.ten_du_an = data.ten_du_an
        duan.mo_ta = data.mo_ta
        duan.trang_thai = data.trang_thai
        duan.updated_at = datetime.utcnow()

        return self.repo.update(duan)

    # 5. Đóng dự án
    def close_du_an(self, duan_id: str):
        duan = self.repo.get_by_id(duan_id)
        duan.trang_thai = "DA_DONG"
        duan.updated_at = datetime.utcnow()
        return self.repo.update(duan)

    # 6. Xóa dự án
    def delete_du_an(self, duan_id: str):
        # sau này có thể kiểm tra còn nhiệm vụ không
        self.repo.delete(duan_id)
