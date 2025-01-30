from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from models.mixins import IdNameMixin

if TYPE_CHECKING:
    from .recipe import Recipe
    from models.product import Product
    
class RecipeIngredient(Base, IdNameMixin):
    count: Mapped[int] = mapped_column(Integer, nullable=False)
    uom: Mapped[str] = mapped_column(String, nullable=False)

    recipe_id: Mapped[int] = mapped_column(Integer, ForeignKey('recipes.id'), nullable=False)
    recipe: Mapped["Recipe"] = relationship("Recipe", back_populates="ingredients")
    
    products: Mapped[List["Product"]] = relationship(
            "Product", 
            secondary='ingredient_product_assiociations', 
            back_populates="ingredients"
        )
    
    main_product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'), nullable=True)
    main_product: Mapped["Product"] = relationship(
        "Product", 
        foreign_keys=[main_product_id], 
        back_populates="main_ingredient_for"
        )