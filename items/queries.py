from .models import Item


def where_completed_query(params, query):
    if "completed" not in params:
        return query

    return query.where(Item.completed == params["completed"])
