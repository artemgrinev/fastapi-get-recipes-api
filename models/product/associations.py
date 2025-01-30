from sqlalchemy import Integer, ForeignKey, Table, Column

from models import Base

products_associations = Table(
    "products_associations",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("similar_product_id", Integer, ForeignKey("products.id"), primary_key=True)
)
