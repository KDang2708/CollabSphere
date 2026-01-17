from flask import Blueprint, request, jsonify
from services.duan_service import DuAnService
from infrastructure.repositories.duan_repository import DuAnRepository
from infrastructure.databases.mssql import session
from types import SimpleNamespace

bp = Blueprint("duan", __name__, url_prefix="/api/duan")
service = DuAnService(DuAnRepository(session))


@bp.route("/", methods=["GET"])
def list_du_an():
    duans = service.get_all_du_an()
    return jsonify([
        {
            "id": d.id,
            "ten_du_an": d.ten_du_an,
            "mo_ta": d.mo_ta,
            "trang_thai": d.trang_thai
        } for d in duans
    ]), 200


@bp.route("/<string:id>", methods=["GET"])
def get_du_an(id):
    try:
        d = service.get_du_an(id)
        return jsonify({
            "id": d.id,
            "ten_du_an": d.ten_du_an,
            "mo_ta": d.mo_ta,
            "trang_thai": d.trang_thai
        }), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/", methods=["POST"])
def create_du_an():
    data = request.get_json()
    payload = SimpleNamespace(
        id=data["id"],
        ten_du_an=data["ten_du_an"],
        mo_ta=data.get("mo_ta", "")
    )
    duan = service.create_du_an(payload)
    return jsonify({"message": "Tạo dự án thành công", "id": duan.id}), 201


@bp.route("/<string:id>", methods=["PUT"])
def update_du_an(id):
    data = request.get_json()
    payload = SimpleNamespace(
        ten_du_an=data["ten_du_an"],
        mo_ta=data.get("mo_ta", ""),
        trang_thai=data.get("trang_thai", "DANG_THUC_HIEN")
    )
    duan = service.update_du_an(id, payload)
    return jsonify({"message": "Cập nhật thành công"}), 200


@bp.route("/close/<string:id>", methods=["PUT"])
def close_du_an(id):
    service.close_du_an(id)
    return jsonify({"message": "Đã đóng dự án"}), 200


@bp.route("/<string:id>", methods=["DELETE"])
def delete_du_an(id):
    service.delete_du_an(id)
    return "", 204
