from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin


class ProductCategory(Base, IntIdPkMixin):
    __tablename__ = "product_categories"

    name = Column(String, nullable=False)

    products = relationship("Product", back_populates="category")
