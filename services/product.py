from repositories.sqlalchemy_repository import ModelType
from services.base_services import BaseServices
from repositories.product import product_repositories


class ProductServices(BaseServices):
    async def search_by_name(self, name: str) -> ModelType:
        return await self.repository.search_by_name(q=name)


product_service = ProductServices(repository=product_repositories)

