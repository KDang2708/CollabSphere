from sqlalchemy.orm import Session
from typing import List, Optional
from infrastructure.models.baikiemtra_model import BaiKiemTraModel

class BaiKiemTraRepository:
    def __init__(self, session: Session):
        self.session = session

    def them_bai_kiem_tra(self, du_lieu) -> BaiKiemTraModel:
        # Không cần truyền created_at/updated_at vì Model đã tự sinh
        bai_kiem_tra = BaiKiemTraModel(
            id=du_lieu.id,
            id_du_an=du_lieu.id_du_an,
            ten_bai_kiem_tra=du_lieu.ten_bai_kiem_tra,
            mo_ta=du_lieu.mo_ta,
            thoi_gian_lam_bai=du_lieu.thoi_gian_lam_bai,
            trang_thai=du_lieu.trang_thai
        )
        try:
            self.session.add(bai_kiem_tra)
            self.session.commit()
            self.session.refresh(bai_kiem_tra)
            return bai_kiem_tra
        except Exception as e:
            self.session.rollback()
            raise e

    def lay_theo_id(self, id_bai_kiem_tra: str) -> Optional[BaiKiemTraModel]:
        return self.session.query(BaiKiemTraModel).filter(BaiKiemTraModel.id == id_bai_kiem_tra).first()

    def danh_sach_theo_du_an(self, id_du_an: str) -> List[BaiKiemTraModel]:
        return self.session.query(BaiKiemTraModel).filter(BaiKiemTraModel.id_du_an == id_du_an).all()