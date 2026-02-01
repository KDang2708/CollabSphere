from abc import ABC, abstractmethod
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
class ISinhVienRepository(ABC):
    @abstractmethod
    def add(self, sinh_vien: SinhVien) -> SinhVien:
        pass

    @abstractmethod
    def get_by_id(self, id_sinh_vien: str) -> SinhVien:
        pass
