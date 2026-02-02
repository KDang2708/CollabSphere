from pydantic import BaseModel
from datetime import datetime
class BaoCaoResponse(BaseModel):
    id_bao_cao : str
    noi_dung : str
    ten_nguoi_gui : str
    id_nguoi_gui : str
    ngay_gui : datetime
    noi_dung_phan_hoi : str