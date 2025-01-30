
from repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository
from core.db.db_helper import db_helper
from models import Product
from schemas.product import ProductRead, ProductBase
from .mixins_repository import CategoryMixin


class ProductRepositories(CategoryMixin, SqlAlchemyRepository[ModelType, ProductRead, ProductBase]):
    pass



product_repositories = ProductRepositories(
    session=db_helper.session_getter,
    model=Product
)
