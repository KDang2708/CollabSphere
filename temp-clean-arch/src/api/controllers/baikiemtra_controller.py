from flask import Blueprint, request, jsonify
from services.baikiemtra_services import BaiKiemTraService
from infrastructure.repositories.baikiemtra_repositories import BaiKiemTraRepository
from infrastructure.databases.mssql import session
from types import SimpleNamespace
from datetime import datetime

bp = Blueprint("baikiemtra", __name__, url_prefix="/api/baikiemtra")

# Dependency Injection
bai_kiem_tra_service = BaiKiemTraService(BaiKiemTraRepository(session))


@bp.route("/duan/<string:id_du_an>", methods=["GET"])
def lay_danh_sach_bai_kiem_tra_theo_du_an(id_du_an):
    danh_sach = bai_kiem_tra_service.list_by_du_an(id_du_an)
    return jsonify([
        {
            "id": bkt.id,
            "ten_bai_kiem_tra": bkt.ten_bai_kiem_tra,
            "trang_thai": bkt.trang_thai,
            "thoi_gian_lam_bai": bkt.thoi_gian_lam_bai,
            "mo_ta": bkt.mo_ta
        } for bkt in danh_sach
    ]), 200


@bp.route("/<string:id_bai_kiem_tra>", methods=["GET"])
def lay_bai_kiem_tra_theo_id(id_bai_kiem_tra):
    try:
        bkt = bai_kiem_tra_service.get_bai_kiem_tra(id_bai_kiem_tra)
        return jsonify({
            "id": bkt.id,
            "id_du_an": bkt.id_du_an,
            "ten_bai_kiem_tra": bkt.ten_bai_kiem_tra,
            "mo_ta": bkt.mo_ta,
            "thoi_gian_lam_bai": bkt.thoi_gian_lam_bai,
            "trang_thai": bkt.trang_thai
        }), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/", methods=["POST"])
def tao_bai_kiem_tra():
    du_lieu = request.get_json()
    required_fields = ["id", "id_du_an", "ten_bai_kiem_tra", "thoi_gian_lam_bai"]

    if not du_lieu or any(field not in du_lieu for field in required_fields):
        return jsonify({"message": "Thiếu thông tin bắt buộc"}), 400

    now = datetime.utcnow()
    payload = SimpleNamespace(
        id=du_lieu["id"],
        id_du_an=du_lieu["id_du_an"],
        ten_bai_kiem_tra=du_lieu["ten_bai_kiem_tra"],
        mo_ta=du_lieu.get("mo_ta", ""),
        thoi_gian_lam_bai=du_lieu["thoi_gian_lam_bai"],
        trang_thai="CHUA_MO",
        created_at=now,
        updated_at=now
    )

    try:
        bkt = bai_kiem_tra_service.create_bai_kiem_tra(payload)
        return jsonify({
            "message": "Tạo bài kiểm tra thành công",
            "id": bkt.id
        }), 201
    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@bp.route("/<string:id_bai_kiem_tra>", methods=["PUT"])
def cap_nhat_bai_kiem_tra(id_bai_kiem_tra):
    du_lieu = request.get_json()
    if not du_lieu:
        return jsonify({"message": "Dữ liệu không hợp lệ"}), 400

    payload = SimpleNamespace(
        ten_bai_kiem_tra=du_lieu.get("ten_bai_kiem_tra"),
        mo_ta=du_lieu.get("mo_ta"),
        thoi_gian_lam_bai=du_lieu.get("thoi_gian_lam_bai"),
        trang_thai=du_lieu.get("trang_thai"),
        updated_at=datetime.utcnow()
    )

    try:
        bai_kiem_tra_service.update_bai_kiem_tra(id_bai_kiem_tra, payload)
        return jsonify({"message": "Cập nhật bài kiểm tra thành công"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/open/<string:id_bai_kiem_tra>", methods=["PUT"])
def mo_bai_kiem_tra(id_bai_kiem_tra):
    try:
        bai_kiem_tra_service.open_bai_kiem_tra(id_bai_kiem_tra)
        return jsonify({"message": "Mở bài kiểm tra thành công"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/close/<string:id_bai_kiem_tra>", methods=["PUT"])
def dong_bai_kiem_tra(id_bai_kiem_tra):
    try:
        bai_kiem_tra_service.close_bai_kiem_tra(id_bai_kiem_tra)
        return jsonify({"message": "Đóng bài kiểm tra thành công"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/<string:id_bai_kiem_tra>", methods=["DELETE"])
def xoa_bai_kiem_tra(id_bai_kiem_tra):
    try:
        bai_kiem_tra_service.delete_bai_kiem_tra(id_bai_kiem_tra)
        return "", 204
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
