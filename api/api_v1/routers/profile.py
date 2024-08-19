from fastapi import (
    APIRouter,
    Depends,
    Path,
    HTTPException
)
from starlette.status import (
    HTTP_400_BAD_REQUEST
)

from api.routers.fastapi_users_routers import current_user
# from api.dependencies.authentication.users import current_user
from core.config import settings
from models import User
from schemas import (
    ProfileCreate,
    ProfileRead,
    ProfileUpdate,
)
from schemas.user import UserRead
from services.profile import profile_service

router = APIRouter(
    prefix=settings.api.v1.profile,
    tags=["Profile"],
)


@router.get("/{profile_id}")
async def get_profile_by_id(
        profile_id: int = Path(title="The ID of the item to get", gt=0, le=1000000000)
) -> ProfileRead:
    try:
        profile = await profile_service.get(pk=profile_id)
        if profile is not None:
            # logger.info(f"get profile by id: {profile.id}")
            return profile
        else:
            # logger.info(f"profile {profile_id} not found")
            raise HTTPException(
                status_code=404,
                detail=f"Profile {profile_id} not found"
            )
    except Exception as e:
        # logger.warning(e)
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("")
def create_profile(
        user: User = Depends(current_user),
):
    return {"id": UserRead.model_validate(user)}


# @router.post("/create")
# async def create_profile(
#         data: ProfileCreate,
#         user: User = Depends(current_user),
# ) -> ProfileRead:
    # data.user_pk = user.id
    # try:
    #     return await profile_service.create(model=data)
    # except Exception as e:
    #     raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


# @router.put("/update")
# async def update_profile(
#         data: ProfileUpdate,
#         user: User = Depends(current_user),
# ) -> ProfileRead:
#     user_id = user.id
#     try:
#         return await profile_service.get_profile_by_user_id(pk=user_id, model=data)
#     except Exception as e:
#         raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
