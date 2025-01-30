from typing import TYPE_CHECKING, List
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import ForeignKey
from models import Base
from models.mixins import IdNameMixin

if TYPE_CHECKING:
    from .product import Product


class ProductVendor(Base, IdNameMixin):
    products: Mapped["Product"] = relationship("Product", back_populates="vendor")