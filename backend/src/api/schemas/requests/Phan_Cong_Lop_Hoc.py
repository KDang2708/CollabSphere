from pydantic import BaseModel , Field

class PhanCongLopHocRequest(BaseModel):
    id_lop_hoc : str = Field(...,)
    id_sinh_vien : str = Field(...,)