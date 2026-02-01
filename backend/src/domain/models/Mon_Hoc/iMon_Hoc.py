from abc import ABC, abstractmethod
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
class IMonHocRepository(ABC):
    @abstractmethod
    def add(self, mon_hoc: MonHoc) -> MonHoc:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> MonHoc | None:
        pass
    @abstractmethod
    def get_all(self)->list[MonHoc]:
        pass