from domain.models.Lop_Hoc.Lop_Hoc import LopHoc
from domain.models.Lop_Hoc.iLop_Hoc import ILopHocRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Moc_Quan_Trong.iMoc_Quan_trong import IMocQuanTrongRepository
from domain.models.Mon_Hoc.iMon_Hoc import IMonHocRepository
from domain.models.Bai_Kiem_Tra.iBai_Kiem_Tra import IBaiKiemTraRepository


class XemThongTinLopHocUseCase():
    def __init__(self , lop_hoc : ILopHocRepository , mon_hoc : IMonHocRepository , moc_quan_trong : IMocQuanTrongRepository , bai_kiem_tra : IBaiKiemTraRepository):
        self.repo_lop_hoc = lop_hoc
        self.rrepo_mon_hoc = mon_hoc
        self.repo_moc_quan_trong = moc_quan_trong
        self.repo_bai_kiem_tra = bai_kiem_tra
        
    def execute(self , lop_hoc : LopHoc)->LopHoc: # lớp học truyền vào chỉ có id , giáo viên , môn học
        # lấy ra các mốc quan trọng , lấy ra các bài kiểm tra , lấy ra danh sách sinh viên
        mon_hoc = lop_hoc.mon_hoc
        ds_moc_quan_trong = self.repo_moc_quan_trong.get_by_mon_hoc(mon_hoc)
        ds_bai_kiem_tra = self.repo_bai_kiem_tra.get_by_mon_hoc(mon_hoc)
        return  {
        "lop_hoc": lop_hoc,
        "ds_moc_quan_trong": ds_moc_quan_trong,
        "ds_bai_kiem_tra": ds_bai_kiem_tra,
        }
    # trả về 1 tuple