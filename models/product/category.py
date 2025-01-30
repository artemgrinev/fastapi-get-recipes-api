from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped

from models import Base
from models.mixins import IdNameMixin
if TYPE_CHECKING:
    from .product import Product

class ProductCategory(Base, IdNameMixin):
    __tablename__ = "product_categories"
    
    products: Mapped["Product"] = relationship("Product", back_populates="category")