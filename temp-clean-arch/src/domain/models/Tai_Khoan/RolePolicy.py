from domain.models.Tai_Khoan.Vai_Tro import VaiTro
from domain.models.Tai_Khoan.Quyen import Quyen

ROLE_PERMISSIONS = {
    VaiTro.ADMIN: {
        Quyen.DOC_BAO_CAO,
        Quyen.VIET_PHAN_HOI,
        Quyen.XEM_TAI_KHOAN,
        Quyen.KHOA_TAI_KHOAN,
        Quyen.MO_TAI_KHOAN,
        Quyen.XOA_TAI_KHOAN,
    },
    VaiTro.GIANG_VIEN: {
        Quyen.DOC_BAO_CAO,
    },
    VaiTro.SINH_VIEN: set(),
}