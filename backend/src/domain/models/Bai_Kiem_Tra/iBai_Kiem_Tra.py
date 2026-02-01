from abc import ABC, abstractmethod
from domain.models.Bai_Kiem_Tra.Bai_Kiem_Tra import BaiKiemTra
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
class IBaiKiemTraRepository(ABC):
    @abstractmethod
    def add(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        pass

    @abstractmethod
    def get_by_id(self, id_bai_kiem_tra: str) -> BaiKiemTra:
        pass
    @abstractmethod
    def get_by_mon_hoc(self , mon_hoc : MonHoc)->list[BaiKiemTra]:
        pass