from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.baikiemtra import BaiKiemTra


class IBaiKiemTraRepository(ABC):

    @abstractmethod
    def them(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        pass

    @abstractmethod
    def lay_theo_id(self, id_bai_kiem_tra: str) -> Optional[BaiKiemTra]:
        pass

    @abstractmethod
    def lay_bat_buoc(self, id_bai_kiem_tra: str) -> BaiKiemTra:
        pass

    @abstractmethod
    def danh_sach_theo_du_an(self, id_du_an: str) -> List[BaiKiemTra]:
        pass

    @abstractmethod
    def cap_nhat(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        pass

    @abstractmethod
    def xoa(self, id_bai_kiem_tra: str) -> None:
        pass
