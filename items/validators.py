from marshmallow import Schema, fields, EXCLUDE 


class GetItemsValidationSchema(Schema):
    completed = fields.Bool()
    class Meta:
            unknown = EXCLUDE