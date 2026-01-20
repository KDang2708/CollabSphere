# Dự án(IDDuAn(String), NoiDungDuAn(String), TrangThai(Bool), IDNguoiTao(String))
class DuAn:
    def __init__(self, NoiDungDuAn: str, TrangThai: bool, IDNguoiTao: str):
        self.IdDuAn = None                  # DB tự sinh id khi lưu dự án
        self.NoiDungDuAn = NoiDungDuAn
        self.TrangThai = TrangThai
        self.IDNguoiTao = IDNguoiTao