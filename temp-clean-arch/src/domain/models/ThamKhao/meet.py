# meet đê lưu trữ thông tin về một cuộc họp trong hệ thống
from sqlalchemy import String, DateTime
class Meeting:
    def __init__(self, id_meet: int, thoigianbatdau: DateTime, id_nguoitao: String, id_lop: String, id_nhom: String):
        self.id_meet = id_meet
        self.thoigianbatdau = thoigianbatdau
        self.id_nguoitao = id_nguoitao
        self.id_lop= id_lop
        self.id_nhom= id_nhom