from flask import Blueprint, request, jsonify
from services.lophoc_service import LopHocService
from infrastructure.repositories.lophoc_repository import LopHocRepository
from datetime import datetime
from infrastructure.databases.mssql import session

# Khởi tạo Blueprint cho Lớp học
bp = Blueprint('lophoc', __name__, url_prefix='/api/lophoc')
lophoc_service = LopHocService(LopHocRepository(session))

@bp.route('/', methods=['GET'])
def list_lophocs():
    """
    Lấy danh sách tất cả lớp học
    ---
    tags:
      - Lớp Học
    responses:
      200:
        description: Danh sách lớp học
    """
    lophocs = lophoc_service.get_all_lophoc()
    return jsonify([{"id": l.id, "id_mon_hoc": l.id_mon_hoc, "si_so": l.si_so} for l in lophocs]), 200

@bp.route('/<string:lophoc_id>', methods=['GET'])
def get_lophoc(lophoc_id):
    """
    Lấy thông tin lớp học theo ID
    ---
    tags:
      - Lớp Học
    parameters:
      - name: lophoc_id
        in: path
        required: true
        schema:
          type: string
    responses:
      200:
        description: Thông tin lớp học
      404:
        description: LopHoc not found
    """
    lophoc = lophoc_service.get_lophoc(lophoc_id)
    if not lophoc:
        return jsonify({'message': 'LopHoc not found'}), 404
    return jsonify({"id": lophoc.id, "id_mon_hoc": lophoc.id_mon_hoc, "si_so": lophoc.si_so}), 200

@bp.route('/', methods=['POST'])
def create_lophoc():
    """
    Tạo một lớp học mới
    ---
    tags:
      - Lớp Học
    responses:
      201:
        description: Tạo thành công
    """
    data = request.get_json()
    from types import SimpleNamespace
    now = datetime.utcnow()
    lophoc_data = SimpleNamespace(
        id=data['id'],
        id_mon_hoc=data['id_mon_hoc'],
        si_so=data.get('si_so', 0),
        id_giang_vien=data.get('id_giang_vien'),
        created_at=now,
        updated_at=now
    )
    result = lophoc_service.create_lophoc(lophoc_data)
    return jsonify({"message": "Lớp học đã được tạo", "id": result.id}), 201

@bp.route('/<string:lophoc_id>', methods=['DELETE'])
def delete_lophoc(lophoc_id):
    """
    Xóa lớp học theo ID
    ---
    tags:
      - Lớp Học
    responses:
      204:
        description: Xóa thành công
    """
    lophoc_service.delete_lophoc(lophoc_id)
    return '', 204