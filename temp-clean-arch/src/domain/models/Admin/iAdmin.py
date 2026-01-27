from abc import ABC, abstractmethod
from domain.models.admin import Admin

class IAdmin(ABC):

    @abstractmethod
    def get_by_id(self, admin_id: str) -> Admin:
        pass
