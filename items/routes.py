from . import bp
from db import db
from .models import Item
from .serializers import ItemSchema
from .validators import GetItemValidationSchema
from flask import request, abort
from marshmallow import ValidationError
import uuid


@bp.route('/', methods=['GET'])
def index():
    stmt = db.select(Item).order_by(Item.updated_at)
    items = db.session.execute(stmt).scalars().all()
    schema = ItemSchema(many=True)
    result = schema.dumps(items)
    return result

@bp.route('/<item_id>', methods=['GET'])
def show(item_id):
    try:
        path_params = GetItemValidationSchema().load(request.view_args)
    except ValidationError as err:
        return err.messages, 400

    item_uuid = uuid.UUID(path_params['item_id'])
    item = db.session.query(Item).filter(Item.uuid == item_uuid).first()
    if item == None:
        abort(404)

    schema = ItemSchema()
    result = schema.dumps(item)
    return result