import os
from .database_strategy import DatabaseStrategy


class SQLite(DatabaseStrategy):
    basedir = os.path.abspath(os.path.dirname(__file__))
    sqlite_database = "app.db"

    @property
    def test_sqlite_database(self):
        return f'{self.sqlite_database}_test'

    def database_uri(self):
        return f'sqlite:///{self.basedir}/{self.sqlite_database}'

    def test_database_uri(self):
        return f'sqlite:///{self.basedir}/{self.test_sqlite_database}'
