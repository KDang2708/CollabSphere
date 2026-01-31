from abc import ABC, abstractmethod
from domain.models.Truong_Khoa.Truong_Khoa import TruongKhoa #lấy từ model TruongKhoa để sử dụng trong interface
class ITruongKhoaRepository(ABC):
    @abstractmethod
    def add(self, truong_khoa: TruongKhoa) -> TruongKhoa: # cú pháp -> TruongKhoa nghĩa là hàm này sẽ trả về một đối tượng TruongKhoa
        pass
#Hàm add là để thêm một đối tượng TruongKhoa mới vào kho lưu trữ và trả về đối tượng đã được thêm.
    @abstractmethod
    def get_by_id(self, id: str) -> TruongKhoa | None: #Hàm get_by_id là để lấy một đối tượng TruongKhoa từ kho lưu trữ dựa trên ID của nó. Nếu không tìm thấy, hàm sẽ trả về None.
        pass