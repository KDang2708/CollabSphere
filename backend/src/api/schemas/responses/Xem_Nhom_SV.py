from pydantic import BaseModel , Field

class SinhVienResponse(BaseModel):
    id_sinh_vien : str
    ten_sinh_vien : str

class XemNhomSVResponse(BaseModel):
    id_nhom : str
    danh_sach_sinh_vien : list[SinhVienResponse]
    