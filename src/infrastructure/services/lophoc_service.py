from infrastructure.repositories.lophoc_repository import LopHocRepository
from infrastructure.models.lophoc_model import LopHocModel

class LopHocService:
    def __init__(self, repository: LopHocRepository = None):
        self.repository = repository or LopHocRepository()

    def create_lophoc(self, lophoc_data) -> LopHocModel:
        return self.repository.add(lophoc_data)

    def get_lophoc(self, lophoc_id: str) -> LopHocModel:
        return self.repository.get_by_id(lophoc_id)

    def get_all_lophoc(self):
        return self.repository.list()

    def update_lophoc(self, lophoc_data) -> LopHocModel:
        return self.repository.update(lophoc_data)

    def delete_lophoc(self, lophoc_id: str):
        return self.repository.delete(lophoc_id)