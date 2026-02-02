from pydantic import BaseModel
from typing import List

class LopHocResponse(BaseModel):
    id_lop_hoc: str
    ten_lop_hoc: str

class MocQuanTrongResponse(BaseModel):
    id: str
    noi_dung: str

class BaiKiemTraResponse(BaseModel):
    id: str
    ten_bai_kiem_tra: str
class XemThongTinLopHocResponse(BaseModel):
    lop_hoc: LopHocResponse
    ds_moc_quan_trong: List[MocQuanTrongResponse]
    ds_bai_kiem_tra: List[BaiKiemTraResponse]
