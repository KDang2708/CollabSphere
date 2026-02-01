from abc import ABC, abstractmethod
from domain.taikhoan.model import TaiKhoan

class TaiKhoanRepository(ABC):

    @abstractmethod
    def save(self, tai_khoan: TaiKhoan):
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> TaiKhoan:
        pass
