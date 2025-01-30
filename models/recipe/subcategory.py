from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import Integer, ForeignKey
from models import Base
from models.mixins import IdNameMixin
if TYPE_CHECKING:
    from .recipe import Recipe
    from .category import RecipeCategory

class RecipeSubcategory(Base, IdNameMixin):
    __tablename__ = "recipe_subcategories"
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('recipe_categories.id'))
    category: Mapped["RecipeCategory"] = relationship("RecipeCategory", back_populates="subcategories")
    recipes: Mapped[List["Recipe"]] = relationship(
        "Recipe", 
        secondary="recipe_subcategory_associations", 
        back_populates="subcategory"
    )
