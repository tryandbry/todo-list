from marshmallow import Schema, fields


class ListSchema(Schema):
    uuid = fields.UUID(data_key="listId")
    name = fields.Str()
    created_at = fields.DateTime(data_key="createdAt")
    updated_at = fields.DateTime(data_key="updatedAt")