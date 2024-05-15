from . import bp
from db import db
from .models import Item
from .serializers import ItemSchema


@bp.route('/', methods=['GET'])
def index():
    stmt = db.select(Item).order_by(Item.updated_at)
    items = db.session.execute(stmt).scalars().all()
    schema = ItemSchema(many=True)
    result = schema.dumps(items)
    return result