from pydantic import BaseModel , Field 
        # self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        # self.tieu_de = tieu_de
        # self.de_kiem_tra = de_kiem_tra
        # self.mon_hoc = mon_hoc
class BaiKiemTraResponse(BaseModel):
    id_bai_kiem_tra : str
    tieu_de : str
    de_kiem_tra : str

