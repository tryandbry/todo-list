from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db import db
from db.timestamp_mixin import TimestampMixin


class List(TimestampMixin, db.Model):
    __tablename__ = "lists"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f'List(id={self.id!r}, name={self.name!r}, created_at={self.created_at!r}, updated_at={self.updated_at!r}'


"""
TODO: how to set created_at and modified_at?
https://stackoverflow.com/questions/70791906/creation-timestamp-of-a-row-in-sqlalchemy

https://docs.sqlalchemy.org/en/20/core/compiler.html#utc-timestamp-function
"""
