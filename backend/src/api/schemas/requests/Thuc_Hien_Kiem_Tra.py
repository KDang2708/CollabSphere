from pydantic import BaseModel , Field

class ThucHienKiemTraRequest(BaseModel):
    id_sinh_vien : str = Field(...,)