from abc import ABC, abstractmethod
from typing import List, Optional
from baikiemtra import BaiKiemTra

class IBaiKiemTraRepository(ABC):
    @abstractmethod
    def create_bai_kiem_tra(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        pass

    @abstractmethod
    def get_bai_kiem_tra_by_id(self, id: int) -> Optional[BaiKiemTra]:
        pass

    @abstractmethod
    def get_all_bai_kiem_tra(self) -> List[BaiKiemTra]:
        pass

    @abstractmethod
    def update_bai_kiem_tra(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        pass

    @abstractmethod
    def delete_bai_kiem_tra(self, id: int) -> None:
        pass