import json
import random
from behave import given
from faker import Faker


@given('a list')
def step_given_a_list(context):
    fake = Faker()
    list_request = {
        "name": fake.name(),
    }
    response = context.client.post(
        '/lists/',
        json=list_request,
    )
    list = json.loads(response.data)
    context.list = list
    assert context.list["listId"]


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
