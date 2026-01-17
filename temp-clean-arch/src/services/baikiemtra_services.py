from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.baikiemtra_model import BaiKiemTraModel
from infrastructure.databases.mssql import session


class BaiKiemTraRepositories:
    """
    Repository xử lý truy cập CSDL cho Bài Kiểm Tra
    """

    def __init__(self, session: Session = session):
        self.session = session

    # ===============================
    # THÊM BÀI KIỂM TRA
    # ===============================
    def them_bai_kiem_tra(self, du_lieu_bai_kiem_tra) -> BaiKiemTraModel:
        try:
            bai_kiem_tra = BaiKiemTraModel(
                id=du_lieu_bai_kiem_tra.id,
                id_du_an=du_lieu_bai_kiem_tra.id_du_an,
                ten_bai_kiem_tra=du_lieu_bai_kiem_tra.ten_bai_kiem_tra,
                mo_ta=du_lieu_bai_kiem_tra.mo_ta,
                thoi_gian_lam_bai=du_lieu_bai_kiem_tra.thoi_gian_lam_bai,
                trang_thai=du_lieu_bai_kiem_tra.trang_thai,
                created_at=du_lieu_bai_kiem_tra.created_at,
                updated_at=du_lieu_bai_kiem_tra.updated_at
            )
            self.session.add(bai_kiem_tra)
            self.session.commit()
            self.session.refresh(bai_kiem_tra)
            return bai_kiem_tra
        except Exception:
            self.session.rollback()
            raise ValueError("Không thể thêm bài kiểm tra")
        finally:
            self.session.close()

    # ===============================
    # LẤY BÀI KIỂM TRA THEO ID
    # ===============================
    def lay_theo_id(self, id_bai_kiem_tra: str) -> Optional[BaiKiemTraModel]:
        return (
            self.session
            .query(BaiKiemTraModel)
            .filter_by(id=id_bai_kiem_tra)
            .first()
        )

    # ===============================
    # LẤY DANH SÁCH BÀI KIỂM TRA THEO DỰ ÁN
    # ===============================
    def danh_sach_theo_du_an(self, id_du_an: str) -> List[BaiKiemTraModel]:
        return (
            self.session
            .query(BaiKiemTraModel)
            .filter_by(id_du_an=id_du_an)
            .all()
        )

    # ===============================
    # CẬP NHẬT BÀI KIỂM TRA
    # ===============================
    def cap_nhat_bai_kiem_tra(self, du_lieu_bai_kiem_tra) -> BaiKiemTraModel:
        try:
            bai_kiem_tra = BaiKiemTraModel(
                id=du_lieu_bai_kiem_tra.id,
                id_du_an=du_lieu_bai_kiem_tra.id_du_an,
                ten_bai_kiem_tra=du_lieu_bai_kiem_tra.ten_bai_kiem_tra,
                mo_ta=du_lieu_bai_kiem_tra.mo_ta,
                thoi_gian_lam_bai=du_lieu_bai_kiem_tra.thoi_gian_lam_bai,
                trang_thai=du_lieu_bai_kiem_tra.trang_thai,
                created_at=du_lieu_bai_kiem_tra.created_at,
                updated_at=du_lieu_bai_kiem_tra.updated_at
            )
            self.session.merge(bai_kiem_tra)
            self.session.commit()
            return bai_kiem_tra
        except Exception:
            self.session.rollback()
            raise ValueError("Không thể cập nhật bài kiểm tra")
        finally:
            self.session.close()

    # ===============================
    # XÓA BÀI KIỂM TRA
    # ===============================
    def xoa_bai_kiem_tra(self, id_bai_kiem_tra: str) -> None:
        try:
            bai_kiem_tra = (
                self.session
                .query(BaiKiemTraModel)
                .filter_by(id=id_bai_kiem_tra)
                .first()
            )

            if not bai_kiem_tra:
                raise ValueError("Bài kiểm tra không tồn tại")

            self.session.delete(bai_kiem_tra)
            self.session.commit()
        except Exception:
            self.session.rollback()
            raise ValueError("Không thể xóa bài kiểm tra")
        finally:
            self.session.close()
