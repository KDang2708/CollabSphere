from pydantic import BaseModel , Field

class TaoDuAnRespone(BaseModel):
    id_du_an : str
    noi_dung : str
    trang_thai : bool
    id_giang_vien : str
    ten_giang_vien : str




        #     self.id = id
        # self.noi_dung = noi_dung
        # self.trang_thai = trang_thai
        # self.nguoi_tao = nguoi_tao
        # self.lop_hoc = lop_hoc
