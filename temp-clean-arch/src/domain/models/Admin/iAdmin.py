# file này định nghĩa nguyên mẫu cho các nghiệp vụ liên quan đến tài khoản 
from abc import ABC, abstractmethod
from domain.models.Admin.Admin import Admin
class IAdminRepository(ABC):
    @abstractmethod
    def add(self, admin : Admin) -> Admin:
        pass

    @abstractmethod
    def get_by_id(self, id_admin: str) -> Admin:
        pass
    