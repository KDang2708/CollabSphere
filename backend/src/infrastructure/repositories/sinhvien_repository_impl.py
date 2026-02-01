from domain.sinhvien.repository import SinhVienRepository
from domain.sinhvien.model import SinhVien
from infrastructure.models.sinhvien_orm import SinhVienORM
from infrastructure.database.db import db

class SinhVienRepositoryImpl(SinhVienRepository):

    def save(self, sinh_vien: SinhVien):
        orm = SinhVienORM(
            id=sinh_vien.id,
            ma_sv=sinh_vien.ma_sv,
            ho_ten=sinh_vien.ho_ten
        )
        db.session.add(orm)
        db.session.commit()

    def get_by_id(self, id: int) -> SinhVien:
        orm = SinhVienORM.query.get(id)
        if not orm:
            return None
        return SinhVien(orm.id, orm.ma_sv, orm.ho_ten)
