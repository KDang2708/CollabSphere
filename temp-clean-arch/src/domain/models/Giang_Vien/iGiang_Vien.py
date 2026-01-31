from abc import ABC, abstractmethod
from domain.models.Giang_Vien.Giang_Vien import GiangVien

class IGiangVien(ABC):

    @abstractmethod
    def add(self, giang_vien:GiangVien)->GiangVien:
        pass

    @abstractmethod
    def get_id_by(self, id:str)->GiangVien:
        pass
