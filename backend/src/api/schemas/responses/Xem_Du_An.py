from pydantic import BaseModel , Field

class XemDuAnResponse(BaseModel):
    id_du_an : str
    noi_dung : str
    trang_thai : bool
    id_giang_vien : str
    ten_giang_vien : str