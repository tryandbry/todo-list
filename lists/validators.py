from marshmallow import Schema, fields, validate, ValidationError


class PostListValidationSchema(Schema):
    name = fields.Str(validate=validate.Length(min=0, max=60))

class GetListValidationSchema(Schema):
    list_id = fields.Str(validate=validate.Regexp(
        regex=r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        error="Invalid UUID"
    ))