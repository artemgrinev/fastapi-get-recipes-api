from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from models.mixins import IdNameMixin

if TYPE_CHECKING:
    from models.product.product import Product

class ProductShop(Base, IdNameMixin):
    url: Mapped[str] = mapped_column(String(255), nullable= False)
    logo: Mapped[str] = mapped_column(String(255), nullable= False)

    products: Mapped["Product"] = relationship("Product", back_populates="shop")