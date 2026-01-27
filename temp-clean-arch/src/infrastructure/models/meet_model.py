# ENTITY: Meeting
# Mô Tả Nghiệp vụ
# Đại diện cho 1 cuộc họp trong hệ thống 
# chỉ chứa các mô hình dữ liệu  và quy tắc nghiệp vụ để ánh xạ dũ liệu cuộc họp
#khong phụ thuộc vào database, faramework hay thu vien ngoai
#Usecae "meeting" bao gom:
# <<boundary>> Form Giao Dien Tro chuyen
# <<control>> Controller Cuoc Hop
# <<subsystem>> Cuoc Hop

#Thuoc tinh:
# start_time: date + time (Khoa chinh) -> ThoiGianBatDau 
# created_at: str(10) (khoa ngoai) -> IDNguoiTao 
# class_id: str(10) (khoa ngoai) -> IDLopHoc
# group_id: str(10) (khoa ngoai) -> IDNhom

# yeucau: 
# CHi khoi tao tao va luu tru du lieu cuoc hop
# chi lam thuoc tinh theo yeu cau
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base

class MeetingModel(Base):
    __tablename__ = 'meetings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_time = Column(DateTime, nullable=False)
    created_at = Column(String(10), nullable=False)  # IDNguoiTao
    class_id = Column(String(10), nullable=False)  # IDLopHoc
    group_id = Column(String(10), nullable=False)  # IDNhom