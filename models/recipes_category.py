from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .recipe_category_association import RecipeCategoryAssociation


class RecipesCategory(Base, IntIdPkMixin):
    __tablename__ = "recipes_categories"
    title: Mapped[str] = mapped_column(String, nullable=False)
    recipes: Mapped["RecipeCategoryAssociation"] = relationship(
        "RecipeCategoryAssociation",
        back_populates="categories"
    )

