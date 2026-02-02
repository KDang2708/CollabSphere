from pydantic import BaseModel, Field
from typing import Optional

class NhanTinRequest(BaseModel):
    noi_dung: str = Field(..., max_length=500)
    vai_tro_nguoi_gui: int = Field(..., description="0: sinh viên, 1: giảng viên")
    id_nguoi_gui: str
    id_lop_hoc: str
    id_nhom: Optional[str] = None
