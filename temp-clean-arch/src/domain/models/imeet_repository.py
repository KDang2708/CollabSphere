from abc import ABC, abstractmethod
from .meet import Meeting
from typing import Optional
from typing import List
class IMeetRepository(ABC):
    @abstractmethod
    def add(self, meet: Meeting) -> Meeting:
        pass

    @abstractmethod
    def get_by_id(self, meet_id: int) -> Optional[Meeting]:
        pass

    @abstractmethod
    def list(self) -> List[Meeting]:
        pass

    @abstractmethod
    def update(self, meet: Meeting) -> Meeting:
        pass

    @abstractmethod
    def delete(self, meet_id: int) -> None:
        pass