from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.duan_model import DuAnModel


class DuAnRepository:
    """
    Repository xử lý dữ liệu Dự Án
    """

    def __init__(self, session: Session):
        self.session = session

    # ===============================
    # THÊM DỰ ÁN
    # ===============================
    def them_du_an(self, du_lieu_du_an) -> DuAnModel:
        du_an = DuAnModel(
            id=du_lieu_du_an.id,
            ten_du_an=du_lieu_du_an.ten_du_an,
            mo_ta=du_lieu_du_an.mo_ta,
            trang_thai=du_lieu_du_an.trang_thai,
            created_at=du_lieu_du_an.created_at,
            updated_at=du_lieu_du_an.updated_at
        )
        try:
            self.session.add(du_an)
            self.session.commit()
            self.session.refresh(du_an)
            return du_an
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # LẤY DỰ ÁN THEO ID
    # ===============================
    def lay_du_an_theo_id(self, id_du_an: str) -> Optional[DuAnModel]:
        return (
            self.session
            .query(DuAnModel)
            .filter(DuAnModel.id == id_du_an)
            .first()
        )

    # ===============================
    # LẤY DANH SÁCH DỰ ÁN
    # ===============================
    def lay_danh_sach_du_an(self) -> List[DuAnModel]:
        return self.session.query(DuAnModel).all()

    # ===============================
    # CẬP NHẬT DỰ ÁN
    # ===============================
    def cap_nhat_du_an(self, du_lieu_du_an) -> DuAnModel:
        du_an = self.lay_du_an_theo_id(du_lieu_du_an.id)
        if not du_an:
            raise ValueError("Dự án không tồn tại")

        du_an.ten_du_an = du_lieu_du_an.ten_du_an
        du_an.mo_ta = du_lieu_du_an.mo_ta
        du_an.trang_thai = du_lieu_du_an.trang_thai
        du_an.updated_at = du_lieu_du_an.updated_at

        try:
            self.session.commit()
            self.session.refresh(du_an)
            return du_an
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # ĐÓNG DỰ ÁN
    # ===============================
    def dong_du_an(self, id_du_an: str):
        du_an = self.lay_du_an_theo_id(id_du_an)
        if not du_an:
            raise ValueError("Dự án không tồn tại")

        try:
            du_an.trang_thai = "DA_DONG"
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # XÓA DỰ ÁN
    # ===============================
    def xoa_du_an(self, id_du_an: str):
        du_an = self.lay_du_an_theo_id(id_du_an)
        if not du_an:
            raise ValueError("Dự án không tồn tại")

        try:
            self.session.delete(du_an)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
