from dataclasses import dataclass
from typing import Optional


@dataclass
class BaiKiemTra:
    id: str
    id_du_an: str
    ten_bai_kiem_tra: str
    mo_ta: Optional[str]
    thoi_gian_lam_bai: int
    trang_thai: int
