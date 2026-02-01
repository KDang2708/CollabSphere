from abc import ABC, abstractmethod
from domain.models.Nhan_Xet.Nhan_Xet import NhanXet
class INhanXetRepository(ABC):
    @abstractmethod
    def add(self, nhan_xet: NhanXet) -> NhanXet:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> NhanXet | None:
        pass