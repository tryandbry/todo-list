import json
from behave import given, when, then


@given('a list name')
def step_given_list_name(context):
    context.request_body = {
        "name": "pikachu",
    }
    pass


@when('we POST /lists/')
def step_when_post_lists(context):
    context.response = context.client.post(
        '/lists/',
        json=context.request_body,
    )
    assert context.response


@then('receive a new list with the name')
def step_then_new_list(context):
    response_body = json.loads(context.response.data)
    assert response_body["name"] == context.request_body["name"]
