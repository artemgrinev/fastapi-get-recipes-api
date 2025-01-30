from typing import TYPE_CHECKING, List

from sqlalchemy.orm import relationship, Mapped

from models import Base
from models.mixins import IdNameMixin

if TYPE_CHECKING:
    from .recipe import Recipe

class Cuisine(Base, IdNameMixin):
   recipes: Mapped[List["Recipe"]] = relationship( "Recipe" , back_populates="cuisine")