import os
from behave import fixture, use_fixture
from config import basedir
from app import create_app
from db import db
from lists.models import List


@fixture
def app_client(context, *args, **kwargs):
    app_instance = create_app(TestConfig)
    # have to manually push an app context:
    # to be able to query the database in test
    # ref: https://flask.palletsprojects.com/en/2.3.x/appcontext/#manually-push-a-context # noqa: E501
    app_instance.app_context().push()
    context.client = app_instance.test_client()
    yield context.client


def before_feature(context, feature):
    use_fixture(app_client, context)


def after_feature(context, feature):
    db.session.query(List).delete()
    db.session.commit()
    db.session.close()


class TestConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
