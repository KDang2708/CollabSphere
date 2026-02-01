from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from infrastructure.models.Lop_Hoc_Model import LopHocORM
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from infrastructure.models.Lop_Hoc_Hoc_Sinh_Model import LopHocHocSinhORM
from infrastructure.models.Sinh_Vien_Model import SinhVienORM
from sqlalchemy.orm import Session 
from domain.models.Nhom.Nhom import Nhom

class LopHocRepository(ILopHocRepository):
    def __init__(self,session : Session, tai_khoan : ITaiKhoanRepository , mon_hoc : IMonHocRepository , sinh_vien : ISinhVienRepository , lop_hoc : ILopHocRepository ):
        self.session = session
        self.repo_tai_khoan= tai_khoan
        self.repo_mon_hoc = mon_hoc
        self.repo_sinh_vien = sinh_vien
        self.repo_lop_hoc = lop_hoc
    def add(self , lop_hoc : LopHoc  )->LopHoc:
        orm = LopHocORM(
            id_mon_hoc = lop_hoc.mon_hoc.id,
            id_giang_vien = lop_hoc.giang_vien.id
        )
        self.session.add(orm)
        self.session.commit()
        return self._to_domain(orm)
    
    def _to_domain(self, orm: LopHocORM) -> LopHoc:
        return LopHoc(
            id=orm.id,
            mon_hoc=self.repo_mon_hoc.get_by_id(orm.id_mon_hoc),
            giang_vien=self.repo_tai_khoan.get_by_id(orm.id_giang_vien)
        )
    
    # def add_sinh_vien(self, sinh_vien : SinhVien , lop_hoc : LopHoc):
    #     orm = LopHocHocSinhORM (
    #         id_sinh_vien = sinh_vien.id,
    #         id_lop_hoc = lop_hoc.id
    #     )
    #     self.session.add(orm)
    #     self.session.commit()
        
    def get_sinh_vien(self , lop_hoc : LopHoc)->list[SinhVien]:
        orm =  self.session.query(LopHocHocSinhORM).filter( LopHocHocSinhORM.id_lop_hoc == lop_hoc.id).all()
        dsSV : list[SinhVien] = [self.repo_sinh_vien.get_by_id(o.id_sinh_vien) for o in orm]
        return dsSV
    
    def get_by_id(self, id:str)->LopHoc:
        orm = self.session.query(LopHocORM).filter_by(id=id).first()
        #lấy ra danh sách học sinh !
        #orm_list_hoc_sinh = self.session.query(LopHocHocSinhORM).filter(LopHocHocSinhORM.id_lop_hoc==id).all()
        if orm is None:
            return None
        return LopHoc(
            id=id ,
            giang_vien=self.repo_tai_khoan.get_by_id(orm.id_giang_vien), 
            mon_hoc=self.repo_mon_hoc.get_by_id(orm.id_mon_hoc), 
        )
    
    def add_sinh_vien(self, lop_hoc: LopHoc, sinh_vien : SinhVien) -> None:
    # kiểm tra cso sinh viên ko 
        checkSV = (
            self.session.query(SinhVienORM).filter(SinhVienORM.id== sinh_vien.id).first()
        )
        if checkSV==None:
            raise Exception("Không tồn tại sinh viên")
    # check đã tồn tại chưa
        existed = (
            self.session.query(LopHocHocSinhORM)
            .filter(
                LopHocHocSinhORM.id_lop_hoc == lop_hoc.id,
                LopHocHocSinhORM.id_sinh_vien == checkSV.id
            )
            .first()
        )

        if existed:
            raise Exception("Sinh viên đã tồn tại trong lớp học")

        orm = LopHocHocSinhORM(
            id_sinh_vien=checkSV.id,
            id_lop_hoc=lop_hoc.id
        )

        self.session.add(orm)
        self.session.commit()

    def get_all(self) -> list[LopHoc]:
        orm_list = self.session.query(LopHocORM).all()
        return [self._to_domain(o) for o in orm_list]
    
    def get_lop_by_sinh_vien(self , sinh_vien : SinhVien)->list[LopHoc]:
        orm_list = self.session.query(LopHocHocSinhORM).filter(LopHocHocSinhORM.id_sinh_vien == sinh_vien.id).all()
        list = [self.repo_lop_hoc.get_by_id(orm.id_lop_hoc) for orm in orm_list]
        return list
        
    