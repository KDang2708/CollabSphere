from pydantic import BaseModel , Field

class TaiKichHoatRequest(BaseModel):
    id_tai_khoan : str = Field(...,)