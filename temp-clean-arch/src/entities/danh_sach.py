from typing import List


class DanhSach:
    def __init__(self):
        self.items: List = []

    def them(self, item):
        self.items.append(item)

    def lay_danh_sach(self):
        return self.items
