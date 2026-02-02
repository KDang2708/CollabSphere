from pydantic import BaseModel , Field

class XemThongTinLopHocRequest(BaseModel):
    id_lop_hoc : str = Field(...,)