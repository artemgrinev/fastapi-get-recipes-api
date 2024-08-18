from typing import TYPE_CHECKING

from sqlalchemy import Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin
from .mixins.created_at import CreateAtMixin
from .mixins.updated_at import UpdateAtMixin

if TYPE_CHECKING:
    from .product_category import ProductCategory


class Product(Base, IntIdPkMixin, UpdateAtMixin, CreateAtMixin):
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("product_categories.id"))
    price: Mapped[float] = mapped_column(Float)
    discountPercentage: Mapped[float] = mapped_column(Float)
    rating: Mapped[float] = mapped_column(Float)
    brand: Mapped[str] = mapped_column(String)
    weight: Mapped[float] = mapped_column(Float)
    shippingInformation: Mapped[str] = mapped_column(String)
    availabilityStatus: Mapped[str] = mapped_column(String)
    returnPolicy: Mapped[str] = mapped_column(String)
    minimumOrderQuantity: Mapped[int] = mapped_column(Integer)
    thumbnail: Mapped[str] = mapped_column(String)
    images_url: Mapped[str] = mapped_column(String)

    category: Mapped["ProductCategory"] = relationship("ProductCategory", back_populates="products")
    recipes = relationship("Recipe", secondary="recipe_product_association", back_populates="ingredients")
