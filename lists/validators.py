from marshmallow import Schema, fields, validate


class ListValidationSchema(Schema):
    name = fields.Str(validate=validate.Length(min=0, max=60))