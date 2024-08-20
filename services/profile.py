from repositories.sqlalchemy_repository import ModelType
from schemas.base_schemas import PyModel
from schemas.profile import (
    ProfileRead,
    ProfileDelete
)

from services.base_services import BaseServices
from repositories.profile import profile_repositories


class ProfileServices(BaseServices):
    async def get_profile_by_user_id(self, pk: int) -> ProfileRead | None:
        return await self.repository.get_single(user_pk=pk)


profile_service = ProfileServices(repository=profile_repositories)
