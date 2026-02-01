from abc import ABC, abstractmethod
from domain.models.Giang_Vien.Giang_Vien import GiangVien
class IGiangVienRepository(ABC):
    @abstractmethod
    def add(self, giang_vien: GiangVien) -> GiangVien:
        pass

    @abstractmethod
    def get_by_id(self, id_giang_vien: str) -> GiangVien:
        pass