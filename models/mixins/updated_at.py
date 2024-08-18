import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class UpdateAtMixin:
    updated_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        onupdate=datetime.datetime.now
    )
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }

