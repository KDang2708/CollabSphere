from domain.models.Tai_Khoan.Vai_Tro import VaiTro
from domain.models.Tai_Khoan.RolePolicy import ROLE_PERMISSIONS
from domain.models.Tai_Khoan.Quyen import Quyen

class TaiKhoan:
    def __init__(self, ten_dang_nhap: str, mat_khau: str, vai_tro: VaiTro):
        self.id: str | None = None
        self.ten_dang_nhap: str = ten_dang_nhap
        self.mat_khau: str = mat_khau
        self.vai_tro: VaiTro = vai_tro
        self.trang_thai: bool = True

    def co_quyen(self, quyen: Quyen) -> bool:
        return quyen in ROLE_PERMISSIONS.get(self.vai_tro, set())

    def khoa(self) -> None:
        self.trang_thai = False

    def mo(self) -> None:
        self.trang_thai = True
