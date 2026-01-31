from abc import ABC, abstractmethod
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc

class ILopHocRepository(ABC):

    @abstractmethod
    def add(self, lop_hoc: LopHoc) -> LopHoc:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> LopHoc | None:
        pass
