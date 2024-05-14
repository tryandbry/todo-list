from marshmallow import Schema, fields


class ItemSchema(Schema):
    uuid = fields.UUID(data_key="itemId")
    name = fields.Str()
    completed = fields.Bool()
    created_at = fields.DateTime(data_key="createdAt")
    updated_at = fields.DateTime(data_key="updatedAt")