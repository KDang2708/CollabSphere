class DanhSach:
    def __init__(self):
        self.items = []

    def them(self, item):
        self.items.append(item)

    def xoa(self, item):
        self.items.remove(item)

    def lay_tat_ca(self):
        return self.items
