from sqlalchemy import Column, String, Date , Boolean # lấy các kiểu dữ liệu cần thiết từ sqlalchemy
from infrastructure.databases.base import Base
import uuid

class TaiKhoanORM(Base):
    __tablename__ = "tai_khoan"  # tên bảng trong cơ sở dữ liệu

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # cột ID, kiểu String, là khóa chính
    ten_dang_nhap = Column(String , unique=True)         # cột tên đăng nhập, kiểu String
    mat_khau = Column(String)              # cột mật khẩu, kiểu String
    vai_tro = Column(String)              #
    trang_thai = Column(Boolean, default=True)           # cột trạng thái, kiểu String