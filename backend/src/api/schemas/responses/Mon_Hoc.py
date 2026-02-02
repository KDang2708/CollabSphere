from pydantic import BaseModel , Field

class MonHocResponse(BaseModel):
    id_mon_hoc : str
    ten_mon_hoc : str
    tin_chi : int 
    de_cuong : str 
