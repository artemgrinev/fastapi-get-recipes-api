from typing import TYPE_CHECKING, List

from sqlalchemy import Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from models import Base
from .associations import products_associations
from models.mixins import (
    IdNameMixin,
    CreateAtMixin,
    UpdateAtMixin
)
if TYPE_CHECKING:
    from models.shop.shop import ProductShop
    from .category import ProductCategory
    from models.recipe.ingredient import RecipeIngredient
    from .vendor import ProductVendor

class Product(Base, IdNameMixin, CreateAtMixin, UpdateAtMixin):
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    uom: Mapped[str] = mapped_column(String(10), nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    pack: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    current_price: Mapped[int] = mapped_column(Integer, nullable=False)
    price_history = relationship(
        "PriceHistory", 
        back_populates="product", 
        order_by="PriceHistory.created_at.desc()"
        )
    property_clarification: Mapped[str] = mapped_column(String(30), nullable=False)
    image: Mapped[str] = mapped_column(String(255), nullable=False)
    thumbnail: Mapped[str] = mapped_column(String(255), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("product_categories.id"), nullable=False)
    category: Mapped["ProductCategory"] = relationship("ProductCategory", back_populates="products")
    vendor_id: Mapped[int] = mapped_column(Integer, ForeignKey("product_vendors.id"), nullable=False)
    vendor: Mapped["ProductVendor"] = relationship("ProductVendor", back_populates="products")
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("product_shops.id"), nullable=False)
    shop: Mapped["ProductShop"] = relationship("ProductShop", back_populates="products")
    main_ingredient_for: Mapped[List["RecipeIngredient"]] = relationship(
        "RecipeIngredient",
        back_populates="main_product"
        )
    similar_products = relationship(
        "Product",
        secondary="products_associations",
        primaryjoin=(id== products_associations.c.product_id),
        secondaryjoin=(id == products_associations.c.similar_product_id),
        backref="related_to"
        )
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name})>"

