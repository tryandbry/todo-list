from behave import when, then


@when('we DELETE /lists/listId')
def step_when_post_lists(context):
    list_id = context.list["listId"]
    context.response = context.client.delete(
        f'/lists/{list_id}',
    )
    assert context.response


@then('receive HTTP 204 No Content')
def step_then_new_list(context):
    assert context.response.status_code == 204
