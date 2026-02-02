from pydantic import BaseModel , Field

class PhanHoiRequest(BaseModel):
    noi_dung : str = Field(...,max_length=255)
    id_bao_cao : str = Field(...,)