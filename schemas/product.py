from typing import List
from pydantic import BaseModel
from schemas import Meta


class ProductBase(BaseModel):
    title: str
    description: str
    category: str
    brand: str
    store: str
    price: float
    discountPercentage: float
    weight: float
    minimumOrderQuantity: int
    shippingInformation: str
    availabilityStatus: str
    images_url: str


class ProductRead(ProductBase):
    id: int
    meta: Meta


class ProductsResponse(BaseModel):
    products: List[ProductRead]
    total: int
    skip: int
    limit: int
