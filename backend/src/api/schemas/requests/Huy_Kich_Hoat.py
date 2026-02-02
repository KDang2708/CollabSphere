from pydantic import BaseModel , Field

class HuyKichHoatRequest(BaseModel):
    id_tai_khoan : str = Field(...,)