from abc import ABC, abstractmethod
from domain.models.Cuoc_Hop.Cuoc_Hop import CuocHop
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
class ICuocHopRepository(ABC):
    @abstractmethod
    def add(self, cuoc_hop: CuocHop) -> CuocHop:
        pass

    @abstractmethod
    def get_cuoc_hop_by_lop_hoc(self, lop_hoc : LopHoc) -> list[CuocHop]|None:
        pass
    @abstractmethod
    def get_cuoc_hop_by_nhom(self , lop_hoc : LopHoc , nhom :Nhom )->list[CuocHop]|None:
        pass