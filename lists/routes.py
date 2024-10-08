from . import bp
from db import db
from .models import List
from .serializers import ListSchema
from .validators import GetListValidationSchema, PostListValidationSchema
from flask import request, abort, Response
from marshmallow import ValidationError
from items.nested_controllers import item_index_by_list, item_create_by_list
import uuid


@bp.route('/', methods=['GET'])
def index():
    stmt = db.select(List).order_by(List.updated_at)
    lists = db.session.execute(stmt).scalars().all()
    schema = ListSchema(many=True)
    result = schema.dumps(lists)
    return result


@bp.route('/<list_id>', methods=['GET'])
def show(list_id):
    try:
        path_params = GetListValidationSchema().load(request.view_args)
    except ValidationError as err:
        return err.messages, 400

    list_uuid = uuid.UUID(path_params['list_id'])
    list = db.session.query(List).filter(List.uuid == list_uuid).first()
    if list is None:
        abort(404)

    schema = ListSchema()
    result = schema.dumps(list)
    return result


@bp.route('/', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type not supported!', 400

    try:
        body = PostListValidationSchema().load(request.json)
    except ValidationError as err:
        return err.messages

    list = List(
        name=body['name']
    )
    db.session.add(list)
    db.session.commit()
    schema = ListSchema()
    result = schema.dumps(list)
    return result


@bp.route('/<list_id>', methods=['PATCH'])
def update(list_id):
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type not supported!', 400

    try:
        path_params = GetListValidationSchema().load(request.view_args)
        body_params = PostListValidationSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    list_uuid = uuid.UUID(path_params['list_id'])
    list = db.session.query(List).filter(List.uuid == list_uuid).first()
    if list is None:
        abort(404)

    list.name = body_params['name']
    db.session.commit()
    schema = ListSchema()
    result = schema.dumps(list)
    return result


@bp.route('/<list_id>', methods=['DELETE'])
def destroy(list_id):
    try:
        path_params = GetListValidationSchema().load(request.view_args)
    except ValidationError as err:
        return err.messages, 400

    list_uuid = uuid.UUID(path_params['list_id'])
    list = db.session.query(List).filter(List.uuid == list_uuid).first()
    if list is None:
        abort(404)

    db.session.delete(list)
    db.session.commit()
    return Response(status=204)


@bp.route('/<list_id>/items', methods=['GET'])
def item_index(list_id):
    try:
        path_params = GetListValidationSchema().load(request.view_args)
    except ValidationError as err:
        return err.messages, 400

    list_uuid = uuid.UUID(path_params['list_id'])
    list = db.session.query(List).filter(List.uuid == list_uuid).first()
    if list is None:
        abort(404)

    return item_index_by_list(list)


@bp.route('/<list_id>/items', methods=['POST'])
def item_create(list_id):
    try:
        path_params = GetListValidationSchema().load(request.view_args)
    except ValidationError as err:
        return err.messages, 400

    list_uuid = uuid.UUID(path_params['list_id'])
    list = db.session.query(List).filter(List.uuid == list_uuid).first()
    if list is None:
        abort(404)

    return item_create_by_list(list)
