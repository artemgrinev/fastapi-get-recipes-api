from repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository

from models.profile import Profile
from schemas.profile import ProfileUpdate, ProfileCreate
from core.db.db_helper import db_helper


class ProfileRepositories(SqlAlchemyRepository[ModelType, ProfileCreate, ProfileUpdate]):
    pass


profile_repositories = ProfileRepositories(
    session=db_helper.session_getter,
    model=Profile
)
