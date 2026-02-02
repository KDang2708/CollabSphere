from domain.models.Bao_Cao.Bao_Cao import BaoCao
from infrastructure.models.Bao_Cao_Model import BaoCaoORM
from domain.models.Bao_Cao.iBao_Cao import IBaoCaoRepository
from domain.models.Tai_Khoan.Tai_Khoan import VaiTro , TaiKhoan
from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi
from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from sqlalchemy.orm import Session

class BaoCaoRepository(IBaoCaoRepository):
    def __init__(self, session : Session , tai_khoan : ITaiKhoanRepository):
        self.session = session
        self.repo_tai_khoan = tai_khoan
    def add(self, bao_cao: BaoCao) -> BaoCao:
        orm = BaoCaoORM( 
                        noi_dung=bao_cao.noi_dung, 
                        id_nguoi_gui=bao_cao.nguoi_gui.id
                        )
        self.session.add(orm)
        self.session.flush()
        bao_cao.id = orm.id
        bao_cao.ngay_gui=orm.ngay_gui
        self.session.commit()
        return bao_cao

    def _to_domain(self, orm: BaoCaoORM) -> BaoCao:
        nguoi_gui = self.repo_tai_khoan.get_by_id(orm.id_nguoi_gui)
        return BaoCao(
            id=orm.id,
            noi_dung=orm.noi_dung,
            ngay_gui=orm.ngay_gui,
            nguoi_gui=nguoi_gui
        )
     
    def get_all(self) -> list[BaoCao]:
        orm_list : list[BaoCaoORM] = self.session.query(BaoCaoORM).all()
        return [
            self._to_domain(orm)
            for orm in orm_list
        ]
    
    def get_by_id(self, id: str) -> BaoCao | None:
        orm : BaoCaoORM = self.session.query(BaoCaoORM).filter_by(id=id).first()
        if orm is None:
            raise Exception("Báo cáo không tồn tại!")
        return self._to_domain(orm)
    
    def set_phan_hoi(self, phan_hoi: PhanHoi, bao_cao: BaoCao) -> bool:
        orm : BaoCaoORM | None = (
            self.session
            .query(BaoCaoORM)
            .filter(BaoCaoORM.id == bao_cao.id)
            .first()
        )
        if orm is None:
            return False
        orm.id_phan_hoi = phan_hoi.id
        self.session.commit()
        return True