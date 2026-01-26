from abc import ABC, abstractmethod
from domain.models.Du_An.Du_An import DuAn
from typing import List, Optional
class IDuAn(ABC):
    @abstractmethod
    def add (self, du_an : DuAn)-> DuAn:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[DuAn]:
        pass

    @abstractmethod
    def get_all(self) -> List[DuAn]:
        pass

    # @abstractmethod
    # def set_lop(self) -> (self, du_an : DuAn , lop_hoc = LopHoc)->DuAn:
    #     pass


   
