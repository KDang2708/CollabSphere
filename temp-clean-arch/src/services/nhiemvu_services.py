from infrastructure.repositories.nhiemvu_repository import NhiemVuRepository
from infrastructure.models.nhiemvu_model import NhiemVuModel

class NhiemVuService:
    def __init__(self, repository: NhiemVuRepository = None):
        self.repository = repository or NhiemVuRepository()

    # 1. Tạo nhiệm vụ
    def create_nhiem_vu(self, data) -> NhiemVuModel:
        return self.repository.add(data)

    # 2. Lấy nhiệm vụ theo ID
    def get_nhiem_vu(self, id: str) -> NhiemVuModel:
        return self.repository.get_by_id(id)

    # 3. Lấy danh sách nhiệm vụ theo dự án
    def get_by_du_an(self, id_du_an: str):
        return self.repository.list_by_du_an(id_du_an)

    # 4. Phân công nhiệm vụ
    def assign_nhiem_vu(self, id: str, nguoi_thuc_hien: str):
        nv = self.repository.get_by_id(id)
        nv.nguoi_thuc_hien = nguoi_thuc_hien
        return self.repository.update(nv)

    # 5. Cập nhật trạng thái
    def update_status(self, id: str, trang_thai: str):
        nv = self.repository.get_by_id(id)
        nv.trang_thai = trang_thai
        return self.repository.update(nv)

    # 6. Xóa nhiệm vụ
    def delete_nhiem_vu(self, id: str):
        self.repository.delete(id)
