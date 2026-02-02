from pydantic import BaseModel , Field

class TaoMonHocRequest(BaseModel):
    ten_mon_hoc : str = Field(..., min_length=3 , max_length=50)
    tin_chi : int = Field(...,ge=2,le=5)
    de_cuong : str = Field(...,max_length=255)
