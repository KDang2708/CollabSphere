from flask import Blueprint, request, jsonify
from services.baikiemtra_service import BaiKiemTraService
from infrastructure.repositories.baikiemtra_repository import BaiKiemTraRepository
from infrastructure.databases.mssql import session
from datetime import datetime
from types import SimpleNamespace

# Khởi tạo Blueprint
bp = Blueprint("baikiemtra", __name__, url_prefix="/api/baikiemtra")

# Khởi tạo Service (Dependency Injection thủ công)
bai_kiem_tra_service = BaiKiemTraService(
    BaiKiemTraRepository(session)
)

# --- ROUTES ---

@bp.route("/duan/<string:id_du_an>", methods=["GET"])
def lay_danh_sach_bai_kiem_tra_theo_du_an(id_du_an):
    """Lấy danh sách bài kiểm tra theo dự án"""
    try:
        danh_sach_bai_kiem_tra = bai_kiem_tra_service.list_by_du_an(id_du_an)
        return jsonify([
            {
                "id": bkt.id,
                "ten_bai_kiem_tra": bkt.ten_bai_kiem_tra,
                "trang_thai": bkt.trang_thai,
                "thoi_gian_lam_bai": bkt.thoi_gian_lam_bai,
                "mo_ta": bkt.mo_ta
            } for bkt in danh_sach_bai_kiem_tra
        ]), 200
    except Exception as e:
        return jsonify({"message": "Lỗi khi lấy danh sách", "error": str(e)}), 500


@bp.route("/<string:id_bai_kiem_tra>", methods=["GET"])
def lay_bai_kiem_tra_theo_id(id_bai_kiem_tra):
    """Lấy thông tin chi tiết bài kiểm tra"""
    bai_kiem_tra = bai_kiem_tra_service.get_bai_kiem_tra(id_bai_kiem_tra)
    if not bai_kiem_tra:
        return jsonify({"message": "Không tìm thấy bài kiểm tra"}), 404

    return jsonify({
        "id": bai_kiem_tra.id,
        "id_du_an": bai_kiem_tra.id_du_an,
        "ten_bai_kiem_tra": bai_kiem_tra.ten_bai_kiem_tra,
        "mo_ta": bai_kiem_tra.mo_ta,
        "thoi_gian_lam_bai": bai_kiem_tra.thoi_gian_lam_bai,
        "trang_thai": bai_kiem_tra.trang_thai
    }), 200


@bp.route("/", methods=["POST"])
def tao_bai_kiem_tra():
    """Tạo bài kiểm tra mới"""
    du_lieu = request.get_json()

    # Kiểm tra các trường bắt buộc
    required_fields = ["id", "id_du_an", "ten_bai_kiem_tra", "thoi_gian_lam_bai"]
    for field in required_fields:
        if field not in du_lieu:
            return jsonify({"message": f"Thiếu thông tin: {field}"}), 400

    try:
        thoi_gian_hien_tai = datetime.utcnow()
        payload = SimpleNamespace(
            id=du_lieu["id"],
            id_du_an=du_lieu["id_du_an"],
            ten_bai_kiem_tra=du_lieu["ten_bai_kiem_tra"],
            mo_ta=du_lieu.get("mo_ta", ""),
            thoi_gian_lam_bai=du_lieu["thoi_gian_lam_bai"],
            trang_thai="CHUA_MO",
            created_at=thoi_gian_hien_tai,
            updated_at=thoi_gian_hien_tai
        )

        bai_kiem_tra = bai_kiem_tra_service.create_bai_kiem_tra(payload)
        return jsonify({
            "message": "Tạo bài kiểm tra thành công",
            "id": bai_kiem_tra.id
        }), 201
    except Exception as e:
        return jsonify({"message": "Lỗi server khi tạo bài kiểm tra", "error": str(e)}), 500


@bp.route("/<string:id_bai_kiem_tra>", methods=["PUT"])
def cap_nhat_bai_kiem_tra(id_bai_kiem_tra):
    """Cập nhật thông tin bài kiểm tra"""
    du_lieu = request.get_json()
    try:
        # Giả sử service có hàm update_bai_kiem_tra nhận vào ID và dictionary dữ liệu mới
        bai_kiem_tra = bai_kiem_tra_service.update_bai_kiem_tra(id_bai_kiem_tra, du_lieu)
        if not bai_kiem_tra:
             return jsonify({"message": "Không tìm thấy bài kiểm tra để cập nhật"}), 404
             
        return jsonify({"message": "Cập nhật thành công"}), 200
    except Exception as e:
        return jsonify({"message": "Lỗi khi cập nhật", "error": str(e)}), 500


@bp.route("/open/<string:id_bai_kiem_tra>", methods=["PUT"])
def mo_bai_kiem_tra(id_bai_kiem_tra):
    """Mở bài kiểm tra"""
    try:
        bai_kiem_tra_service.open_bai_kiem_tra(id_bai_kiem_tra)
        return jsonify({"message": "Mở bài kiểm tra thành công"}), 200
    except Exception as e:
        return jsonify({"message": "Lỗi khi mở bài kiểm tra", "error": str(e)}), 500


@bp.route("/close/<string:id_bai_kiem_tra>", methods=["PUT"])
def dong_bai_kiem_tra(id_bai_kiem_tra):
    """Đóng bài kiểm tra"""
    try:
        bai_kiem_tra_service.close_bai_kiem_tra(id_bai_kiem_tra)
        return jsonify({"message": "Đóng bài kiểm tra thành công"}), 200
    except Exception as e:
        return jsonify({"message": "Lỗi khi đóng bài kiểm tra", "error": str(e)}), 500


@bp.route("/<string:id_bai_kiem_tra>", methods=["DELETE"])
def xoa_bai_kiem_tra(id_bai_kiem_tra):
    """Xóa bài kiểm tra"""
    try:
        success = bai_kiem_tra_service.delete_bai_kiem_tra(id_bai_kiem_tra)
        if not success:
            return jsonify({"message": "Không tìm thấy bài kiểm tra để xóa"}), 404
        return "", 204
    except Exception as e:
        return jsonify({"message": "Lỗi khi xóa", "error": str(e)}), 500