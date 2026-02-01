from domain.models.Nhom.Nhom import Nhom
from domain.models.Nhom.iNhom import INhomRepository
from infrastructure.models.Nhom_Model import NhomORM
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from sqlalchemy.orm import Session
from infrastructure.models.Nhom_Hoc_Sinh_Model import NhomHocSinhORM
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository

class NhomRepository(INhomRepository):
    def __init__(self, session : Session , sinh_vien : ISinhVienRepository ):
        self.session=session
        self.repo_sinh_vien = sinh_vien
    def get_nhom_theo_lop(self, lop : LopHoc)->list[Nhom]:
        orm_list = self.session.query(NhomORM).filter(NhomORM.id_lop_hoc == lop.id).all()
        dsN = [Nhom(id=o.id) for o in orm_list]
        return dsN
    
    def add(self, nhom: Nhom)->Nhom:
        orm = NhomORM(
            id_lop_hoc = nhom.lop_hoc.id 
        )
        self.session.add(orm)
        nhom.id=orm.id
        self.session.commit()
        return nhom
    def add_sinh_vien(self, sinh_vien : SinhVien , nhom : Nhom)->bool:
        orm = NhomHocSinhORM(
            id_nhom = nhom.id,
            id_sinh_vien = sinh_vien.id
        )
        self.session.add(orm)
        self.session.commit()
        return True
    def get_list_id_sinh_vien(self, nhom : Nhom)->list[str]:
        orm = self.session.query(NhomHocSinhORM).filter(NhomHocSinhORM.id_nhom==nhom.id).all()
        return [o.id_sinh_vien for o in orm ]