from abc import ABC, abstractmethod
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
class ILopHocRepository(ABC):
    @abstractmethod
    def add(self, lop_hoc: LopHoc) -> LopHoc:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> LopHoc | None:
        pass
    @abstractmethod
    def add_sinh_vien(self  , lop_hoc : LopHoc , sinh_vien : SinhVien):
        pass
    @abstractmethod
    def get_sinh_vien(self , lop_hoc : LopHoc)-> list[SinhVien]:
        pass
    @abstractmethod
    def get_all(self)->list[LopHoc]:
        pass
    @abstractmethod
    def get_lop_by_sinh_vien(self , sinh_vien : SinhVien)->list[LopHoc]:
        pass