from fastapi import APIRouter

from core.config import settings
from .profile import router as profile_router
from .recipes import router as recipes_router
from .products import router as product_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    profile_router,
)

router.include_router(
    recipes_router,
)

router.include_router(
    product_router,
)