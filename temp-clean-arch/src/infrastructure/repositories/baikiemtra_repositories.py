from sqlalchemy.orm import Session
from typing import List, Optional
from infrastructure.models.baikiemtra import BaiKiemTraModel


class BaiKiemTraRepository:
    """
    Repository xử lý dữ liệu Bài Kiểm Tra
    """

    def __init__(self, session: Session):
        self.session = session

    # ===============================
    # THÊM BÀI KIỂM TRA
    # ===============================
    def them_bai_kiem_tra(self, du_lieu) -> BaiKiemTraModel:
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
        except Exception:
            self.session.rollback()
            raise

    # ===============================
    # LẤY THEO ID
    # ===============================
    def lay_theo_id(self, id_bai_kiem_tra: str) -> Optional[BaiKiemTraModel]:
        return (
            self.session
            .query(BaiKiemTraModel)
            .filter(BaiKiemTraModel.id == id_bai_kiem_tra)
            .first()
        )

    # ===============================
    # DANH SÁCH THEO DỰ ÁN
    # ===============================
    def danh_sach_theo_du_an(self, id_du_an: str) -> List[BaiKiemTraModel]:
        return (
            self.session
            .query(BaiKiemTraModel)
            .filter(BaiKiemTraModel.id_du_an == id_du_an)
            .all()
        )

    # ===============================
    # CẬP NHẬT
    # ===============================
    def cap_nhat_bai_kiem_tra(self, du_lieu) -> BaiKiemTraModel:
        bai_kiem_tra = self.lay_theo_id(du_lieu.id)
        if not bai_kiem_tra:
            raise ValueError("Bài kiểm tra không tồn tại")

        bai_kiem_tra.ten_bai_kiem_tra = du_lieu.ten_bai_kiem_tra
        bai_kiem_tra.mo_ta = du_lieu.mo_ta
        bai_kiem_tra.thoi_gian_lam_bai = du_lieu.thoi_gian_lam_bai
        bai_kiem_tra.trang_thai = du_lieu.trang_thai

        try:
            self.session.commit()
            self.session.refresh(bai_kiem_tra)
            return bai_kiem_tra
        except Exception:
            self.session.rollback()
            raise

    # ===============================
    # XÓA
    # ===============================
    def xoa_bai_kiem_tra(self, id_bai_kiem_tra: str):
        bai_kiem_tra = self.lay_theo_id(id_bai_kiem_tra)
        if not bai_kiem_tra:
            raise ValueError("Bài kiểm tra không tồn tại")

        try:
            self.session.delete(bai_kiem_tra)
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise
