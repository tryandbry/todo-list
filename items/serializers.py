from marshmallow import Schema, fields
from lists.serializers import ListSchema


class ItemSchema(Schema):
    uuid = fields.UUID(data_key="itemId")
    name = fields.Str()
    completed = fields.Bool()
    list = fields.Nested(ListSchema(only=("uuid",)))
    created_at = fields.DateTime(data_key="createdAt")
    updated_at = fields.DateTime(data_key="updatedAt")
