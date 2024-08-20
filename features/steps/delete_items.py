from behave import when


@when('we DELETE /items/itemId')
def step_when_delete_items(context):
    item_id = context.item["itemId"]
    context.response = context.client.delete(
        f'/items/{item_id}',
    )
    assert context.response