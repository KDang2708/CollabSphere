from abc import ABC, abstractmethod
from domain.models.Cuoc_Hop.Cuoc_Hop import CuocHop
class ICuocHopRepository(ABC):
    @abstractmethod
    def add(self, cuoc_hop: CuocHop) -> CuocHop:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> CuocHop | None:
        pass