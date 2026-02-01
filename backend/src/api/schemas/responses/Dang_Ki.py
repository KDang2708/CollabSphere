from pydantic import BaseModel


class DangKiResponse(BaseModel):
    id_tai_khoan: str
    ten_dang_nhap: str
    vai_tro : str
    trang_thai : str