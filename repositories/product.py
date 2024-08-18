from repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository

from models.product import Product

from core.db.db_helper import db_helper
from schemas import ProductRead


class ProductRepositories(SqlAlchemyRepository[ModelType, ProductRead]):
    pass


product_repositories = ProductRepositories(
    session=db_helper.session_getter,
    model=Product
)
