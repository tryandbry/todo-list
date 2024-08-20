import json
from behave import when, then


@when('we GET /lists/listId')
def step_when_post_lists(context):
    list_id = context.list["listId"]
    context.response = context.client.get(
        f'/lists/{list_id}',
    )
    assert context.response


@then('get the list')
def step_then_get_list(context):
    response_body = json.loads(context.response.data)
    assert response_body["listId"] == context.list["listId"]
