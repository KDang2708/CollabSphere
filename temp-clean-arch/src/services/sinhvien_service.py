from domain.sinhvien.model import SinhVien
from domain.sinhvien.repository import SinhVienRepository


class SinhVienService:
    def __init__(self, sinh_vien_repository: SinhVienRepository):
        self.sinh_vien_repository = sinh_vien_repository

    def tao_sinh_vien(self, id_sinh_vien: str, ten_sinh_vien: str) -> SinhVien:
        sinh_vien = SinhVien(
            id_sinh_vien=id_sinh_vien,
            ten_sinh_vien=ten_sinh_vien
        )

        self.sinh_vien_repository.save(sinh_vien)
        return sinh_vien

    def lay_sinh_vien_theo_id(self, id_sinh_vien: str) -> SinhVien:
        return self.sinh_vien_repository.get_by_id(id_sinh_vien)
