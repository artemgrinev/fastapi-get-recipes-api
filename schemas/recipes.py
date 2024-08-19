from typing import List
from pydantic import BaseModel, HttpUrl

from schemas import (
    RecipeCategory,
    ProductRead,
    Meta,
    Autor,
)


class RecipeBase(BaseModel):
    name: str
    ingredients: List[ProductRead]
    cuisine: str
    category: List[RecipeCategory]
    autor: Autor
    prepTimeMinutes: int
    cookTimeMinutes: int
    caloriesPerServing: int
    image: HttpUrl
    reviewCount: int


class RecipeCreate(RecipeBase):
    pass


class RecipeRead(RecipeBase):
    id: int
    rating: float
    meta: Meta


class RecipeUpdate(RecipeBase):
    pass


class RecipeDelete(RecipeBase):
    pass


class RecipeResponse(BaseModel):
    recipes: List[RecipeRead]
    total: int
    skip: int
    limit: int


