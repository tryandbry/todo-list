import json
import random
from behave import given, when, then
from faker import Faker


@given('one or more lists')
def step_given_multiple_lists(context):
    list_count = random.randint(2, 4)
    fake = Faker()
    context.lists = []
    for i in range(0, list_count):
        list_request = {
            "name": fake.name(),
        }
        response = context.client.post(
            '/lists/',
            json=list_request,
        )
        list_response = json.loads(response.data)
        assert list_response
        context.lists.append(list_response)


@when('we GET /lists/')
def step_when_post_lists(context):
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
