import json
from behave import given


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
