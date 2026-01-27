from typing import List, Optional
from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
import uuid

class DuAnService:
    def __init__(self, repository: IDuAn):
        self.repository = repository

    def create_du_an(
        self,
        noi_dung: str,
        nguoi_tao: GiangVien,
        lop_hoc: LopHoc
    ) -> DuAn:
        du_an = DuAn(
            id=str(uuid.uuid4()),
            noi_dung=noi_dung,
            trang_thai=False,   # mặc định chưa duyệt
            nguoi_tao=nguoi_tao,
            lop_hoc=lop_hoc
        )
        return self.repository.add(du_an)

    def get_by_id(self, id: str) -> Optional[DuAn]:
        return self.repository.get_by_id(id)

    def get_all(self) -> List[DuAn]:
        return self.repository.get_all()

    def duyet(self, id: str) -> Optional[DuAn]:
        du_an = self.repository.get_by_id(id)
        if not du_an:
            return None
        du_an.trang_thai = True
        return du_an
