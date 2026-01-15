from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.lophoc_model import LopHocModel
from infrastructure.databases.mssql import session

class LopHocRepository:
    def __init__(self, session: Session = session):
        self.session = session

    def add(self, lophoc_data) -> LopHocModel:
        try:
            lophoc = LopHocModel(
                id=lophoc_data.id,
                id_mon_hoc=lophoc_data.id_mon_hoc,
                si_so=lophoc_data.si_so,
                id_giang_vien=lophoc_data.id_giang_vien,
                created_at=lophoc_data.created_at,
                updated_at=lophoc_data.updated_at
            )
            self.session.add(lophoc)
            self.session.commit()
            self.session.refresh(lophoc)
            return lophoc
        except Exception as e:
            self.session.rollback()
            raise ValueError('Không thể thêm lớp học')
        finally:
            self.session.close()

    def get_by_id(self, lophoc_id: str) -> Optional[LopHocModel]:
        return self.session.query(LopHocModel).filter_by(id=lophoc_id).first()

    def list(self) -> List[LopHocModel]:
        return self.session.query(LopHocModel).all()

    def update(self, lophoc_data) -> LopHocModel:
        try:
            lophoc = LopHocModel(
                id=lophoc_data.id,
                id_mon_hoc=lophoc_data.id_mon_hoc,
                si_so=lophoc_data.si_so,
                id_giang_vien=lophoc_data.id_giang_vien,
                created_at=lophoc_data.created_at,
                updated_at=lophoc_data.updated_at
            )
            self.session.merge(lophoc)
            self.session.commit()
            return lophoc
        except Exception as e:
            self.session.rollback()
            raise ValueError('Không thể cập nhật lớp học')
        finally:
            self.session.close()

    def delete(self, lophoc_id: str) -> None:
        try:
            lophoc = self.session.query(LopHocModel).filter_by(id=lophoc_id).first()
            if lophoc:
                self.session.delete(lophoc)
                self.session.commit()
            else:
                raise ValueError('Lớp học không tồn tại')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Không thể xóa lớp học')
        finally:
            self.session.close()