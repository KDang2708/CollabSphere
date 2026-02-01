# Phản hồi - dùng TYPE_CHECKING tránh circular import với Bao_Cao
from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.models.Bao_Cao.Bao_Cao import BaoCao


class PhanHoi:
    def __init__(self, id: str | None, noi_dung: str, ngay_gui: datetime | None, bao_cao: BaoCao):
        self.id = id
        self.noi_dung = noi_dung
        self.ngay_gui = ngay_gui
        self.bao_cao = bao_cao