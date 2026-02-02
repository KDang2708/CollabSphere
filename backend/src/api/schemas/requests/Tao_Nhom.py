from pydantic import BaseModel , Field

class TaoNhomRequest(BaseModel):
    id_lop_hoc : str = Field(...,)