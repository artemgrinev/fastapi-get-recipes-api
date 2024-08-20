from typing import List

from fastapi import (
    APIRouter,
    HTTPException,
    Path,
    status
)
from sqlalchemy.exc import NoResultFound

from core.config import settings
from services.product import product_service
from schemas.product import ProductRead, ProductsResponse

router = APIRouter(
    prefix=settings.api.v1.product,
    tags=["Product"],
)


@router.get(
    "/search",
    name="product: search_product_by_name",
    response_model=List[ProductRead]
)
async def search_product_by_name(name: str) -> List[ProductRead]:
    try:
        results = await product_service.search_by_name(name=name)
        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Product {name} not found"
            )

        return results
    except NoResultFound:
        raise HTTPException(status_code=404, detail="No products found")


@router.get(
    "/{product_id}",
    name="product: get_product_by_id",
    response_model=ProductRead
)
async def get_product_by_id(
        product_id: int = Path(title="The ID of the item to get", gt=0, le=1000000000)
) -> ProductRead:
    try:
        product = await product_service.get(pk=product_id)
        if product is not None:
            return product
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Product {product_id} not found"
            )
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))


@router.get(
    "/products",
    name="product: get_products_list",
    response_model=ProductsResponse
)
async def get_products_list(
        limit: int
) -> ProductsResponse:
    try:
        results = await product_service.get_multi(order="id", limit=limit)
        if results is not None:
            products = ProductsResponse()
            products.products = results
            products.total = results.count()
            products.limit = limit
            return products
        else:
            raise HTTPException(
                status_code=404,
                detail=f"Products not found"
            )
    except Exception as e:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, str(e))