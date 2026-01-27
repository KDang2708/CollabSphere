from flask import Blueprint, request, jsonify
from services.du_an_service import DuAnService
from infrastructure.repositories.du_an_repository import DuAnRepository
from domain.models.Giang_Vien.Giang_Vien import GiangVien

bp = Blueprint("du_an", __name__, url_prefix="/du-an")

# Khởi tạo service
du_an_service = DuAnService(DuAnRepository())

# Lấy Danh Sách Dự Án
@bp.route("/", methods=["GET"])
def List_du_an():
    """
    Get all projects
    ---
    get:
      summary: Lấy danh sách dự án
      tags:
        - DuAn
      responses:
        200:
          description: Danh sách dự án
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                    noi_dung:
                      type: string
                    trang_thai:
                      type: boolean
                    id_nguoi_tao:
                      type: string
    """
    du_ans = du_an_service.get_all()

    return jsonify([
        {
            "id": d.id,
            "noi_dung": d.noi_dung,
            "trang_thai": d.trang_thai,
            "id_nguoi_tao": d.nguoi_tao.id if d.nguoi_tao else None
        }
        for d in du_ans
    ]), 200

# Lấy chi tiết dự án
@bp.route("/<string:id>", methods=["GET"])
def get_du_an(id):
    """
    Get project by id
    ---
    get:
      summary: Lấy chi tiết dự án theo ID
      tags:
        - DuAn
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        200:
          description: Chi tiết dự án
        404:
          description: Không tìm thấy dự án
    """
    du_an = du_an_service.get_by_id(id)
    if not du_an:
        return jsonify({"message": "Không tìm thấy dự án"}), 404

    return jsonify({
        "id": du_an.id,
        "noi_dung": du_an.noi_dung,
        "trang_thai": du_an.trang_thai,
        "id_nguoi_tao": du_an.nguoi_tao.id if du_an.nguoi_tao else None
    }), 200

# Tạo dự án mới (GIẢNG VIÊN tạo)
@bp.route("/", methods=["POST"])
def create_du_an():
    """
    Create a new project
    ---
    post:
      summary: Tạo dự án mới
      tags:
        - DuAn
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                noi_dung:
                  type: string
                id_nguoi_tao:
                  type: string
      responses:
        201:
          description: Tạo dự án thành công
        400:
          description: Thiếu dữ liệu
    """
    data = request.get_json()

    if not data or "noi_dung" not in data or "id_nguoi_tao" not in data:
        return jsonify({"message": "Thiếu dữ liệu"}), 400

    # Tạo GiangVien reference (ID-only)
    giang_vien = GiangVien(id=data["id_nguoi_tao"])

    du_an = du_an_service.create(
        noi_dung=data["noi_dung"],
        nguoi_tao=giang_vien
    )

    return jsonify({
        "id": du_an.id,
        "noi_dung": du_an.noi_dung,
        "trang_thai": du_an.trang_thai,
        "id_nguoi_tao": du_an.nguoi_tao.id
    }), 201

# Duyệt dự án (trưởng khoa)
@bp.route("/<string:id>/duyet", methods=["PUT"])
def duyet_du_an(id):
    """
    Approve project
    ---
    put:
      summary: Duyệt dự án
      tags:
        - DuAn
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        200:
          description: Duyệt thành công
        404:
          description: Không tìm thấy dự án
    """
    du_an = du_an_service.duyet(id)
    if not du_an:
        return jsonify({"message": "Không tìm thấy dự án"}), 404

    return jsonify({
        "message": "Dự án đã được duyệt",
        "id": du_an.id
    }), 200
