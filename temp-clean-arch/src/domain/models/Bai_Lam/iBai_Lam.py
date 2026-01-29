from abc import ABC, abstractmethod
from domain.models.Bai_Lam.Bai_Lam import BaiLam
class IBaiLamRepository(ABC):
    @abstractmethod
    def add(self, bai_lam: BaiLam) -> BaiLam:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> BaiLam | None:
        pass