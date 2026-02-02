class NhanTinResponse(BaseModel):
    id_tin_nhan: str
    noi_dung: str
    ten_nguoi_gui: str
    id_lop_hoc: str
    id_nhom: str | None
