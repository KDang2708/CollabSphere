# CONTROLLER: MeetingController (Xu Ly Cac Yeu Cau Tu Phia Nguoi Dung Va Goi Cac Service Tuong Ung)
#vai tro:
#- Nhan request tu nguoi dung
#- Chuyen du lieu tu request thanh entity Meeting
#- Goi MeetingService de xu ly nghiep vu lien quan den cuoc hop
#- Tra ve response cho nguoi dung

#endpoint:
# POST /meetings: Tao cuoc hop moi
# GET /meetings/<id>: Lay thong tin cuoc hop theo ID
# PUT /meetings/<id>: Cap nhat thong tin cuoc hop
# DELETE /meetings/<id>: Xoa cuoc hop theo ID

#yeu cau:
#- Chi Goi Service Va Tra Ve Response 
#- khong Truy Cap Database truc tiep
from flask import Blueprint, request, jsonify
from services.meet_service import MeetingService
from infrastructure.repositories.todo_repository import TodoRepository
from api.schemas.meet import MeetRequestSchema, MeetResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('meeting', __name__, url_prefix='/meetings')
meeting_service = MeetingService(TodoRepository(session))
request_schema = MeetRequestSchema()
response_schema = MeetResponseSchema()
@bp.route('/', methods=['POST'])
def create_meeting():
    """
    Tạo cuộc họp mới
    ---
    post:
      summary: Tạo cuộc họp mới
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MeetRequest'
        responses:
            201:
                description: Cuộc họp được tạo thành công
                content:
                application/json:
                    schema:
                    $ref: '#/components/schemas/MeetResponse'
            400:
                description: Yêu cầu không hợp lệ
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    start_time = datetime.fromisoformat(data['start_time'])
    created_at = data['created_at']
    class_id = data['class_id']
    group_id = data['group_id']

    meeting = meeting_service.create_meeting(
        start_time=start_time,
        created_at=created_at,
        class_id=class_id,
        group_id=group_id
    )

    return jsonify(response_schema.dump(meeting)), 201
@bp.route('/<int:meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    """
    Lấy thông tin cuộc họp theo ID
    ---
    get:
      summary: Lấy thông tin cuộc họp theo ID
      parameters:
        - name: meeting_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của cuộc họp cần lấy
      responses:
        200:
          description: Thông tin cuộc họp
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MeetResponse'
        404:
          description: Cuộc họp không tìm thấy
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
    """
    meeting = meeting_service.get_meeting_by_id(meeting_id)
    if not meeting:
        return jsonify({'error': 'Cuộc họp không tìm thấy'}), 404
    return jsonify(response_schema.dump(meeting)), 200
@bp.route('/<int:meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    """
    Xóa cuộc họp theo ID
    ---
    delete:
      summary: Xóa cuộc họp theo ID
      parameters:
        - name: meeting_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của cuộc họp cần xóa
      responses:
        204:
          description: Cuộc họp đã được xóa thành công
        404:
          description: Cuộc họp không tìm thấy
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
    """
    success = meeting_service.delete_meeting(meeting_id)
    if not success:
        return jsonify({'error': 'Cuộc họp không tìm thấy'}), 404
    return '', 204
@bp.route('/<int:meeting_id>', methods=['PUT'])
def update_meeting(meeting_id):
    """
    Cập nhật thông tin cuộc họp theo ID
    ---
    put:
      summary: Cập nhật thông tin cuộc họp theo ID
      parameters:
        - name: meeting_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của cuộc họp cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MeetRequest'
        responses:
            200:
                description: Cuộc họp được cập nhật thành công
                content:
                application/json:
                    schema:
                    $ref: '#/components/schemas/MeetResponse'
            400:
                description: Yêu cầu không hợp lệ
            404:
                description: Cuộc họp không tìm thấy
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    start_time = datetime.fromisoformat(data['start_time'])
    created_at = data['created_at']
    class_id = data['class_id']
    group_id = data['group_id']

    meeting = meeting_service.update_meeting(
        meeting_id=meeting_id,
        start_time=start_time,
        created_at=created_at,
        class_id=class_id,
        group_id=group_id
    )

    if not meeting:
        return jsonify({'error': 'Cuộc họp không tìm thấy'}), 404

    return jsonify(response_schema.dump(meeting)), 200
@bp.route('/', methods=['GET'])
def list_meetings():
    """
    Lấy danh sách tất cả các cuộc họp
    ---
    get:
      summary: Lấy danh sách tất cả các cuộc họp
      responses:
        200:
          description: Danh sách cuộc họp
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/MeetResponse'
    """
    meetings = meeting_service.list_meetings()
    return jsonify(response_schema.dump(meetings, many=True)), 200
@bp.route('/count', methods=['GET'])
def count_meetings():
    """
    Đếm tổng số cuộc họp
    ---
    get:
      summary: Đếm tổng số cuộc họp
      responses:
        200:
          description: Tổng số cuộc họp
          content:
            application/json:
              schema:
                type: object
                properties:
                  count:
                    type: integer
    """
    count = meeting_service.count_meetings()
    return jsonify({'count': count}), 200
