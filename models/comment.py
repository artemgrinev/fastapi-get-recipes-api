from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from models.mixins import (
    IntIdPkMixin,
    UpdateAtMixin,
    CreateAtMixin
)

if TYPE_CHECKING:
    from .recipes import Recipe
    from .profile import Profile


class Comment(Base, IntIdPkMixin, CreateAtMixin, UpdateAtMixin):
    body: Mapped[str] = mapped_column(String, nullable=False)
    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey("recipes.id"))
    profile_id: Mapped[int] = mapped_column(Integer, ForeignKey("profiles.id"))

    recipe: Mapped["Recipe"] = relationship("Recipe", back_populates="comments")
    profile: Mapped["Profile"] = relationship("Profile", back_populates="comments")
