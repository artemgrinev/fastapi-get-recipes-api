from sqlalchemy import select
from .sqlalchemy_repository import ModelType


class CategoryMixin:
    async def get_by_category_id(self, category_id: int) -> list[ModelType]:
        products = await self.session.execute(
            select(self.model).where(self.model.category_id == category_id)
        )
        return products.scalars().all()