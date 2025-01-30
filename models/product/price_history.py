import datetime
from sqlalchemy import Integer, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models import Base
from models.mixins import IntIdPkMixin
from .product import Product


class ProductPriceHistory(Base, IntIdPkMixin):
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('products.id'), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    discount: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=datetime.datetime.utcnow,
        nullable=False
    )
    product: Mapped["Product"] = relationship("Product", back_populates="price_history")