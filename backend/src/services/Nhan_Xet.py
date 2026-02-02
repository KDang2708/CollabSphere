from domain.models.Nhan_Xet.Nhan_Xet import NhanXet
from domain.models.Nhan_Xet.iNhan_Xet import INhanXetRepository
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Bai_Lam.Bai_Lam import BaiLam
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from domain.models.Bai_Lam.iBai_Lam import IBaiLamRepository

class NhanXetUseCase():
    def __init__(self, nhan_xet : INhanXetRepository , bai_lam : IBaiLamRepository , giang_vien : IGiangVienRepository ):
        self.repo_nhan_xet = nhan_xet
        self.repo_bai_lam = bai_lam
        self.repo_giang_vien = giang_vien
    def execute(self , noi_dung_nhan_xet : str , id_giang_vien : str , id_bai_lam : str )->NhanXet:
        giang_vien = self.repo_giang_vien.get_by_id(id_giang_vien)
        bai_lam = self.repo_bai_lam.get_by_id(id_bai_lam)
        nhan_xet = NhanXet(
            noi_dung_nhan_xet=noi_dung_nhan_xet,
            giang_vien_nhan_xet=giang_vien,
            bai_lam=bai_lam
        )
        nhan_xet = self.repo_nhan_xet.add(nhan_xet)
        return nhan_xet



# class NhanXet:
#     def __init__(self,id : str |None, noi_dung_nhan_xet: str, giang_vien_nhan_xet: GiangVien, bai_lam: BaiLam):
#         self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung_nhan_xet = noi_dung_nhan_xet
#         self.giang_vien_nhan_xet = giang_vien_nhan_xet
#         self.bai_lam = bai_lam


# class NhiemVuORM(Base):
#     __tablename__ = "nhiem_vu"

#     id = Column(String , primary_key=True , default=lambda : str(uuid.uuid4()))
#     noi_dung_nhan_xet = Column(String)
#     id_giang_vien = Column(String , ForeignKey("giang_vien"))
#     id_bai_lam = Column(String, ForeignKey("bai_lam"))