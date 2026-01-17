from flask import Blueprint, request, jsonify
from services.nhiemvu_service import NhiemVuService
from infrastructure.repositories.nhiemvu_repository import NhiemVuRepository
from infrastructure.databases.mssql import session
from datetime import datetime
from types import SimpleNamespace

bp = Blueprint("nhiemvu", __name__, url_prefix="/api/nhiemvu")

nhiem_vu_service = NhiemVuService(NhiemVuRepository(session))


@bp.route("/duan/<string:id_du_an>", methods=["GET"])
def lay_nhiem_vu_theo_du_an(id_du_an):
    try:
        danh_sach = nhiem_vu_service.get_by_du_an(id_du_an)
        return jsonify([
            {
                "id": nv.id,
                "ten_nhiem_vu": nv.ten_nhiem_vu,
                "trang_thai": nv.trang_thai,
                "nguoi_thuc_hien": nv.nguoi_thuc_hien
            } for nv in danh_sach
        ]), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@bp.route("/<string:id_nhiem_vu>", methods=["GET"])
def lay_nhiem_vu_theo_id(id_nhiem_vu):
    try:
        nv = nhiem_vu_service.get_nhiem_vu(id_nhiem_vu)
        return jsonify({
            "id": nv.id,
            "ten_nhiem_vu": nv.ten_nhiem_vu,
            "mo_ta": nv.mo_ta,
            "trang_thai": nv.trang_thai,
            "nguoi_thuc_hien": nv.nguoi_thuc_hien
        }), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/", methods=["POST"])
def tao_nhiem_vu():
    du_lieu = request.get_json()
    if not du_lieu:
        return jsonify({"message": "Dữ liệu không hợp lệ"}), 400

    try:
        now = datetime.utcnow()
        payload = SimpleNamespace(
            id=du_lieu["id"],
            id_du_an=du_lieu["id_du_an"],
            ten_nhiem_vu=du_lieu["ten_nhiem_vu"],
            mo_ta=du_lieu.get("mo_ta", ""),
            trang_thai="MOI_TAO",
            nguoi_thuc_hien=None,
            created_at=now,
            updated_at=now
        )

        nv = nhiem_vu_service.create_nhiem_vu(payload)
        return jsonify({
            "message": "Tạo nhiệm vụ thành công",
            "id": nv.id
        }), 201

    except KeyError:
        return jsonify({"message": "Thiếu trường bắt buộc"}), 400


@bp.route("/assign/<string:id_nhiem_vu>", methods=["PUT"])
def phan_cong_nhiem_vu(id_nhiem_vu):
    du_lieu = request.get_json()
    if "nguoi_thuc_hien" not in du_lieu:
        return jsonify({"message": "Thiếu người thực hiện"}), 400

    try:
        nhiem_vu_service.assign_nhiem_vu(
            id_nhiem_vu,
            du_lieu["nguoi_thuc_hien"]
        )
        return jsonify({"message": "Phân công nhiệm vụ thành công"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/status/<string:id_nhiem_vu>", methods=["PUT"])
def cap_nhat_trang_thai(id_nhiem_vu):
    du_lieu = request.get_json()
    if "trang_thai" not in du_lieu:
        return jsonify({"message": "Thiếu trạng thái"}), 400

    try:
        nhiem_vu_service.update_status(id_nhiem_vu, du_lieu["trang_thai"])
        return jsonify({"message": "Cập nhật trạng thái thành công"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404


@bp.route("/<string:id_nhiem_vu>", methods=["DELETE"])
def xoa_nhiem_vu(id_nhiem_vu):
    try:
        nhiem_vu_service.delete_nhiem_vu(id_nhiem_vu)
        return "", 204
    except ValueError as e:
        return jsonify({"message": str(e)}), 404
