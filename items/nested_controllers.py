from .serializers import ItemSchema


def item_index_by_list(list):
    schema = ItemSchema(many=True)
    result = schema.dumps(list.items)
    return result