from domain.models.Cuoc_Hop.Cuoc_Hop import CuocHop
from domain.models.Cuoc_Hop.iCuoc_Hop import ICuocHopRepository
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from datetime import datetime

class HopUseCase():
    def __init__(self , cuoc_hop : ICuocHopRepository):
        self.repo_cuoc_hop = cuoc_hop
    def xem_danh_sach_hop_lop(self, lop_hoc :LopHoc)->list[CuocHop]:
        return self.repo_cuoc_hop.get_cuoc_hop_by_lop(lop_hoc)
    def xem_danh_sach_hop_nhom(self, lop_hoc: LopHoc, nhom: Nhom) -> list[CuocHop]:
        return self.repo_cuoc_hop.get_cuoc_hop_by_nhom(lop_hoc, nhom)
    def them_cuoc_hop(self,thoi_gian_bat_dau: datetime,nguoi_tao,lop_hoc: LopHoc,nhom: Nhom | None) -> CuocHop:
        cuoc_hop = CuocHop(
            thoi_gian_bat_dau=thoi_gian_bat_dau,
            nguoi_tao=nguoi_tao,
            lop_hoc=lop_hoc,
            nhom=nhom
        )

        return self.repo_cuoc_hop.add(cuoc_hop)