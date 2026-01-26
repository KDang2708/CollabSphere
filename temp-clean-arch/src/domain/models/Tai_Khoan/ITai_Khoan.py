from abc import ABC, abstractmethod
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan

class ITaiKhoanRepository(ABC):
    @abstractmethod
    def add(self, tai_khoan: TaiKhoan) -> TaiKhoan:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> TaiKhoan | None:
        pass
    @abstractmethod
    def get_by_username(self, username: str) -> TaiKhoan | None:
        pass
    @abstractmethod
    def get_all(self)->list[TaiKhoan]:
        pass
    @abstractmethod
    def change(self , id_tai_khoan : str):
        pass
    @abstractmethod
    def update(self , tai_khoan : TaiKhoan)->None:
        pass