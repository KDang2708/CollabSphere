        # self.id = id
        # self.mon_hoc = mon_hoc
        # self.giang_vien = giang_vien
from pydantic import BaseModel
class TaoLopHocResponse(BaseModel):
    id_lop_hoc : str
    id_mon_hoc : str
    ten_mon_hoc : str
    de_cuong : str
    tin_chi : str
    id_giang_vien : str
    ten_giang_vien : str