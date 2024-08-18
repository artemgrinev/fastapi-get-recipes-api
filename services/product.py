from services.base_services import BaseServices
from repositories.product import product_repositories


class ProductServices(BaseServices):
    pass


product_service = ProductServices(repository=product_repositories)
