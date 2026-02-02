from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from infrastructure.models.Du_An_Model import DuAnORM
from sqlalchemy.orm import Session
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository

class DuAnRepository(IDuAn):
    def __init__(self, session : Session , giang_vien : IGiangVienRepository , lop_hoc : ILopHocRepository):
        self.session = session
        self.repo_giang_vien = giang_vien
        self.repo_lop_hoc = lop_hoc

    def add(self, du_an : DuAn)-> DuAn:
        orm = DuAnORM(
            noi_dung = du_an.noi_dung,
            id_nguoi_tao = du_an.nguoi_tao
        )
        self.session.add(orm)
        du_an.id = orm.id
        du_an.trang_thai = orm.trang_thai
        return du_an
    def set_lop(self, du_an : DuAn, lop_hoc : LopHoc)->DuAn:
        orm = self.session.query(DuAnORM).filter(DuAnORM.id == du_an.id).first()
        if orm is None:
            raise Exception("Dự án không tồn tại")
        orm.id_lop_hoc = lop_hoc.id
        du_an.lop_hoc = lop_hoc
        self.session.commit()
        return du_an
    def get_all(self)->list[DuAn]:
        orm_list = self.session.query(DuAnORM).all()
        return [
            DuAn(
                id = orm.id,
                trang_thai = orm.trang_thai,
                noi_dung = orm.noi_dung,
                nguoi_tao = self.repo_giang_vien.get_by_id(orm.id_nguoi_tao),
                lop_hoc = self.repo_lop_hoc.get_by_id(orm.id_lop_hoc)
            )
            for orm in orm_list
        ]

    def duyet_du_an(self, du_an : DuAn)->DuAn:
        orm = self.session.query(DuAnORM).filter(DuAnORM.id == du_an.id).first()
        if orm is None:
            raise Exception("Dự án không tồn tại !")
        orm.trang_thai = True
        du_an.trang_thai = orm.trang_thai
        self.session.commit()
        return du_an
    def huy_duyet_du_an(self, du_an: DuAn)->DuAn:
        orm = self.session.query(DuAnORM).filter(DuAnORM.id==du_an.id).first()
        if orm is None:
            raise Exception("Dự án không tồn tại !")
        orm.trang_thai = False
        du_an.trang_thai = orm.trang_thai
        self.session.commit()
        return du_an
    def get_by_id(self, id_du_an : str)->DuAn:
        orm = self.session.query(DuAnORM).filter(DuAnORM.id == id_du_an).first()
        if orm is None:
            raise Exception("Id dự án không tồn tại !")
        nguoi_tao = self.repo_giang_vien(orm.id_nguoi_tao)
        lop_hoc = self.repo_lop_hoc(orm.id_lop_hoc)
        return DuAn(
            id=orm.id,
            noi_dung=orm.noi_dung,
            nguoi_tao = nguoi_tao,
            lop_hoc=lop_hoc,
            trang_thai=orm.trang_thai
        )