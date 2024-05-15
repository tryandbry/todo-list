from .models import Item
from .queries import where_completed_query
from .serializers import ItemSchema
from .validators import GetItemsValidationSchema, PostItemValidationSchema
from flask import request
from marshmallow import ValidationError
from db import db


def item_index_by_list(list):
    try:
        query_params = GetItemsValidationSchema().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    query = db.session.query(Item).where(Item.list_id == list.id)
    query = where_completed_query(query_params, query)
    items = db.session.scalars(query).all()
    schema = ItemSchema(many=True)
    result = schema.dumps(items)
    return result

def item_create_by_list(list):
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return 'Content-Type not supported!', 400

    try:
        body = PostItemValidationSchema().load(request.json)
    except ValidationError as err:
        return err.messages

    item = Item(
        name=body['name'],
        list=list,
    )
    db.session.add(item)
    db.session.commit()
    schema = ItemSchema()
    result = schema.dumps(item)
    return result