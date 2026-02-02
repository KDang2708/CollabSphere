# domain/models/Nhom/Nhom.py
from typing import List, Optional
from domain.models.Sinh_Vien.Sinh_Vien import SinhVien as HocSinh

# KHÔNG import LopHoc ở đây

class Nhom:
    def __init__(
        self,
        id: Optional[str] = None,
        lop_hoc=None,                       # type sẽ được check runtime hoặc qua mypy
        danh_sach_hoc_sinh: List[HocSinh] = None
    ):
        self.id = id
        self.lop_hoc = lop_hoc
        self.danh_sach_hoc_sinh = danh_sach_hoc_sinh or []

    # Nếu dùng type checker nghiêm ngặt (mypy/pyright), thêm:
    # from __future__ import annotations   (ở đầu file nếu Python < 3.10)