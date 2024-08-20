import json
from behave import given, when, then


@given('a new list name')
def step_given_a_new_list_name(context):
    context.request_body = {"name": "squirtle"}
    pass


@when('we PATCH /lists/listId')
def step_when_patch_lists(context):
    list_id = context.list["listId"]
    context.response = context.client.patch(
        f'/lists/{list_id}',
        json=context.request_body,
    )
    assert context.response


@then('receive the list with the new name')
def step_then_list_with_new_name(context):
    response_body = json.loads(context.response.data)
    assert response_body["listId"] == context.list["listId"]
    assert response_body["name"] == context.request_body["name"]
