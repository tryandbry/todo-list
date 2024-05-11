import uuid
from dataclasses import dataclass
from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column
from db import db
from db.timestamp_mixin import TimestampMixin


@dataclass
class List(TimestampMixin, db.Model):
    __tablename__ = "lists"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    uuid: Mapped[Uuid] = mapped_column(Uuid, unique=True, default=uuid.uuid4)