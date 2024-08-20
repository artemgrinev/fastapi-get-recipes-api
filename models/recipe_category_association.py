from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .recipes_category import RecipesCategory
    from recipes import Recipe


class RecipeCategoryAssociation(Base, IntIdPkMixin):

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    category_id = Column(Integer, ForeignKey("recipes_categories.id"))

    categories: Mapped["Recipe"] = relationship("RecipesCategory", back_populates="recipes")
    recipes: Mapped["RecipesCategory"] = relationship("Recipe", back_populates="categories")
