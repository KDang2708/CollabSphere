from domain.models.Mon_Hoc.Mon_Hoc import MonHoc
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository
from infrastructure.models.Mon_Hoc_Model import MonHocORM
from sqlalchemy.orm import Session

class MonHocRepositoty(IMonHocRepository):
    def __init__(self,session : Session ):
        self.session = session
        
    def add(self, mon_hoc : MonHoc)->MonHoc:
        orm = MonHocORM(
            ten = mon_hoc.ten,
            de_cuong = mon_hoc.de_cuong,
            tin_chi = mon_hoc.tin_chi
        )
        self.session.add(orm)
        self.session.commit()
        return MonHoc(id=orm.id,ten=orm.ten,tin_chi=orm.tin_chi,de_cuong=orm.de_cuong)
    
    def get_all(self)->list[MonHoc]:
        orm_list : list[MonHocORM] = self.session.query(MonHocORM).all()
        return [
            self._to_domain(orm)
            for orm in orm_list
        ]
    
    def _to_domain(self, orm: MonHocORM) -> MonHoc:
        return MonHoc(
            id=orm.id,
            ten=orm.ten,
            tin_chi=orm.tin_chi,
            de_cuong=orm.de_cuong
        )
    def get_by_id(self, id_mon_hoc : str)->MonHoc:
        orm = self.session.query(MonHocORM).filter(MonHocORM.id == id_mon_hoc).first()
        return MonHoc(
            id=orm.id,
            ten=orm.ten,
            tin_chi=orm.tin_chi,
            de_cuong=orm.de_cuong
        )