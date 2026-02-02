from pydantic import BaseModel , Field

class NopBaiRequest(BaseModel):
    noi_dung_bai_lam : str 
    loai_bai_lam : int 
    id_bai_kiem_tra : str 
    id_sinh_vien : str