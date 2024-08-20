
from repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository
from core.db.db_helper import db_helper
from models.product import Product
from schemas.product import ProductRead, ProductBase


class ProductRepositories(SqlAlchemyRepository[ModelType, ProductRead, ProductBase]):
    pass


product_repositories = ProductRepositories(
    session=db_helper.session_getter,
    model=Product
)
