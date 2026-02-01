from abc import ABC, abstractmethod
from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
class IPhanHoiRepository(ABC):
    @abstractmethod
    def add(self, phan_hoi: PhanHoi) -> PhanHoi:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> PhanHoi | None:
        pass