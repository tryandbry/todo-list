from behave import when


@when('we GET /health')
def step_when_get_health(context):
    context.response = context.client.get('/health')
    assert context.response
