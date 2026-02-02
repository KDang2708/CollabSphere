from pydantic import BaseModel , Field
from datetime import datetime

class TaoNhiemVuRequest(BaseModel):
    noi_dung : str 
    id_sinh_vien_thuc_hien : str 
    id_nguoi_tao : str  
    vai_tro_nguoi_tao : int 
    ngay_bat_dau : datetime 
    ngay_ket_thuc : datetime