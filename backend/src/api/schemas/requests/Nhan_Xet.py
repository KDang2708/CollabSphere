from pydantic import BaseModel , Field

class NhanXetRequest(BaseModel):
    noi_dung_nhan_xet : str 
    id_giang_vien : str 
    id_bai_lam : str