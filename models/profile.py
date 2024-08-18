import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Date, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .user import User


class Profile(Base, IntIdPkMixin):
    user: Mapped["User"] = relationship(back_populates="profiles")
    user_pk: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    last_name: Mapped[str | None] = mapped_column(String(40))
    first_name: Mapped[str | None] = mapped_column(String(40), nullable=True)
    birthdate: Mapped[datetime.date] = mapped_column(Date)
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True)
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        onupdate=datetime.datetime.now
    )

    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }
