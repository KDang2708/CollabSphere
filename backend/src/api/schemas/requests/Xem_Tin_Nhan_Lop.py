from pydantic import BaseModel , Field

class XemTinNhanLopRequest(BaseModel):
    id_lop_hoc : str = Field(...,)