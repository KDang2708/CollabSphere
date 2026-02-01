from pydantic import BaseModel , Field

class DangNhapRequset(BaseModel):
    ten_dang_nhap : str = Field(...,min_length=3 , max_length=50)
    mat_khau : str = Field(...,min_length=6)