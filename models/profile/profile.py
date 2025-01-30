import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    String,
    Date,
    Boolean
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from models import Base
from models.mixins import (
    IntIdPkMixin,
    UpdateAtMixin,
    CreateAtMixin
)

if TYPE_CHECKING:
    from models import (
        User,
        RecipeReview,
        Recipe
    )


class Profile(Base, IntIdPkMixin, UpdateAtMixin, CreateAtMixin):
    user: Mapped["User"] = relationship(back_populates="profile")
    user_pk: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    last_name: Mapped[str | None] = mapped_column(String(40))
    first_name: Mapped[str | None] = mapped_column(String(40), nullable=True)
    birthdate: Mapped[datetime.date] = mapped_column(Date)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    recipes: Mapped[list["Recipe"]] = relationship("Recipe", back_populates="profile")
    reviews: Mapped[list["RecipeReview"]] = relationship("Reviews", back_populates="profile")

