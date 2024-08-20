import json
import random
from behave import given
from faker import Faker


@given('an item')
def step_given_an_item(context):
    fake = Faker()
    list_id = context.list["listId"]
    item_request = {
        "name": fake.name(),
    }
    response = context.client.post(
        f'/lists/{list_id}/items',
        json=item_request,
    )

    item = json.loads(response.data)
    context.item = item
    assert context.item["itemId"]


@given("one or more items in each list")
def step_given_multiple_items(context):
    for list in context.lists:
        context.list = list
        context.execute_steps("given one or more items in that list")

    del context.list


@given("one or more items in that list")
def step_given_multiple_items_in_a_list(context):
    try:
        context.items
    except AttributeError:
        context.items = []

    fake = Faker()
    itemCount = random.randint(0, 2)
    for i in range(0, itemCount):
        list_id = context.list["listId"]
        item_request = {
            "name": fake.name(),
        }
        response = context.client.post(
            f'/lists/{list_id}/items',
            json=item_request,
        )
        item_response = json.loads(response.data)
        assert item_response
        context.items.append(item_response)
