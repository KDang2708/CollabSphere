from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan , VaiTro
from domain.models.Admin.Admin import Admin
from domain.models.Nhan_Vien.Nhan_Vien import NhanVien
from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Truong_Khoa.Truong_Khoa import TruongKhoa
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien
from domain.models.Admin.iAdmin import IAdminRepository
from domain.models.Giang_Vien.iGiang_Vien import IGiangVienRepository
from domain.models.Nhan_Vien.iNhan_Vien import INhanVienRepository
from domain.models.Sinh_Vien.iSinh_Vien import ISinhVienRepository
from domain.models.Truong_Khoa.iTruong_Khoa import ITruongKhoaRepository

class DangKiUseCase():
    def __init__(self, tai_khoan: ITaiKhoanRepository , admin : IAdminRepository , nhan_vien : INhanVienRepository , giang_vien : IGiangVienRepository , sinh_vien : ISinhVienRepository, truong_khoa : ITruongKhoaRepository):
        self.repo_tai_khoan = tai_khoan
        self.repo_admin =admin
        self.repo_nhan_vien =nhan_vien
        self.repo_giang_vien =giang_vien
        self.repo_sinh_vien = sinh_vien
        self.repo_truong_khoa = truong_khoa
    def execute(self, ten_dang_nhap: str, mat_khau: str, vai_tro : VaiTro) -> TaiKhoan:
        tai_khoan = TaiKhoan(ten_dang_nhap=ten_dang_nhap, mat_khau=mat_khau , vai_tro=vai_tro)
        tai_khoan =  self.repo_tai_khoan.add(tai_khoan)
        if vai_tro == VaiTro.ADMIN:
            admin= Admin(
                ten=tai_khoan.ten_dang_nhap,
                tai_khoan=tai_khoan
            )
            self.repo_admin.add(admin)
        elif vai_tro == VaiTro.NHAN_VIEN:
            nhan_vien = NhanVien(
                ten=tai_khoan.ten_dang_nhap,
                tai_khoan=tai_khoan
            )
            self.repo_nhan_vien.add(nhan_vien)

        elif vai_tro == VaiTro.GIANG_VIEN:
            giang_vien = GiangVien(
                ten=tai_khoan.ten_dang_nhap,
                tai_khoan=tai_khoan
            )
            self.repo_giang_vien.add(giang_vien)

        elif vai_tro == VaiTro.SINH_VIEN:
            sinh_vien = SinhVien(
                ten=tai_khoan.ten_dang_nhap,
                tai_khoan=tai_khoan
            )
            self.repo_sinh_vien.add(sinh_vien)

        elif vai_tro == VaiTro.TRUONG_KHOA:
            truong_khoa = TruongKhoa(
                ten=tai_khoan.ten_dang_nhap,
                tai_khoan=tai_khoan
            )
            self.repo_truong_khoa.add(truong_khoa)

        else:
            raise Exception("Vai trò không hợp lệ")
        return tai_khoan