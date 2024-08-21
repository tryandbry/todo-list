import os


def database_uri(database="app.db"):
    basedir = os.path.abspath(os.path.dirname(__file__))
    return f'sqlite:///{basedir}/{database}'


def test_database_uri():
    return database_uri('app_test.db')
