from pydantic import BaseModel , Field

class TaoMocQuanTrongRequest(BaseModel):
    noi_dung : str 
    id_mon_hoc : str 
    loai_moc : str