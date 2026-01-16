from marshmallow import Schema, fields

class MeetRequestSchema(Schema):
    start_time = fields.Str(required=True)
    class_id = fields.Str(required=True)
    group_id = fields.Str(required=True)
    
class MeetResponseSchema(Schema):
    id = fields.Int(required=True)
    start_time = fields.Str(required=True)
    created_at = fields.Str(required=True)
    class_id = fields.Str(required=True)
    group_id = fields.Str(required=True)    