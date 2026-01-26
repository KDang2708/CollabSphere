from abc import ABC, abstractmethod
from domain.models.Moc_Quan_Trong.Moc_Quan_Trong import MocQuanTrong
class IMocQuanTrongRepository(ABC):
    @abstractmethod
    def add(self, moc_quan_trong: MocQuanTrong) -> MocQuanTrong:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> MocQuanTrong:
        pass