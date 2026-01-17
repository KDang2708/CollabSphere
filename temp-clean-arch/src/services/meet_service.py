#USE CASE : create meeting(Tao/ Tham Gia cuoc hop)
# Service layer: MeetingService
# Vai tro:
#-Dieu phoi nghiep vu tao cuoc hop
#-Nhan cac entity meeting tu controller
#-Goi repository de luu tru du lieu cuoc hop
# Quy tac nghiep vu:
# - Mot cuoc hop phai co nguoi tao
# - Mot cuoc hop phai co thoi gian bat dau
# - Cuoc hop phai gan voi NHOM HOAC LOP HOC (IDNhom hoac IDLopHoc)
# - Khong chua code lien quan den database truc tiep 

# Yeu Cau:
#- chi lam viec voi entity va repository
#- khong import flask, SQLAlchemy 
#- khong xu ly request/response HTTP
from domain.models.meet import Meeting
from domain.models.imeet_repository import IMeetRepository
from typing import List, Optional

class MeetingService:
    def __init__(self, meet_repository: IMeetRepository):
        self.meet_repository = meet_repository

    def create_meeting(self, start_time: str, created_at: str, class_id: str, group_id: str) -> Meeting:
        # Tạo entity Meeting
        new_meeting = Meeting(
            id=0,  # ID sẽ được gán bởi database
            start_time=start_time,
            created_at=created_at,
            class_id=class_id,
            group_id=group_id
        )
        # Lưu trữ cuộc họp thông qua repository
        saved_meeting = self.meet_repository.add(new_meeting)
        return saved_meeting

    def get_meeting(self, meet_id: int) -> Optional[Meeting]:
        return self.meet_repository.get_by_id(meet_id)

    def list_meetings(self) -> List[Meeting]:
        return self.meet_repository.list()

    def update_meeting(self, meet: Meeting) -> Meeting:
        return self.meet_repository.update(meet)

    def delete_meeting(self, meet_id: int) -> None:
        self.meet_repository.delete(meet_id)