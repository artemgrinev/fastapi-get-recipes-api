from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from .recipe import Recipe

class RecipeInstruction(Base, IntIdPkMixin):
    title: Mapped[str] = mapped_column(String)
    image: Mapped[str] = mapped_column(String, nullable=True) 
    step_number: Mapped[int] = mapped_column(Integer)

    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey('recipes.id'))
    
    recipe: Mapped["Recipe"] = relationship("Recipe", back_populates="instructions")