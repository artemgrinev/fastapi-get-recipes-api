import datetime

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class CreateAtMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=datetime.datetime.utcnow
    )
    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }
