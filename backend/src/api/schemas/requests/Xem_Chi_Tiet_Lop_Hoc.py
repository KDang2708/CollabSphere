from pydantic import BaseModel , Field

class XemChiTietLopHocRequest(BaseModel):
    id_lop_hoc : str = Field(...,)