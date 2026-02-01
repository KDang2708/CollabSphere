from domain.models.Moc_Quan_Trong.Moc_Quan_Trong import MocQuanTrong
from domain.models.Moc_Quan_Trong.iMoc_Quan_trong import IMocQuanTrongRepository
from infrastructure.models.Moc_Quan_trong_Model import MocQuanTrongORM
from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from sqlalchemy.orm import Session

class MocQuanTrongRepository(IMocQuanTrongRepository):
    def __init__(self , session : Session ):
        self.session = session
    def get_by_mon_hoc(self, mon_hoc : MonHoc)->list[MocQuanTrong]:
        orm = self.session.query(MocQuanTrongORM).filter(MocQuanTrongORM.id_mon_hoc == mon_hoc.id).all()
        return [ MocQuanTrong(
            noi_dung= o.noi_dung,
            mon_hoc=mon_hoc,
            id=o.id,
            loai_moc=o.loai_moc
        )
        for o in orm 
        ]
    def add(self, moc_quan_trong : MocQuanTrong)->MocQuanTrong:
        orm = MocQuanTrongORM(
            noi_dung = moc_quan_trong.noi_dung,
            id_mon_hoc = moc_quan_trong.mon_hoc.id,
            loai_moc = moc_quan_trong.loai_moc
        )
        self.session.add(orm)
        self.session.flush()
        moc_quan_trong.id=orm.id
        self.session.commit()
        return moc_quan_trong
    
    # id = Column(String, primary_key=True)      # cột ID, kiểu String, là khóa chính
    # noi_dung = Column(String)                   # cột nội dung mốc quan trọng, kiểu String
    # id_mon_hoc = Column(String)                 # cột ID môn học liên kết, kiểu String
    # loai_moc = Column(String)                   # cột loại mốc quan trọng, kiểu String
    