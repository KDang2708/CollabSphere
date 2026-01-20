from abc import ABC, abstractmethod
from typing import List, Optional
from duan import DuAn
class IDuAnRepository(ABC):
    @abstractmethod
    def create_du_an(self, du_an: DuAn) -> DuAn:
        pass

    @abstractmethod
    def get_du_an_by_id(self, id: str) -> Optional[DuAn]:
        pass

    @abstractmethod
    def get_all_du_an(self) -> List[DuAn]:
        pass

    @abstractmethod
    def update_du_an(self, du_an: DuAn) -> DuAn:
        pass

    @abstractmethod
    def delete_du_an(self, id: str) -> None:
        pass