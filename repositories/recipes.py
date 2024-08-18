from repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository

from core.db.db_helper import db_helper
from schemas import RecipeRead, RecipeUpdate
from models import Profile


class RecipieRepositories(SqlAlchemyRepository[ModelType, RecipeRead, RecipeUpdate]):
    pass


recipe_repositories = RecipieRepositories(
    session=db_helper.session_getter,
    model=Profile
)
