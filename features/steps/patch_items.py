import json
from behave import given, when, then
from faker import Faker


@given('a new item name')
def step_given_a_new_item_name(context):
    fake = Faker()
    context.request_body = {"name": fake.name()}
    pass


@given('a new item completed status')
def step_given_a_new_item_completed_status(context):
    opposite_status = not context.item["completed"]
    context.request_body = {"completed": opposite_status}
    pass


@when('we PATCH /items/itemId')
def step_when_patch_items(context):
    item_id = context.item["itemId"]
    context.response = context.client.patch(
        f'/items/{item_id}',
        json=context.request_body,
    )
    assert context.response


@then('receive the item with the new name')
def step_then_item_with_new_name(context):
    response_body = json.loads(context.response.data)
    assert response_body["itemId"] == context.item["itemId"]
    assert response_body["name"] == context.request_body["name"]


@then('receive the item with the new completed status')
def step_then_item_with_new_completed_status(context):
    response_body = json.loads(context.response.data)
    assert response_body["itemId"] == context.item["itemId"]
    assert response_body["completed"] == context.request_body["completed"]
