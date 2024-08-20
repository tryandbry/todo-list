import uuid
from dataclasses import dataclass
from sqlalchemy import String, Uuid, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import db
from db.timestamp_mixin import TimestampMixin


@dataclass
class Item(TimestampMixin, db.Model):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    uuid: Mapped[Uuid] = mapped_column(Uuid, unique=True, default=uuid.uuid4)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    list_id: Mapped[int] = mapped_column(ForeignKey(
        "lists.id",
        ondelete="CASCADE"
    ))
    list: Mapped["List"] = relationship("List", back_populates="items")