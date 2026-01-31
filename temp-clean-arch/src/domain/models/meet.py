# meet đê lưu trữ thông tin về một cuộc họp trong hệ thống
class Meeting:
    def __init__(self, id: int, start_time: str, created_at: str, class_id: str, group_id: str):
        self.id = id
        self.start_time = start_time
        self.created_at = created_at
        self.class_id = class_id
        self.group_id = group_id