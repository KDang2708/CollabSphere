from abc import ABC, abstractmethod
from domain.models.Tin_Nhan.Tin_Nhan import TinNhan
class ITinNhanRepository(ABC):
    @abstractmethod
    def add(self, tin_nhan: TinNhan) -> TinNhan:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> TinNhan | None:
        pass