from abc import ABC, abstractmethod
from domain.models.Truong_Khoa.Truong_Khoa import TruongKhoa

class ITruongKhoaRepository(ABC):
    @abstractmethod
    def add(self, truong_khoa: TruongKhoa) -> TruongKhoa:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> TruongKhoa | None:
        pass
