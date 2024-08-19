import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Date
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from .base import Base
from .mixins import (
    IntIdPkMixin,
    UpdateAtMixin,
    CreateAtMixin
)

if TYPE_CHECKING:
    from .user import User


class Profile(Base, IntIdPkMixin, UpdateAtMixin, CreateAtMixin):
    user: Mapped["User"] = relationship(back_populates="profile")
    user_pk: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    last_name: Mapped[str | None] = mapped_column(String(40))
    first_name: Mapped[str | None] = mapped_column(String(40), nullable=True)
    birthdate: Mapped[datetime.date] = mapped_column(Date)

    recipes = relationship("Recipe", back_populates="profile")
    comments = relationship("Comment", back_populates="profile")

