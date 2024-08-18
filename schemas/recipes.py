from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class Review(BaseModel):
    rating: int
    comment: str
    date: datetime
    reviewerName: str


class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    instructions: List[str]
    prepTimeMinutes: int
    cookTimeMinutes: int
    servings: int
    difficulty: str
    cuisine: str
    caloriesPerServing: int
    tags: List[str]
    userId: int
    image: HttpUrl
    rating: float
    reviewCount: int
    mealType: List[str]


class RecipeResponse(BaseModel):
    recipes: List[Recipe]
    total: int
    skip: int
    limit: int


