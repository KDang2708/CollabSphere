from pydantic import BaseModel , Field

class XemNhomRequest(BaseModel):
    id_nhom : str = Field(...,)