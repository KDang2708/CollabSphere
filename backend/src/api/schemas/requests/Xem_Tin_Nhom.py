from pydantic import BaseModel , Field

class XemTinNhomRequest(BaseModel):
    id_lop_hoc : str = Field(...,)
    id_nhom : str = Field(...,)