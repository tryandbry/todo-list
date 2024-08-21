import os
from db.mysql import MySQL


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_STRATEGY = MySQL()

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return self.DB_STRATEGY.database_uri()
