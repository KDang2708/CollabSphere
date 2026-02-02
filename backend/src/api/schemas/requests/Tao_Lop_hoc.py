from pydantic import BaseModel , Field

class TaoLopHocRequest(BaseModel):
    id_mon_hoc :str=Field(...,)
    id_giang_vien : str = Field(...,)