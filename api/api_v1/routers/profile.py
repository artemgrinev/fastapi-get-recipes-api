from fastapi import (
    APIRouter,
    Depends,
    Path,
    HTTPException
)
from starlette.status import (
    HTTP_400_BAD_REQUEST
)

from core.config import settings
from schemas import (
    ProfileCreate,
    ProfileUpdate
)

router = APIRouter(
    prefix=settings.api.v1.profile,
    tags=["Profile"],
)


@router.get(
    "/{id}",
    name="profiles:get-profile-by-id",
    responses={
        404: {
            "model": HTTP_404,
            "description": "Profile not found"
        },

    }
)
async def get_profile_by_id(
        user_id: int = Path(title="The ID of the item to get", gt=0, le=1000000000)
):
    try:
        profile = await profile_service.get(pk=user_id)
        if profile is not None:
            # logger.info(f"get profile by id: {profile.id}")
            return profile
        else:
            # logger.info(f"profile {id} not found")
            raise HTTPException(
                status_code=404,
                detail=f"Profile {user_id} not found"
            )
    except Exception as e:
        # logger.warning(e)
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/create")
async def create_profile(
        data: ProfileCreate,
        user: User = Depends(current_user),
) -> ProfileResponse:
    data.user_pk = user.id
    try:
        return await profile_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.put("/update")
async def update_profile(
        data: ProfileUpdate,
        user: User = Depends(current_user),
) -> ProfileResponse:
    user_id = user.id
    try:
        return await profile_service.get_profile_by_user_id(pk=user_id, model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
