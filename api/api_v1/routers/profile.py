from fastapi import (
    APIRouter,
    Depends,
    Path,
    HTTPException,
    status
)
from starlette.status import HTTP_400_BAD_REQUEST

from api.routers.fastapi_users_routers import current_user
from core.config import settings
from models import User
from schemas import (
    ProfileCreate,
    ProfileRead,
    ProfileUpdate,
    ProfileDelete
)

from services.profile import profile_service

router = APIRouter(
    prefix=settings.api.v1.profile,
    tags=["Profile"],
)


@router.get(
    "/{profile_id}",
    status_code=status.HTTP_200_OK,
    name="profile: get_profile_by_id",
    response_model=ProfileRead
)
async def get_profile_by_id(
        profile_id: int = Path(title="The ID of the item to get", gt=0, le=1000000000)
) -> ProfileRead:
    try:
        profile = await profile_service.get(pk=profile_id)
        if profile is not None:
            return profile
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Profile {profile_id} not found"
            )
    except Exception as e:
        # logger.warning(e)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    name="profile:create",
    response_model=ProfileRead
)
async def create_profile(
        data: ProfileCreate,
        user: User = Depends(current_user),
) -> ProfileRead:
    user_pk = user.id
    profile = await profile_service.get_profile_by_user_id(pk=user_pk)
    if not profile.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The profile has been deleted"
        )
    if profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile for this user already exists."
        )
    data.user_pk = user_pk
    try:
        return await profile_service.create(model=data)
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.put(
    "/update",
    status_code=status.HTTP_200_OK,
    name="profile:update",
    response_model=ProfileRead
)
async def update_profile(
        data: ProfileUpdate,
        user: User = Depends(current_user),
):
    profile = await profile_service.get_profile_by_user_id(pk=user.id)
    try:
        return await profile_service.update(pk=profile.id, model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.put(
    "/delete",
    status_code=status.HTTP_200_OK,
    name="profile:update",
    response_model=ProfileDelete
)
async def delete_profile(
        user: User = Depends(current_user),
):
    profile = await profile_service.get_profile_by_user_id(pk=user.id)
    profile.is_active = False
    deleted_profile = await profile_service.update(pk=profile.id, model=profile)
    try:
        return deleted_profile.id
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
