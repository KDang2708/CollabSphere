from flask import Blueprint, request, jsonify
from services.duan_service import DuAnService
from infrastructure.repositories.duan_repository import DuAnRepository
from infrastructure.databases.mssql import session
from types import SimpleNamespace

# Khởi tạo Blueprint cho Dự Án
bp = Blueprint("duan", __name__, url_prefix="/api/duan")

# Khởi tạo Service
du_an_service = DuAnService(DuAnRepository(session))


@bp.route("/", methods=["GET"])
def lay_danh_sach_du_an():
    """
    Lấy danh sách tất cả dự án
    """
    danh_sach_du_an = du_an_service.get_all_du_an()
    return jsonify([
        {
            "id": du_an.id,
            "ten_du_an": du_an.ten_du_an,
            "mo_ta": du_an.mo_ta,
            "trang_thai": du_an.trang_thai
        } for du_an in danh_sach_du_an
    ]), 200


@bp.route("/<string:id_du_an>", methods=["GET"])
def lay_du_an_theo_id(id_du_an):
    """
    Lấy thông tin dự án theo ID
    """
    try:
        du_an = du_an_service.get_du_an(id_du_an)
        return jsonify({
            "id": du_an.id,
            "ten_du_an": du_an.ten_du_an,
            "mo_ta": du_an.mo_ta,
            "trang_thai": du_an.trang_thai
        }), 200
    except ValueError as loi:
        return jsonify({"message": str(loi)}), 404


@bp.route("/", methods=["POST"])
def tao_du_an():
    """
    Tạo dự án mới
    """
    du_lieu = request.get_json()

    payload = SimpleNamespace(
        id=du_lieu["id"],
        ten_du_an=du_lieu["ten_du_an"],
        mo_ta=du_lieu.get("mo_ta", "")
    )

    du_an = du_an_service.create_du_an(payload)
    return jsonify({
        "message": "Tạo dự án thành công",
        "id": du_an.id
    }), 201


@bp.route("/<string:id_du_an>", methods=["PUT"])
def cap_nhat_du_an(id_du_an):
    """
    Cập nhật thông tin dự án
    """
    du_lieu = request.get_json()

    payload = SimpleNamespace(
        ten_du_an=du_lieu["ten_du_an"],
        mo_ta=du_lieu.get("mo_ta", ""),
        trang_thai=du_lieu.get("trang_thai", "DANG_THUC_HIEN")
    )

    du_an_service.update_du_an(id_du_an, payload)
    return jsonify({"message": "Cập nhật dự án thành công"}), 200


@bp.route("/close/<string:id_du_an>", methods=["PUT"])
def dong_du_an(id_du_an):
    """
    Đóng dự án
    """
    du_an_service.close_du_an(id_du_an)
    return jsonify({"message": "Đã đóng dự án"}), 200


@bp.route("/<string:id_du_an>", methods=["DELETE"])
def xoa_du_an(id_du_an):
    """
    Xóa dự án
    """
    du_an_service.delete_du_an(id_du_an)
    return "", 204
