from fastapi import APIRouter

from core.config import settings
from core.schemas.recipes import (
    Recipe,
    RecipeResponse
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Recipes"],
)
