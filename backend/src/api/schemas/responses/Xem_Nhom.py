from pydantic import BaseModel , Field

class SinhVien(BaseModel):
    id_sinh_vien : str
    ten_sinh_vien : str
class XemNhomResponse(BaseModel):
    id_nhom : str
    danh_sach_sinh_vien : list[SinhVien]