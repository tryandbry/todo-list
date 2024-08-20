from behave import when


@when('we DELETE /lists/listId')
def step_when_delete_lists(context):
    list_id = context.list["listId"]
    context.response = context.client.delete(
        f'/lists/{list_id}',
    )
    assert context.response
