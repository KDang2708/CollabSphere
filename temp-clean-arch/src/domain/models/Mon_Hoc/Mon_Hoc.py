#Môn học(IDMonHoc(String), TenMonHoc(String), DeCuong(URL))
class MonHoc:
    def __init__(self,id : str | None,  ten: str, tin_chi:int, de_cuong: str):
        self.id = id  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.ten = ten
        self.tin_chi = tin_chi
        self.de_cuong = de_cuong