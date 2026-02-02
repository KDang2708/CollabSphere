from pydantic import BaseModel 
class TaiKhoanResponse(BaseModel):
    id_tai_khoan : str
    ten_dang_nhap : str
    vai_tro : str
    trang_thai : str




    #  self.id = id
    #     self.ten_dang_nhap = ten_dang_nhap
    #     self.mat_khau = mat_khau
    #     self.vai_tro = vai_tro
    #     self.trang_thai = True