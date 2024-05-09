from marshmallow import Schema, fields


class ListSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    created_at = fields.DateTime(data_key="createdAt")
    updated_at = fields.DateTime(data_key="updatedAt")