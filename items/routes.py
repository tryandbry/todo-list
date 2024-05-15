from . import bp
from db import db
from .models import Item
from .serializers import ItemSchema
from .validators import GetItemValidationSchema, PostItemValidationSchema, PatchItemValidationSchema
from flask import request, abort, Response
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

@bp.route('/<item_id>', methods=['PATCH'])
def update(item_id):
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type not supported!', 400

    try:
        path_params = GetItemValidationSchema().load(request.view_args)
        body_params = PatchItemValidationSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    item_uuid = uuid.UUID(path_params['item_id'])
    item = db.session.query(Item).filter(Item.uuid == item_uuid).first()
    if item == None:
        abort(404)

    if 'name' in body_params:
        item.name = body_params['name']

    if 'completed' in body_params:
        item.completed = body_params['completed']

    db.session.commit()
    schema = ItemSchema()
    result = schema.dumps(item)
    return result

@bp.route('/<item_id>', methods=['DELETE'])
def destroy(item_id):
    try:
        path_params = GetItemValidationSchema().load(request.view_args)
    except ValidationError as err:
        return err.messages, 400

    item_uuid = uuid.UUID(path_params['item_id'])
    item = db.session.query(Item).filter(Item.uuid == item_uuid).first()
    if item == None:
        abort(404)

    db.session.delete(item)
    db.session.commit()
    return Response(status=204)