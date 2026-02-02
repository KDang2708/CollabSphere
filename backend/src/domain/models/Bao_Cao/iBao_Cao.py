from abc import ABC, abstractmethod
from domain.models.Bao_Cao.Bao_Cao import BaoCao
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Nhan_Vien.Nhan_Vien import NhanVien
from domain.models.Truong_Khoa.Truong_Khoa import TruongKhoa
from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
class IBaoCaoRepository(ABC):
    @abstractmethod
    def add(self, bao_cao: BaoCao) -> BaoCao:
        pass
    @abstractmethod
    def get_all(self) -> list[BaoCao]:
        pass
    @abstractmethod
    def get_by_id(self,id:str)->BaoCao:
        pass
    @abstractmethod
    def set_phan_hoi(self, bao_cao : BaoCao , phan_hoi : PhanHoi )->BaoCao:
        pass