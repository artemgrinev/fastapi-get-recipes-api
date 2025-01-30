from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from models.mixins import (
    IntIdPkMixin,
    UpdateAtMixin,
    CreateAtMixin
)
if TYPE_CHECKING:
    from .recipe import Recipe
    from models.profile.profile import Profile

class RecipeReview(Base, IntIdPkMixin, CreateAtMixin, UpdateAtMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    profile_id: Mapped[int] = mapped_column(Integer, ForeignKey("profiles.id"))
    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey('recipes.id'))
    rating: Mapped[float] = mapped_column(Float, default=0)
    comment: Mapped[str] = mapped_column(String, default="")
    
    recipe: Mapped["Recipe"] = relationship("Recipe", back_populates="reviews")
    profile: Mapped["Profile"] = relationship("Profile", back_populates="reviews")