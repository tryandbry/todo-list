import os
from .strategy import DatabaseStrategy


class MySQL(DatabaseStrategy):
    def database_uri(self, mysql_database=None):
        if mysql_database is None:
            mysql_database = os.environ.get('MYSQL_DATABASE')

        mysql_host = os.environ.get('MYSQL_HOST')
        mysql_user = os.environ.get('MYSQL_USER')
        mysql_password = os.environ.get('MYSQL_PASSWORD')
        return f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}'  # noqa: E501

    def test_database_uri(self):
        mysql_database = f'{os.environ.get('MYSQL_DATABASE')}_test'
        return self.database_uri(mysql_database)
