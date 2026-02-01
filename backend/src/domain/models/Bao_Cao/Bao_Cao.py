# Báo cáo(IDBaoCao, NoiDung, NgayGui, IDNguoiGui) - dùng TYPE_CHECKING tránh circular import với Phan_Hoi
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

from domain.models.Giang_Vien.Giang_Vien import GiangVien
from domain.models.Tai_Khoan.Tai_Khoan import TaiKhoan

if TYPE_CHECKING:
    from domain.models.Phan_Hoi.Phan_Hoi import PhanHoi


class BaoCao:
    def __init__(self, id: str | None, noi_dung: str, ngay_gui: datetime | None, nguoi_gui: TaiKhoan, phan_hoi: PhanHoi | None):
        self.id = id
        self.noi_dung = noi_dung
        self.ngay_gui = ngay_gui
        self.nguoi_gui = nguoi_gui
        self.phan_hoi = phan_hoi
    