import os
from db import mysql


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_STRATEGY = mysql

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return self.DB_STRATEGY.database_uri()
