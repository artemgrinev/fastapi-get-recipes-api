from schemas.profile import (
    ProfileRead,
    ProfileUpdate
)

from services.base_services import BaseServices
from repositories.profile import profile_repositories


class ProfileServices(BaseServices):
    async def get_profile_by_user_id(
            self,
            pk: int,
            model: ProfileUpdate
    ) -> ProfileRead | None:
        profile = await self.repository.get_single(user_pk=pk)
        return await self.repository.update(data=model.model_dump(), id=profile.id)


profile_service = ProfileServices(repository=profile_repositories)
