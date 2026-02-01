from domain.models.Cuoc_Hop.Cuoc_Hop import CuocHop
from domain.models.Cuoc_Hop.iCuoc_Hop import ICuocHopRepository
from infrastructure.models.Cuoc_Hop_Model import CuocHopORM
from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Nhom.Nhom import Nhom
from sqlalchemy.orm import Session

class CuocHopRepository(ICuocHopRepository):
    def __init__(self , session : Session ):
        self.session = session
    def add(self, cuoc_hop : CuocHop)->CuocHop:
        orm = CuocHopORM(
            thoi_gian_bat_dau = cuoc_hop.thoi_gian_bat_dau,
            id_nguoi_tao = cuoc_hop.nguoi_tao.id,
            vai_tro_nguoi_tao = cuoc_hop.nguoi_tao.tai_khoan.vai_tro.value,
            id_lop_hoc = cuoc_hop.lop_hoc.id,
            id_nhom = cuoc_hop.nhom.id if cuoc_hop.nhom is not None else None
        )
        self.session.add(orm)   
        self.session.flush()
        cuoc_hop.id=orm.id
        self.session.commit()
        return cuoc_hop
    def get_cuoc_hop_by_lop(self, lop_hoc: LopHoc) -> list[CuocHop]:
        orm_list = (
            self.session
            .query(CuocHopORM)
            .filter(
                CuocHopORM.id_lop_hoc == lop_hoc.id,
                CuocHopORM.id_nhom == None   # chỉ lấy cuộc họp lớp
            )
            .order_by(CuocHopORM.thoi_gian_bat_dau.asc())
            .all()
        )

        ds_cuoc_hop: list[CuocHop] = []

        for orm in orm_list:
            cuoc_hop = CuocHop(
                id=orm.id,
                thoi_gian_bat_dau=orm.thoi_gian_bat_dau,
                lop_hoc=lop_hoc,
                nguoi_tao=None,   # nếu cần thì load thêm sau
                nhom=None
            )
            ds_cuoc_hop.append(cuoc_hop)

        return ds_cuoc_hop
    def get_cuoc_hop_by_nhom(self, lop_hoc : LopHoc, nhom:Nhom)->list[CuocHop]:
        orm_list = (
            self.session
            .query(CuocHopORM)
            .filter(
                CuocHopORM.id_lop_hoc == lop_hoc.id,
                CuocHopORM.id_nhom == nhom.id
            )
            .order_by(CuocHopORM.thoi_gian_bat_dau.asc())
            .all()
        )

        ds_cuoc_hop: list[CuocHop] = []

        for orm in orm_list:
            cuoc_hop = CuocHop(
                id=orm.id,
                thoi_gian_bat_dau=orm.thoi_gian_bat_dau,
                lop_hoc=lop_hoc,
                nhom=nhom,
                nguoi_tao=None   # nếu cần thì load sau
            )
            ds_cuoc_hop.append(cuoc_hop)

        return ds_cuoc_hop
    # id = Column(String, primary_key=True , default=lambda:str(uuid.uuid4()))          # cột ID, kiểu String, là khóa chính
    # thoi_gian_bat_dau = Column(DateTime)           # cột thời gian bắt đầu, kiểu DateTime
    # id_nguoi_tao = Column(String)                   # cột ID người tạo, kiểu String
    # id_lop_hoc = Column(String , ForeignKey("lop_hoc"))                     # cột ID lớp học, kiểu String
    # id_nhom = Column(String,ForeignKey("nhom") ,  nullable=True)                        # cột ID nhóm, kiểu String