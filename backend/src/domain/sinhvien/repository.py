from abc import ABC, abstractmethod
from domain.sinhvien.model import SinhVien

class SinhVienRepository(ABC):

    @abstractmethod
    def save(self, sinh_vien: SinhVien):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> SinhVien:
        pass
