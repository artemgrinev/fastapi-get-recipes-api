from fastapi import APIRouter

from core.config import settings
from .auth import router as auth_router
from api.api_v1.routers import router as api_v1_router

router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(auth_router)
router.include_router(api_v1_router)
