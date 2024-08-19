import json
from behave import given, when, then


@given('a list name')
def step_given_list_name(context):
    context.request_body = {
        "name": "pikachu",
    }
    pass


@when('we POST /lists with the name')
def step_when_post_lists(context):
    context.response = context.client.post(
        '/lists/',
        json=context.request_body,
    )
    assert context.response


@then('receive HTTP 200 OK')
def step_then_200_ok(context):
    assert context.response.status_code == 200


@then('receive a new list with the name')
def step_then_new_list(context):
    response_body = json.loads(context.response.data)
    assert response_body["name"] == context.request_body["name"]
