from pydantic import BaseModel , Field
class SinhVienResponse(BaseModel):
    id_sinh_vien : str
    ten_sinh_vien : str
class XemChiTietLopHocResponse(BaseModel):
    id_lop_hoc : str
    id_mon_hoc : str
    ten_mon_hoc : str
    de_cuong : str
    id_giang_vien : str
    ten_giang_vien : str
    danh_sach_sinh_vien : list[SinhVienResponse]



    


    