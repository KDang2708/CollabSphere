from abc import ABC, abstractmethod
from domain.models.Du_An.Du_An import DuAn
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc

class IDuAn(ABC):
    @abstractmethod
    def add(self, du_an: DuAn) -> DuAn:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> DuAn | None:
        pass
    @abstractmethod
    def set_lop(self , du_an : DuAn , lop_hoc : LopHoc )->DuAn:
        pass
    @abstractmethod
    def get_all(self)->list[DuAn]:
        pass
    @abstractmethod
    def duyet_du_an(self , du_an : DuAn)->DuAn:
        pass
    @abstractmethod
    def huy_duyet_du_an(self , du_an : DuAn)->DuAn:
        pass