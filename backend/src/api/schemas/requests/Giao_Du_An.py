from pydantic import BaseModel , Field

class GiaoDuAnRequest(BaseModel):
    id_du_an : str = Field(...,)
    id_lop_hoc : str = Field(...,)