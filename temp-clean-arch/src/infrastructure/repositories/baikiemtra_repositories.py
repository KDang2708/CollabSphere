from sqlalchemy.orm import session
from typing import List, Optional

from domain.models.baikiemtra import BaiKiemTra
from domain.models.ibaikiemtra import IBaiKiemTraRepository
from infrastructure.models.baikiemtra_models import BaiKiemTraModel


class BaiKiemTraRepository(IBaiKiemTraRepository):
    """
    Repository triển khai IBaiKiemTraRepository
    Sử dụng SQLAlchemy
    """

    def __init__(self, session: Session):
        self.session = session

    # ===============================
    # PRIVATE: ORM -> DOMAIN
    # ===============================
    def _to_domain(self, model: BaiKiemTraModel) -> BaiKiemTra:
        return BaiKiemTra(
            id=model.id,
            id_du_an=model.id_du_an,
            ten_bai_kiem_tra=model.ten_bai_kiem_tra,
            mo_ta=model.mo_ta,
            thoi_gian_lam_bai=model.thoi_gian_lam_bai,
            trang_thai=model.trang_thai
        )

    # ===============================
    # PRIVATE: DOMAIN -> ORM
    # ===============================
    def _to_model(self, entity: BaiKiemTra) -> BaiKiemTraModel:
        return BaiKiemTraModel(
            id=entity.id,
            id_du_an=entity.id_du_an,
            ten_bai_kiem_tra=entity.ten_bai_kiem_tra,
            mo_ta=entity.mo_ta,
            thoi_gian_lam_bai=entity.thoi_gian_lam_bai,
            trang_thai=entity.trang_thai
        )

    # ===============================
    # THÊM
    # ===============================
    def them(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        model = self._to_model(bai_kiem_tra)

        try:
            self.session.add(model)
            self.session.commit()
            self.session.refresh(model)
            return self._to_domain(model)
        except Exception:
            self.session.rollback()
            raise

    # ===============================
    # LẤY THEO ID (CÓ THỂ NONE)
    # ===============================
    def lay_theo_id(self, id_bai_kiem_tra: str) -> Optional[BaiKiemTra]:
        model = (
            self.session
            .query(BaiKiemTraModel)
            .filter(BaiKiemTraModel.id == id_bai_kiem_tra)
            .first()
        )

        if model is None:
            return None

        return self._to_domain(model)

    # ===============================
    # LẤY THEO ID (BẮT BUỘC)
    # ===============================
    def lay_bat_buoc(self, id_bai_kiem_tra: str) -> BaiKiemTra:
        bai_kiem_tra = self.lay_theo_id(id_bai_kiem_tra)
        if bai_kiem_tra is None:
            raise ValueError("Bài kiểm tra không tồn tại")
        return bai_kiem_tra

    # ===============================
    # DANH SÁCH THEO DỰ ÁN
    # ===============================
    def danh_sach_theo_du_an(self, id_du_an: str) -> List[BaiKiemTra]:
        models = (
            self.session
            .query(BaiKiemTraModel)
            .filter(BaiKiemTraModel.id_du_an == id_du_an)
            .all()
        )

        return [self._to_domain(model) for model in models]

    # ===============================
    # CẬP NHẬT
    # ===============================
    def cap_nhat(self, bai_kiem_tra: BaiKiemTra) -> BaiKiemTra:
        model = (
            self.session
            .query(BaiKiemTraModel)
            .filter(BaiKiemTraModel.id == bai_kiem_tra.id)
            .first()
        )

        if model is None:
            raise ValueError("Bài kiểm tra không tồn tại")

        model.ten_bai_kiem_tra = bai_kiem_tra.ten_bai_kiem_tra
        model.mo_ta = bai_kiem_tra.mo_ta
        model.thoi_gian_lam_bai = bai_kiem_tra.thoi_gian_lam_bai
        model.trang_thai = bai_kiem_tra.trang_thai

        try:
            self.session.commit()
            self.session.refresh(model)
            return self._to_domain(model)
        except Exception:
            self.session.rollback()
            raise

    # ===============================
    # XÓA
    # ===============================
    def xoa(self, id_bai_kiem_tra: str) -> None:
        model = (
            self.session
            .query(BaiKiemTraModel)
            .filter(BaiKiemTraModel.id == id_bai_kiem_tra)
            .first()
        )

        if model is None:
            raise ValueError("Bài kiểm tra không tồn tại")

        try:
            self.session.delete(model)
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise
