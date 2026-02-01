"""
Import tất cả ORM models để Base.metadata có đủ bảng khi gọi create_all.
"""


def import_all_models():
    from infrastructure.models import Admin_Model  # noqa: F401
    from infrastructure.models import Bai_Kiem_Tra_Model  # noqa: F401
    from infrastructure.models import Bai_Lam_Model  # noqa: F401
    from infrastructure.models import Bao_Cao_Model  # noqa: F401
    from infrastructure.models import Cuoc_Hop_Model  # noqa: F401
    from infrastructure.models import Du_An_Model  # noqa: F401
    from infrastructure.models import Giang_Vien_Model  # noqa: F401
    from infrastructure.models import Lop_Hoc_Hoc_Sinh_Model  # noqa: F401
    from infrastructure.models import Lop_Hoc_Model  # noqa: F401
    from infrastructure.models import Moc_Quan_trong_Model  # noqa: F401
    from infrastructure.models import Mon_Hoc_Model  # noqa: F401
    from infrastructure.models import Nhan_Vien_Model  # noqa: F401
    from infrastructure.models import Nhan_Xet_Model  # noqa: F401
    from infrastructure.models import Nhiem_Vu_Model  # noqa: F401
    from infrastructure.models import Nhom_Hoc_Sinh_Model  # noqa: F401
    from infrastructure.models import Nhom_Model  # noqa: F401
    from infrastructure.models import Phan_Hoi_Model  # noqa: F401
    from infrastructure.models import Sinh_Vien_Model  # noqa: F401
    from infrastructure.models import Tai_Khoan_Model  # noqa: F401
    from infrastructure.models import Tin_Nhan_Model  # noqa: F401
    from infrastructure.models import Truong_Khoa_Model  # noqa: F401
