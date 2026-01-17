from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.nhiemvu_model import NhiemVuModel


class NhiemVuRepository:
    """
    Repository xử lý dữ liệu Nhiệm Vụ
    """

    def __init__(self, session: Session):
        self.session = session

    # ===============================
    # THÊM NHIỆM VỤ
    # ===============================
    def them_nhiem_vu(self, du_lieu) -> NhiemVuModel:
        nhiem_vu = NhiemVuModel(
            id=du_lieu.id,
            id_du_an=du_lieu.id_du_an,
            ten_nhiem_vu=du_lieu.ten_nhiem_vu,
            mo_ta=du_lieu.mo_ta,
            trang_thai=du_lieu.trang_thai,
            nguoi_thuc_hien=du_lieu.nguoi_thuc_hien,
            created_at=du_lieu.created_at,
            updated_at=du_lieu.updated_at
        )
        try:
            self.session.add(nhiem_vu)
            self.session.commit()
            self.session.refresh(nhiem_vu)
            return nhiem_vu
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # LẤY NHIỆM VỤ THEO ID
    # ===============================
    def lay_nhiem_vu_theo_id(self, id_nhiem_vu: str) -> Optional[NhiemVuModel]:
        return (
            self.session
            .query(NhiemVuModel)
            .filter(NhiemVuModel.id == id_nhiem_vu)
            .first()
        )

    # ===============================
    # LẤY DANH SÁCH THEO DỰ ÁN
    # ===============================
    def lay_danh_sach_theo_du_an(self, id_du_an: str) -> List[NhiemVuModel]:
        return (
            self.session
            .query(NhiemVuModel)
            .filter(NhiemVuModel.id_du_an == id_du_an)
            .all()
        )

    # ===============================
    # CẬP NHẬT NHIỆM VỤ
    # ===============================
    def cap_nhat_nhiem_vu(self, du_lieu) -> NhiemVuModel:
        nhiem_vu = self.lay_nhiem_vu_theo_id(du_lieu.id)
        if not nhiem_vu:
            raise ValueError("Nhiệm vụ không tồn tại")

        nhiem_vu.ten_nhiem_vu = du_lieu.ten_nhiem_vu
        nhiem_vu.mo_ta = du_lieu.mo_ta
        nhiem_vu.trang_thai = du_lieu.trang_thai
        nhiem_vu.nguoi_thuc_hien = du_lieu.nguoi_thuc_hien
        nhiem_vu.updated_at = du_lieu.updated_at

        try:
            self.session.commit()
            self.session.refresh(nhiem_vu)
            return nhiem_vu
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # PHÂN CÔNG NHIỆM VỤ
    # ===============================
    def phan_cong_nhiem_vu(self, id_nhiem_vu: str, nguoi_thuc_hien: str):
        nhiem_vu = self.lay_nhiem_vu_theo_id(id_nhiem_vu)
        if not nhiem_vu:
            raise ValueError("Nhiệm vụ không tồn tại")

        try:
            nhiem_vu.nguoi_thuc_hien = nguoi_thuc_hien
            nhiem_vu.trang_thai = "DA_PHAN_CONG"
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # CẬP NHẬT TRẠNG THÁI
    # ===============================
    def cap_nhat_trang_thai(self, id_nhiem_vu: str, trang_thai: str):
        nhiem_vu = self.lay_nhiem_vu_theo_id(id_nhiem_vu)
        if not nhiem_vu:
            raise ValueError("Nhiệm vụ không tồn tại")

        try:
            nhiem_vu.trang_thai = trang_thai
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

    # ===============================
    # XÓA NHIỆM VỤ
    # ===============================
    def xoa_nhiem_vu(self, id_nhiem_vu: str):
        nhiem_vu = self.lay_nhiem_vu_theo_id(id_nhiem_vu)
        if not nhiem_vu:
            raise ValueError("Nhiệm vụ không tồn tại")

        try:
            self.session.delete(nhiem_vu)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
