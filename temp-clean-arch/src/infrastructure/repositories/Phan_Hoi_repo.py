from sqlalchemy.orm import Session
from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
from domain.models.Phan_Hoi.iPhan_Hoi import IPhanHoiRepository
from infrastructure.models.Phan_Hoi_Model import PhanHoiORM
 
class PhanHoiRepository(IPhanHoiRepository):
    def __init__(self, session: Session):
        self.session=session
    def add(self, phan_hoi : PhanHoi)->PhanHoi:
        orm = PhanHoiORM(
            noi_dung = phan_hoi.noi_dung,
            id_bao_cao = phan_hoi.bao_cao.id
        )
        self.session.add(orm)
        self.session.flush()
        phan_hoi.id=orm.id
        phan_hoi.ngay_gui=orm.ngay_gui
        self.session.commit()
        return phan_hoi
