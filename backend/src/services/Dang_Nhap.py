from domain.models.Tai_Khoan.iTai_Khoan import ITaiKhoanRepository
from infrastructure.security.jwt import create_access_token

class DangNhapUseCase:
    def __init__(self, repo: ITaiKhoanRepository):
        self.repo = repo

    def execute(self, ten_dang_nhap: str, mat_khau: str ):
        tai_khoan = self.repo.get_by_ten_dang_nhap(ten_dang_nhap)
        if tai_khoan is None:
            raise Exception("Tài khoản không đúng !")
        if tai_khoan.trang_thai == False:
            raise Exception("Tài khoản đã bị khóa !")
        if tai_khoan.mat_khau != mat_khau:
            raise Exception("Sai mật khẩu !")
        token = create_access_token(
            {
                "id_tai_khoan" : tai_khoan.id ,
                "ten_dang_nhap" : tai_khoan.ten_dang_nhap,
                "vai_tro" : tai_khoan.vai_tro.value
            }
        )
        return token
    