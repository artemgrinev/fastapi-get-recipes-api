from fastapi import APIRouter

from core.config import settings
from core.schemas.product import (
    ProductRead,
    ProductsResponse
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Product"],
)

