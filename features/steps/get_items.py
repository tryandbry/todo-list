from behave import when


@when('we GET /items/')
def step_when_get_items(context):
    context.response = context.client.get(
        '/items/',
    )
    assert context.response
