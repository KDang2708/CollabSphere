from pydantic import BaseModel , Field

class TaoBaiKiemTraRequest(BaseModel):
    tieu_de :str 
    de_kiem_tra : str 
    id_mon_hoc : str