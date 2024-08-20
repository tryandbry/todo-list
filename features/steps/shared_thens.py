from behave import then


@then('receive HTTP 200 OK')
def step_then_200_ok(context):
    assert context.response.status_code == 200
