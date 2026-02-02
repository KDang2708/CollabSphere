from pydantic import BaseModel

class XemLopHocResponse(BaseModel):
    id_lop_hoc : str
    id_mon_hoc : str
    ten_mon_hoc : str
    id_giang_vien : str
    ten_giang_vien : str