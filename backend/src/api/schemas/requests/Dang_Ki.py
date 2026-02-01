from pydantic import BaseModel, Field
from domain.models.Tai_Khoan.Vai_Tro import VaiTro

class DangKiRequest(BaseModel):
    ten_dang_nhap: str = Field(..., min_length=3, max_length=50)
    mat_khau: str = Field(..., min_length=6)
    vai_tro: VaiTro
