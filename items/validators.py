from marshmallow import Schema, fields, validate, EXCLUDE


class GetItemValidationSchema(Schema):
    item_id = fields.Str(validate=validate.Regexp(
        regex=r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        error="Invalid UUID"
    ))

class GetItemsValidationSchema(Schema):
    completed = fields.Bool()
    class Meta:
            unknown = EXCLUDE