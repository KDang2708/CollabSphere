from domain.models.Tai_Khoan.Vai_Tro import VaiTro
from domain.models.Tai_Khoan.RolePolicy import ROLE_PERMISSIONS
from domain.models.Tai_Khoan.Quyen import Quyen
from fastapi import pw

class TaiKhoan:
    def __init__(self,id : str | None, ten_dang_nhap: str, mat_khau: str, vai_tro: VaiTro , trang_thai : bool |None):
        self.id = id
        self.ten_dang_nhap = ten_dang_nhap
        self.mat_khau = mat_khau
        self.vai_tro = vai_tro
        self.trang_thai = True

    def co_quyen(self, quyen: Quyen) -> bool:
        return quyen in ROLE_PERMISSIONS.get(self.vai_tro, set())

    def khoa(self):
        self.trang_thai = False

    def mo(self):
        self.trang_thai = True
    