from domain.models.Tin_Nhan.Tin_Nhan import TinNhan
from domain.models.Tin_Nhan.iTin_Nhan import ITinNhanRepository
from infrastructure.models.Tin_Nhan_Model import TinNhanORM
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from sqlalchemy.orm import Session
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Tai_Khoan.Vai_Tro import VaiTro

class TinNhanRepository(ITinNhanRepository):
    def __init__(self , session : Session , giang_vien : IGiangVienRepository , sinh_vien : ISinhVienRepository , lop_hoc : ILopHocRepository):
        self.session = session
        self.repo_giang_vien = giang_vien
        self.repo_sinh_vien = sinh_vien
        self.repo_lop_hoc = lop_hoc
    def add(self, tin_nhan : TinNhan)->TinNhan:
        orm = TinNhanORM(
            id_nguoi_gui = tin_nhan.nguoi_gui.id,
            noi_dung = tin_nhan.noi_dung,
            vai_tro_nguoi_gui = tin_nhan.nguoi_gui.tai_khoan.vai_tro,
            id_lop_hoc = tin_nhan.lop_hoc.id,
            id_nhom = tin_nhan.nhom.id
        )
        self.session.add(orm)
        self.session.flush()
        tin_nhan.id = orm.id
        tin_nhan.thoi_gian_gui=orm.thoi_gian_gui
        self.session.commit()
        return tin_nhan
    def get_tin_nhan_lop(self, lop_hoc:LopHoc)->list[TinNhan]:
        orm_list = self.session.query(TinNhanORM).filter(TinNhanORM.id_lop_hoc==lop_hoc.id , TinNhanORM.id_nhom==None).order_by(TinNhanORM.thoi_gian_gui.asc()).all()
        dsTN :list[TinNhan] = []
        for orm in orm_list:
            if orm.vai_tro_nguoi_gui == VaiTro.GIANG_VIEN:
                nguoi_gui = self.repo_giang_vien.get_by_id(orm.id_nguoi_gui)
            else:
                nguoi_gui = self.repo_sinh_vien.get_by_id(orm.id_nguoi_gui)
            tin_nhan = TinNhan(
                id=orm.id,
                noi_dung=orm.noi_dung,
                nguoi_gui=nguoi_gui,
                lop_hoc=lop_hoc,
                thoi_gian_gui=orm.thoi_gian_gui
            ) 
            dsTN.append(tin_nhan)
        return dsTN

    def get_tin_nhan_nhom(self, lop_hoc : LopHoc, nhom : Nhom)->list[TinNhan]:
        orm_list = self.session.query(TinNhanORM).filter(TinNhanORM.id_lop_hoc == lop_hoc.id , TinNhanORM.id_nhom == nhom.id).order_by(TinNhanORM.thoi_gian_gui.asc()).all()
        dsTN: list[TinNhan] = []
        for orm in orm_list:
            if orm.vai_tro_nguoi_gui == VaiTro.GIANG_VIEN:
                nguoi_gui = self.repo_giang_vien.get_by_id(orm.id_nguoi_gui)
            else:
                nguoi_gui = self.repo_sinh_vien.get_by_id(orm.id_nguoi_gui)

            tin_nhan = TinNhan(
                id=orm.id,
                noi_dung=orm.noi_dung,
                nguoi_gui=nguoi_gui,
                lop_hoc=lop_hoc,
                nhom=nhom,
                thoi_gian_gui=orm.thoi_gian_gui
            )
            dsTN.append(tin_nhan)
            return dsTN
        
    # id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))            # cột ID, kiểu String, là khóa chính
    # id_nguoi_gui = Column(String)                     # cột ID người gửi, kiểu String
    # vai_tro_nguoi_gui 
    # thoi_gian_gui = Column(DateTime, server_default=func.now())                  # cột thời gian gửi, kiểu DateTime
    # id_lop_hoc = Column(String)                       # cột ID lớp học liên kết, kiểu String
    # id_nhom = Column(String, nullable=True)     