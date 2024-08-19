from behave import *
from db import db
from lists.models import List
from lists.serializers import ListSchema

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    stmt = db.select(List).order_by(List.updated_at)
    lists = db.session.execute(stmt).scalars().all()
    schema = ListSchema(many=True)
    result = schema.dumps(lists)
    print("Query:")
    print(result)
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False