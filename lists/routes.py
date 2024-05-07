from . import bp
from db import db
from .models import List
from flask import jsonify


@bp.route('/', methods=['GET'])
def index():
    stmt = db.select(List).order_by(List.updated_at)
    lists = db.session.execute(stmt).scalars().all()
    return jsonify(lists)