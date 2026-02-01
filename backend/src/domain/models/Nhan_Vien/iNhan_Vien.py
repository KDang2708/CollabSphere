from abc import ABC, abstractmethod
from domain.models.Nhan_Vien.Nhan_Vien import NhanVien
class INhanVienRepository(ABC):
    @abstractmethod
    def add(self, nhan_vien: NhanVien) -> NhanVien:
        pass
#hàm add là hàm của thư viện abc (abstract base class) trong Python, được sử dụng để định nghĩa một phương thức trừu tượng trong một lớp cơ sở trừu tượng.
    @abstractmethod
    def get_by_id(self, id: str) -> NhanVien | None:
        pass