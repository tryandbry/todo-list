from behave import fixture, use_fixture
from config import Config
from app import create_app
from db import db
from lists.models import List


@fixture
def app_instance(context, *args, **kwargs):
    test_app = create_app(TestConfig)
    context.app = test_app
    yield context.app


@fixture
def app_client(context, *args, **kwargs):
    context.client = context.app.test_client()
    yield context.client


@fixture
def app_context(context, *args, **kwargs):
    context.app_context = context.app.app_context()
    yield context.app_context


def before_feature(context, feature):
    use_fixture(app_instance, context)
    use_fixture(app_client, context)
    use_fixture(app_context, context)
    context.app_context.push()


def after_feature(context, feature):
    db.session.query(List).delete()
    db.session.commit()
    db.session.close()
    context.app_context.pop()


class TestConfig(Config):
    TESTING = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return self.DB_STRATEGY.test_database_uri()
