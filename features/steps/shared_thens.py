import json
from behave import then


@then('receive HTTP 200 OK')
def step_then_200_ok(context):
    assert context.response.status_code == 200


@then('receive HTTP 204 No Content')
def step_then_204_no_content(context):
    assert context.response.status_code == 204


@then('get the items')
def step_then_get_items(context):
    item_ids = [x["itemId"] for x in context.items]
    response_body = json.loads(context.response.data)
    matches = [x["itemId"] in item_ids for x in response_body]
    assert len(matches) == len(context.items)