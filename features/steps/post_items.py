import json
from behave import given, when, then


@given('an item name')
def step_given_an_item_name(context):
    context.request_body = {"name": "thunderbolt"}
    pass


@when('we POST /lists/listId/items')
def step_when_post_items(context):
    list_id = context.list["listId"]
    context.response = context.client.post(
        f'/lists/{list_id}/items',
        json=context.request_body,
    )
    assert context.response


@then('receive a new item with the name')
def step_then_new_item(context):
    response_body = json.loads(context.response.data)
    assert response_body["name"] == context.request_body["name"]


@then('associated with the list')
def step_then_associated_with_the_list(context):
    response_body = json.loads(context.response.data)
    assert response_body["list"]['listId'] == context.list['listId']
