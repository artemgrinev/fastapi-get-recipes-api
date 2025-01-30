from typing import TYPE_CHECKING, List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models import Base
from models.mixins import (
    IdNameMixin,
    UpdateAtMixin,
    CreateAtMixin
)
if TYPE_CHECKING:
    from .ingredient import RecipeIngredient
    from .instruction import RecipeInstruction
    from .review import RecipeReview
    from .category import RecipeCategory
    from .subcategory import RecipeSubcategory
    from .cuisine import Cuisine
    from .tag import RecipeTag


class Recipe(Base, IdNameMixin, UpdateAtMixin, CreateAtMixin):
    url: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    prep_time_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    cook_time_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    preliminary_preparation: Mapped[str] = mapped_column(String(50))
    servings: Mapped[int] = mapped_column(Integer, nullable=False)
    difficulty: Mapped[str] = mapped_column(String(10), nullable=False, default="simple")
    image: Mapped[str] = mapped_column(String, nullable=False, default="/recipe/plug.png")
    calories_per_serving: Mapped[int] = mapped_column(Integer, nullable=True)
    ingredients: Mapped[List["RecipeIngredient"]] = relationship("Ingredient", back_populates="recipe")
    instructions: Mapped[List["RecipeInstruction"]] = relationship("Instruction", back_populates="recipe")
    reviews: Mapped[List["RecipeReview"]] = relationship("RecipeReview", back_populates="recipe")

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('recipe_categories.id'), nullable=False)
    category: Mapped["RecipeCategory"] = relationship("RecipeCategory", back_populates="recipes")

    subcategories: Mapped[List["RecipeSubcategory"]] = relationship(
        "RecipeSubcategory", 
        secondary="recipe_subcategory_associations", 
        back_populates="recipe"
        )

    cuisine_id: Mapped[int] = mapped_column(Integer, ForeignKey('cuisines.id'), nullable=False)
    cuisine: Mapped["Cuisine"] = relationship("Cuisine", back_populates="recipes")
    
    tags: Mapped["RecipeTag"] = relationship("RecipeTagAssociations", back_populates="recipes")



