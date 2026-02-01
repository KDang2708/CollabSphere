#REPOSITORY: MeetingRepository (De truy cap du lieu cuoc hop)

# Vai tro:
#- Chiu trach nhiem luu tru du lieu va truy xuat du lieu cuoc hop 
#- Thuc hien cac phep toan CRUD cho entity Meeting (Create, Read, Update, Delete)
#_ Tang duy nhat lam viec voi datebase

# Yeu Cau:
#- Su dung SQLAlchemy session de tuong tac voi database
#- Anh xa Meeting entity sang MeetingModel de luu tru
#- Khong chua logic nghiep vu

from domain.models.imeet_repository import IMeetRepository
from domain.models.meet import Meeting
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.meet_model import MeetingModel
from infrastructure.databases.mssql import session
from infrastructure.databases.factory_database import FactoryDatabase as db_factory
load_dotenv()
class MeetingRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_meeting(self, meeting_model: MeetingModel) -> MeetingModel:
        """
        Thêm một cuộc họp mới vào cơ sở dữ liệu.
        """
        self.db_session.add(meeting_model)
        self.db_session.commit()
        self.db_session.refresh(meeting_model)
        return meeting_model
    def get_meeting_by_id(self, meeting_id: int) -> MeetingModel:
        """
        Lấy một cuộc họp theo ID từ cơ sở dữ liệu.
        """
        return self.db_session.query(MeetingModel).filter(MeetingModel.id == meeting_id).first()
    def delete_meeting(self, meeting_id: int) -> None:
        """
        Xóa một cuộc họp khỏi cơ sở dữ liệu theo ID.
        """
        meeting = self.get_meeting_by_id(meeting_id)
        if meeting:
            self.db_session.delete(meeting)
            self.db_session.commit()
    def update_meeting(self, meeting_id: int, **kwargs) -> MeetingModel:
        """
        Cập nhật thông tin cuộc họp theo ID.
        """
        meeting = self.get_meeting_by_id(meeting_id)
        if meeting:
            for key, value in kwargs.items():
                setattr(meeting, key, value)
            self.db_session.commit()
            self.db_session.refresh(meeting)
        return meeting
    
    def list_meetings(self) -> list[MeetingModel]:
        """
        Lấy danh sách tất cả các cuộc họp từ cơ sở dữ liệu.
        """
        return self.db_session.query(MeetingModel).all()
    
    def find_meetings_by_class_id(self, class_id: str) -> list[MeetingModel]:
        """
        Tìm các cuộc họp theo ID lớp học.
        """
        return self.db_session.query(MeetingModel).filter(MeetingModel.class_id == class_id).all()
    def find_meetings_by_group_id(self, group_id: str) -> list[MeetingModel]:
        """
        Tìm các cuộc họp theo ID nhóm.
        """
        return self.db_session.query(MeetingModel).filter(MeetingModel.group_id == group_id).all()
    
    def count_meetings(self) -> int:
        """
        Đếm tổng số cuộc họp trong cơ sở dữ liệu.
        """
        return self.db_session.query(MeetingModel).count()
    
            