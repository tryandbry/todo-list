import json
from behave import given, when, then


@given('a list')
def step_given_a_list(context):
    list_request = {
        "name": "pikachu",
    }
    response = context.client.post(
        '/lists/',
        json=list_request,
    )
    list_response = json.loads(response.data)
    context.list = list_response
    assert context.list["listId"]


@given('an item name')
def step_given_an_item_name(context):
    context.item_name = "thunderbolt"
    pass


@when('we POST /lists/listId/items with the name')
def step_when_post_items(context):
    list_id = context.list["listId"]
    request_body = {
        "name": context.item_name,
    }
    context.response = context.client.post(
        f'/lists/{list_id}/items',
        json=request_body,
    )
    assert context.response


@then('receive a new item with the name')
def step_then_new_item(context):
    response_body = json.loads(context.response.data)
    assert response_body["name"] == context.item_name


@then('associated with the list')
def step_then_associated_with_the_list(context):
    response_body = json.loads(context.response.data)
    assert response_body["list"]['listId'] == context.list['listId']
