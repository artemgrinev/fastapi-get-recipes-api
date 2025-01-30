from repositories.sqlalchemy_repository import ModelType


class CategoryMixin:

    async def get_category_by_id(self, category_id: int) -> ModelType:
        return await self.repository.get_by_category_id(category_id)