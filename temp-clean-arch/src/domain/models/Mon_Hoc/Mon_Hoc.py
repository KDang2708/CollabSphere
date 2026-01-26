#Môn học(IDMonHoc(String), TenMonHoc(String), DeCuong(URL))
class MonHoc:
    def __init__(
            self, 
            ten: str, 
            de_cuong: str
        ):
        self.id = None  # ID sẽ được gán khi lưu vào cơ sở dữ liệu
        self.ten = ten
        self.de_cuong = de_cuong