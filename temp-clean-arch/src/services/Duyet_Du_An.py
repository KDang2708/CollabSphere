from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from domain.models.Truong_Khoa.Truong_Khoa import TruongKhoa
from services.Duyet_Du_An import XemDuAnUseCase

from typing import List, Optional

class DuyetDuAnService:
    def __init__(self, repository: IDuAn):
        self.repository = repository
        self.xem_du_an_uc = XemDuAnUseCase(repository)

    # Lấy danh sách dự án
    def xem_du_an(self) -> List[DuAn]:
        return self.xem_du_an_uc.execute()
    # Trưởng khoa DUYỆT dự án
    def duyet_du_an(
        self,
        truong_khoa: TruongKhoa,
        du_an_id: str
    ) -> Optional[DuAn]:
         
        if truong_khoa is None:
            raise Exception("Trưởng khoa không hợp lệ")
        return self.repository.update_trang_thai(
            id=du_an_id,
            trang_thai=True
        )

    # Trưởng khoa HỦY DUYỆT dự án
    def huy_duyet_du_an(
        self,
        truong_khoa: TruongKhoa,
        du_an_id: str
    ) -> Optional[DuAn]:

        du_an = self.repository.get_by_id(du_an_id)
        if not du_an:
            return None

        du_an.trang_thai = False
        return du_an
