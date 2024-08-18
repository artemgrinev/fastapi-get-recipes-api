from typing import List
from pydantic import BaseModel
from datetime import datetime


class Dimensions(BaseModel):
    width: float
    height: float
    depth: float


class Meta(BaseModel):
    createdAt: datetime
    updatedAt: datetime


class ProductRead(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    tags: List[str]
    brand: str
    weight: float
    dimensions: Dimensions
    shippingInformation: str
    availabilityStatus: str
    returnPolicy: str
    minimumOrderQuantity: int
    meta: Meta
    thumbnail: str
    images: List[str]


class ProductsResponse(BaseModel):
    products: List[ProductRead]
    total: int
    skip: int
    limit: int
