import json
from behave import when, then


@when('we GET /items/itemId')
def step_when_get_item(context):
    item_id = context.item["itemId"]
    context.response = context.client.get(
        f'/items/{item_id}',
    )
    assert context.response


@then('get the item')
def step_then_get_item(context):
    response_body = json.loads(context.response.data)
    assert response_body["itemId"] == context.item["itemId"]
