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
    from .recipes_category import RecipesCategory
    from .product import Product


class Recipe(Base, IntIdPkMixin, UpdateAtMixin, CreateAtMixin):

    name: Mapped[str] = mapped_column(String, nullable=False)
    ingredients: Mapped["Product"] = relationship(
        "Product",
        secondary="recipe_product_associations",
        back_populates="recipes"
    )
    instructions: Mapped[str] = mapped_column(String)
    prep_time_minutes: Mapped[int] = mapped_column(Integer)
    cook_time_minutes: Mapped[int] = mapped_column(Integer)
    servings: Mapped[int] = mapped_column(Integer)
    difficulty: Mapped[str] = mapped_column(String)
    cuisine: Mapped[str] = mapped_column(String)
    calories_per_serving: Mapped[int] = mapped_column(Integer)
    category: Mapped["RecipesCategory"] = relationship(
        "RecipesCategory",
        secondary="recipe_category_associations",
        back_populates="recipes"
    )
    profile_id: Mapped[int] = mapped_column(Integer, ForeignKey("profiles.id"))
    image: Mapped[str] = mapped_column(String)
    rating: Mapped[float] = mapped_column(Float)
    review_count: Mapped[int] = mapped_column(Integer)

    profile = relationship("Profile", back_populates="recipes")
    comments = relationship("Comment", back_populates="recipe")


