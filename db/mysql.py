import os
from .database_strategy import DatabaseStrategy


class MySQL(DatabaseStrategy):
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_user = os.environ.get('MYSQL_USER')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_database = os.environ.get('MYSQL_DATABASE')

    @property
    def test_mysql_database(self):
        return f'{self.mysql_database}_test'

    def database_uri(self):
        return f'mysql+pymysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}/{self.mysql_database}'  # noqa: E501

    def test_database_uri(self):
        return f'mysql+pymysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}/{self.test_mysql_database}'  # noqa: E501
