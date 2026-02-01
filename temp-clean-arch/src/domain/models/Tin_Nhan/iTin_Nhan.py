from abc import ABC, abstractmethod
from domain.models.Tin_Nhan.Tin_Nhan import TinNhan
from domain.models.Lop_Hoc.iLop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
class ITinNhanRepository(ABC):
    @abstractmethod
    def add(self, tin_nhan: TinNhan) -> TinNhan:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> TinNhan | None:
        pass
    @abstractmethod
    def get_tin_nhan_lop(self, lop_hoc : LopHoc )->list[TinNhan]:
        pass
    @abstractmethod
    def get_tin_nhan_nhom(self , lop_hoc : LopHoc , nhom : Nhom)->list[TinNhan]:
        pass