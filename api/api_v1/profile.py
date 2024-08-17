from fastapi import APIRouter

from core.config import settings
from core.schemas.profile import (
    ProfileRead,
    ProfileCreate,
    ProfileDelete,
    ProfileUpdate
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Profile"],
)
