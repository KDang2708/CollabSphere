from pydantic import BaseModel , Field

class TaoDuAnRequest(BaseModel):
    noi_dung : str = Field(...,max_length=500)
    id_giang_vien : str = Field(...,)