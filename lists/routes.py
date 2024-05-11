from . import bp
from db import db
from .models import List
from .serializers import ListSchema
from .validators import ListValidationSchema
from flask import jsonify, request
from marshmallow import ValidationError
import uuid


@bp.route('/', methods=['GET'])
def index():
    stmt = db.select(List).order_by(List.updated_at)
    lists = db.session.execute(stmt).scalars().all()
    schema = ListSchema(many=True)
    result = schema.dumps(lists)
    return result

@bp.route('/<listId>', methods=['GET'])
def show(listId):
    list_uuid = uuid.UUID(listId)
    list = db.session.query(List).filter(List.uuid == list_uuid).first()
    schema = ListSchema()
    result = schema.dumps(list)
    return result

@bp.route('/', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type not supported!'
    
    try:
        body = ListValidationSchema().load(request.json)
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