from pydantic import BaseModel
from datetime import datetime

class PhanHoiResponse(BaseModel):
    id_phan_hoi : str
    noi_dung : str
    ngay_gui : datetime
    id_bao_cao : str