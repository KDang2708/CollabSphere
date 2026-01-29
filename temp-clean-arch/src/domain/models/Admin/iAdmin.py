# file này định nghĩa nguyên mẫu cho các nghiệp vụ liên quan đến tài khoản 
from abc import ABC, abstractmethod
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan
class ITaiKhoanRepository(ABC):
    @abstractmethod
    def add(self, tai_khoan: TaiKhoan) -> TaiKhoan:
        pass

    @abstractmethod
    def get_by_ten_dang_nhap(self, ten: str) -> TaiKhoan | None:
        pass
