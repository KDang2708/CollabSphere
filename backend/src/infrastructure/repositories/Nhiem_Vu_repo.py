from domain.models.Nhiem_Vu.iNhiem_Vu import INhiemVuRepository
from domain.models.Nhiem_Vu.Nhiem_Vu import NhiemVu
from infrastructure.models.Nhiem_Vu_Model import NhiemVuORM
from sqlalchemy.orm import Session
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository

class NhiemVuRepository(INhiemVuRepository):
    def __init__(self , session : Session , sinh_vien : ISinhVienRepository , giang_vien : IGiangVienRepository):
        self.session = session
        self.repo_sinh_vien = sinh_vien
        self.repo_giang_vien = giang_vien
    def get_by_id(self, id_nhiem_vu : str)->NhiemVu:
        orm = self.session.query(NhiemVuORM).filter(NhiemVuORM.id == id_nhiem_vu).first()
        if orm.vai_tro_nguoi_tao == 0 :
            nguoi_tao = self.repo_sinh_vien.get_by_id(orm.id_nguoi_tao) # viết thêm hàm get_by_id
        elif orm.id_nguoi_tao == 1:
            nguoi_tao = self.repo_giang_vien.get_by_id(orm.id_nguoi_tao) # viết thêm hàm get_by_id
        return NhiemVu(
            id = orm.id,
            noi_dung=orm.noi_dung,
            id_nguoi_thuc_hien=orm.id_nguoi_thuc_hien,
            id_nguoi_tao= orm.id_nguoi_tao,
            vai_tro_nguoi_tao=orm.vai_tro_nguoi_tao,
            ngay_bat_dau=  orm.ngay_bat_dau,
            ngay_ket_thuc=orm.ngay_ket_thuc
        )

    def add(self, nhiem_vu : NhiemVu)->NhiemVu:
        orm = NhiemVuORM(
            noi_dung = nhiem_vu.noi_dung,
            id_nguoi_thuc_hien = nhiem_vu.nguoi_thuc_hien.id,
            id_nguoi_tao = nhiem_vu.nguoi_tao.id,
            vai_tro_nguoi_tao = nhiem_vu.nguoi_tao.tai_khoan.vai_tro,
            ngay_bat_dau = nhiem_vu.ngay_bat_dau,
            ngay_ket_thuc = nhiem_vu.ngay_ket_thuc
        )
        self.session.add(orm)
        self.session.flush()
        nhiem_vu.id = orm.id
        self.session.commit()
        return nhiem_vu


# from datetime import date
# from domain.models.Giang_Vien.Giang_Vien import GiangVien
# from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh
# class NhiemVu:
#     def __init__(self, id_nguoi_thuc_hien: HocSinh, ngay_bat_dau: date, ngay_ket_thuc: date, id_nguoi_tao: GiangVien | HocSinh):
#         self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.id_nguoi_thuc_hien = id_nguoi_thuc_hien
#         self.noi_dung = noi_dung
#         self.ngay_bat_dau = ngay_bat_dau
#         self.ngay_ket_thuc = ngay_ket_thuc
#         self.id_nguoi_tao = id_nguoi_tao