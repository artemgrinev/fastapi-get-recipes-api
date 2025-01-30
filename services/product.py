from services import BaseServices
from repositories import product_repositories
from repositories.sqlalchemy_repository import ModelType
from services.mixins_services import CategoryMixin

class ProductServices(BaseServices, CategoryMixin):
    async def search_by_name(self, name: str) -> ModelType:
        return await self.repository.search_by_name(q=name)


product_service = ProductServices(repository=product_repositories)

