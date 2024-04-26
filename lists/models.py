from sqlalchemy.orm import Mapped, mapped_column, String
from sqlalchemy.sql import func
from datetime import datetime
from db import db


class List(db.Model):
    __tablename__ = "lists"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    modified_at: Mapped[datetime.datetime] = mapped_column(onupdate=func.utc_timestamp())


"""
TODO: how to set created_at and modified_at?
https://stackoverflow.com/questions/70791906/creation-timestamp-of-a-row-in-sqlalchemy

https://docs.sqlalchemy.org/en/20/core/compiler.html#utc-timestamp-function
"""
