class LopHoc:
    def __init__(self, id, id_mon_hoc, si_so=0, id_giang_vien=None):
        self.id = id
        self.id_mon_hoc = id_mon_hoc
        self.si_so = si_so
        self.id_giang_vien = id_giang_vien

    def cap_nhat_si_so(self, si_so):
        self.si_so = si_so
