from behave import when


@when('we GET /lists/listId/items')
def step_when_get_items(context):
    list_id = context.list["listId"]
    context.response = context.client.get(
        f'/lists/{list_id}/items',
    )
    assert context.response
