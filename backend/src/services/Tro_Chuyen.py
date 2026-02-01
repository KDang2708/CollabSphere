from domain.models.Tin_Nhan.Tin_Nhan import TinNhan
from domain.models.Tin_Nhan.iTin_Nhan import ITinNhanRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom

class TroChuyenLopUseCase():
    def __init__(self , tin_nhan : ITinNhanRepository):
        self.repo_tin_nhan = tin_nhan
    def nhan_tin(self , noi_dung : str, nguoi_gui : SinhVien |GiangVien , lop_hoc : LopHoc , nhom : Nhom|None)->TinNhan:
        tin_nhan = TinNhan(
            nguoi_gui=nguoi_gui,
            noi_dung=noi_dung,
            lop_hoc=lop_hoc,
            nhom=nhom
        )
        tin_nhan=self.repo_tin_nhan.add(tin_nhan)
        return tin_nhan
    def xem_tin_lop(self , lop_hoc : LopHoc)->list[TinNhan]:
        dsTN = self.repo_tin_nhan.get_tin_nhan_lop(lop_hoc)
        return dsTN
    def xem_tin_nhom(self , lop_hoc : LopHoc , nhom : Nhom)->list[TinNhan]:
        dsTN = self.repo_tin_nhan.get_tin_nhan_nhom(lop_hoc , nhom)
        return dsTN



    # class TinNhan:
    # def __init__(self, id : str | None, nguoi_gui: TaiKhoan ,noi_dung : str, thoi_gian_gui: datetime | None, lop_hoc: LopHoc , nhom: Nhom | None):
    #     self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
    #     self.noi_dung = noi_dung
    #     self.nguoi_gui = nguoi_gui
    #     self.thoi_gian_gui = thoi_gian_gui
    #     self.lop_hoc = lop_hoc
    #     self.nhom = nhom
