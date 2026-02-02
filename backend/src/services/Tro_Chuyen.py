from domain.models.Tin_Nhan.Tin_Nhan import TinNhan
from domain.models.Tin_Nhan.iTin_Nhan import ITinNhanRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Nhom.iNhom import INhomRepository
class TroChuyenLopUseCase():
    def __init__(self , nhom : INhomRepository , tin_nhan : ITinNhanRepository , sinh_vien : ISinhVienRepository , giang_vien : IGiangVienRepository , lop_hoc : ILopHocRepository):
        self.repo_tin_nhan = tin_nhan
        self.repo_sinh_vien = sinh_vien
        self.repo_giang_vien = giang_vien
        self.repo_lop_hoc = lop_hoc
        self.repo_nhom = nhom
    def nhan_tin(self , noi_dung : str , vai_tro_nguoi_gui :int , id_nguoi_gui : str , id_lop_hoc : str , id_nhom : str|None)->TinNhan:
        if vai_tro_nguoi_gui ==0:
            nguoi_gui = self.repo_sinh_vien.get_by_id(id_nguoi_gui)
        else:
            nguoi_gui = self.repo_giang_vien.get_by_id(id_nguoi_gui)
        lop_hoc = self.repo_lop_hoc.get_by_id(id_lop_hoc)
        tin_nhan = TinNhan(
            nguoi_gui=nguoi_gui,
            noi_dung=noi_dung,
            lop_hoc=lop_hoc,
            nhom=self.repo_nhom.get_by_id(id_nhom)
        )
        tin_nhan=self.repo_tin_nhan.add(tin_nhan)
        return tin_nhan
    def xem_tin_lop(self , id_lop_hoc : str)->list[TinNhan]:
        lop_hoc = self.repo_lop_hoc.get_by_id(id_lop_hoc)
        dsTN = self.repo_tin_nhan.get_tin_nhan_lop(lop_hoc)
        return dsTN
    def xem_tin_nhom(self , id_lop_hoc : str , id_nhom : str)->list[TinNhan]:
        nhom = self.repo_nhom.get_by_id(id_nhom)
        lop_hoc = self.repo_lop_hoc.get_by_id(id_lop_hoc)
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
