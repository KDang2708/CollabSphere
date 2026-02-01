from domain.models.Nhan_Xet.Nhan_Xet import NhanXet
from domain.models.Nhan_Xet.iNhan_Xet import INhanXetRepository
from infrastructure.models.Nhan_Xet_Model import NhanXetORM
from sqlalchemy.orm import Session

class NhanXetRepository(INhanXetRepository):
    def __init__(self , session : Session):
        self.session = session
    def add(self, nhan_xet : NhanXet)->NhanXet:
        orm = NhanXetORM(
            noi_dung_nhan_xet = nhan_xet.noi_dung_nhan_xet,
            id_giang_vien = nhan_xet.giang_vien_nhan_xet.id,
            id_bai_lam = nhan_xet.bai_lam.id
        )
        self.session.add(orm)
        self.session.flush()
        nhan_xet.id = orm.id
        self.session.commit()
        return nhan_xet
    

    # class NhanXetORM(Base):
    # __tablename__ = "nhan_xet"

    # id = Column(String , primary_key=True , default=lambda : str(uuid.uuid4()))
    # noi_dung_nhan_xet = Column(String)
    # id_giang_vien = Column(String , ForeignKey("giang_vien"))
    # id_bai_lam = Column(String, ForeignKey("bai_lam"))