from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, relationship
from models import Base
from models.mixins import IdNameMixin
if TYPE_CHECKING:
    from .recipe import Recipe
    from .subcategory import RecipeSubcategory


class RecipeCategory(Base, IdNameMixin):
    __tablename__ = "recipe_categories"
    subcategories: Mapped[List["RecipeSubcategory"]] = relationship("RecipeSubcategory", back_populates="category")
    recipes: Mapped[List["Recipe"]] = relationship("Recipe", back_populates="category")
