import datetime
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class TimestampMixin:
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }
    created_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=func.now(),
        onupdate=func.now()
    )


## TODO: Try defining the `timezone=True` attribute without setting a new type_map
## ref: https://docs.sqlalchemy.org/en/20/core/compiler.html#utc-timestamp-function
