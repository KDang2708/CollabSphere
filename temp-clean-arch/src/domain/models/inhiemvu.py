from abc import ABC, abstractmethod
from typing import List, Optional
from nhiemvu import NhiemVu


class INhiemVuRepository(ABC):

    @abstractmethod
    def create_nhiem_vu(self, nhiem_vu: NhiemVu) -> NhiemVu:
        pass

    @abstractmethod
    def get_nhiem_vu_by_id(self, id: str) -> Optional[NhiemVu]:
        pass

    @abstractmethod
    def get_all_nhiem_vu_by_du_an(self, id_du_an: str) -> List[NhiemVu]:
        pass

    @abstractmethod
    def update_nhiem_vu(self, nhiem_vu: NhiemVu) -> NhiemVu:
        pass

    @abstractmethod
    def delete_nhiem_vu(self, id: str) -> None:
        pass
