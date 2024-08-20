import json
from behave import when, then


@when('we GET /lists/')
def step_when_get_lists(context):
    context.response = context.client.get(
        '/lists/',
    )
    assert context.response


@then('get the lists')
def step_then_get_lists(context):
    list_ids = [x["listId"] for x in context.lists]
    response_body = json.loads(context.response.data)
    matches = [x["listId"] in list_ids for x in response_body]
    assert len(matches) == len(context.lists)
