from abc import ABC, abstractmethod
from domain.models.Nhom.Nhom import Nhom
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
class INhomRepository(ABC): 
    @abstractmethod
    def add(self, nhom: Nhom) -> Nhom:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> Nhom | None:
        pass
    @abstractmethod
    def get_nhom_theo_lop(self , id_lop : str)->list[Nhom]:
        pass
    @abstractmethod
    def add_sinh_vien(self, sinh_vien : SinhVien , nhom : Nhom)->bool:
        pass
    @abstractmethod
    def get_list_id_sinh_vien(self, nhom : Nhom)->list[str]:
        pass