from pydantic import BaseModel , Field

class TimKiemTaiKhoanRequest(BaseModel):
    id_tai_khoan : str = Field(...,)