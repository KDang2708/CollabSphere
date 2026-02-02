# Sinh Vien tạo bài làm và nộp lên hệ thống 
from domain.models.Bai_Lam.Bai_Lam import BaiLam
from domain.models.Bai_Lam.iBai_Lam import IBaiLamRepository
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Nhiem_Vu.iNhiem_Vu import INhiemVuRepository
from domain.models.Bai_Kiem_Tra.iBai_Kiem_Tra import IBaiKiemTraRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository

class NopBaiUseCase():
    def __init__(self ,sinh_vien : ISinhVienRepository, bai_lam : IBaiLamRepository , nhiem_vu : INhiemVuRepository , bai_kiem_tra : IBaiKiemTraRepository):
        self.repo_bai_lam = bai_lam
        self.repo_nhiem_vu = nhiem_vu
        self.repo_bai_kiem_tra = bai_kiem_tra
        self.repo_sinh_vien = sinh_vien
    def execute(self , noi_dung_bai_lam : str , loai_bai_lam : int , id_bai_kiem_tra : str , id_sinh_vien : str )->BaiLam:
        sinh_vien = self.repo_sinh_vien.get_by_id(id_sinh_vien)
        if loai_bai_lam == 0 :
            bai_kiem_tra= self.repo_nhiem_vu.get_by_id(id_bai_kiem_tra) # viết hàm get_by_id
        elif loai_bai_lam==1:
            bai_kiem_tra = self.repo_bai_kiem_tra.get_by_id(id_bai_kiem_tra) # viết hàm het_by_id
        bai_lam = BaiLam(noi_dung_bai_lam=noi_dung_bai_lam , loai_bai_lam=loai_bai_lam , bai_kiem_tra=bai_kiem_tra , sinh_vien_thuc_hien= sinh_vien )
        bai_lam=self.repo_bai_lam.add(bai_lam) # viết hàm add
        return bai_lam



# class BaiLam:
#     def __init__(self, id : str | None , noi_dung_bai_lam: str, loai_bai_lam: int , bai_kiem_tra : BaiKiemTra|NhiemVu, sinh_vien_thuc_hien: HocSinh):
#         self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
#         self.noi_dung_bai_lam = noi_dung_bai_lam
#         self.loai_bai_lam = loai_bai_lam # bằng 0 là bài kiểm tra = 1 là nhiệm vụ 
#         self.bai_kiem_tra = bai_kiem_tra
#         self.sinh_vien_thuc_hien = sinh_vien_thuc_hien