from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin


class RecipesCategory(Base, IntIdPkMixin):
    __tablename__ = "recipes_categories"
    name: Mapped[str] = mapped_column(String, nullable=False)

