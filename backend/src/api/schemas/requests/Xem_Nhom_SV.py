from pydantic import BaseModel , Field

class XemNhomSVRequest(BaseModel):
    id_nhom : str = Field(...,)