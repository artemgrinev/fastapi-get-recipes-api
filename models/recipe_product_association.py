from sqlalchemy import Column, Integer, ForeignKey

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin


class RecipeProductAssociation(Base, IntIdPkMixin):
    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
