from domain.models.Du_An.Du_An import DuAn
from domain.models.Du_An.iDu_An import IDuAn
from infrastructure.models.Du_An_Model import DuAnORM
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from infrastructure.databases.mssql import session
from typing import List, Optional

class DuAnRepository(IDuAn):
    def add (self, du_an: DuAn) -> DuAn :
        orm = DuAnORM(
            id = du_an.id,
            noidung = du_an.noi_dung,
            trang_thai = du_an.trang_thai,
            id_nguoi_tao = du_an.nguoi_tao.id
        )
        session.add(orm)
        session.commit()
        return du_an
    
    def get_by_id(self, id: str) -> Optional [DuAn]:
        orm = session.query(DuAnORM).filter_by(id=id).first()
        if not orm:
            return None
        

         # Khởi tạo GiangVien ở mức reference (chỉ ID)
        giang_vien = GiangVien(
            id=orm.id_nguoi_tao 
        )
        return DuAn(
            id = orm.id,
            noi_dung= orm.noidung,
            trang_thai= orm.trang_thai,
            nguoi_tao= giang_vien,
            lop_hoc= None # nếu chưa cần
        )
    def get_all(self) -> List[DuAn]:
        result = []
        for o in session.query(DuAnORM).all():
            giang_vien = GiangVien(
                id=o.id_nguoi_tao
            )

            result.append(
                DuAn(
                    id=o.id,
                    noi_dung=o.noidung,
                    trang_thai=o.trang_thai,
                    nguoi_tao=giang_vien,
                    lop_hoc=None
                )
            )
        return result
    