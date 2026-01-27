from abc import ABC, abstractmethod
from domain.models.baikiemtra import BaiKiemTra

class IBaiKiemTra(ABC):

    @abstractmethod
    def get_by_id(self, id: str) -> BaiKiemTra:
        pass
