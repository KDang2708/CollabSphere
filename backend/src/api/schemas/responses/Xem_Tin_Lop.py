from pydantic import BaseModel , Field
class TinNhanResponse(BaseModel):
    noi_dung : str 
    id_tin_nhan : str
    ten_nguoi_gui : str