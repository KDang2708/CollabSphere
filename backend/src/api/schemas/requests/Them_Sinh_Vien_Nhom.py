from pydantic import BaseModel , Field

class ThemSinhVienNhomRequest(BaseModel):
    id_nhom : str = Field(...,)
    id_sinh_vien : str = Field(...,)