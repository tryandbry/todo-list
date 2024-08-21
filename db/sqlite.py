import os
from .strategy import DatabaseStrategy


class MySQL(DatabaseStrategy):
    def database_uri(self, database="app.db"):
        basedir = os.path.abspath(os.path.dirname(__file__))
        return f'sqlite:///{basedir}/{database}'

    def test_database_uri(self):
        return self.database_uri('app_test.db')
