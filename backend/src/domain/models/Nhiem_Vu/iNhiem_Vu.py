from abc import ABC, abstractmethod
from domain.models.Nhiem_Vu.Nhiem_Vu import NhiemVu
class INhiemVuRepository(ABC):
    @abstractmethod
    def add(self, nhiem_vu: NhiemVu) -> NhiemVu:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> NhiemVu :
        pass