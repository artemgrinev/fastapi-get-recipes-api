from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from api.dependencies.authentication.users import current_user
from core.config import settings
from schemas import RecipeRead, RecipeCreate
from services.recipe import recipe_service

router = APIRouter(
    prefix=settings.api.v1.recipes,
    tags=["Recipes"],
)


@router.post("/", response_model=RecipeRead, status_code=status.HTTP_201_CREATED)
async def create_recipe(recipe: RecipeCreate, user: Depends(current_user)):
    try:
        return await recipe_service.create(model=recipe)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/", response_model=List[RecipeRead])
async def read_recipes(order: str, limit: int = 10):
    try:
        return await recipe_service.get_multi(order=order, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Recipes not found")


@router.get("/{recipe_id}", response_model=RecipeRead)
async def read_recipe(recipe_id: int):
    try:
        return await recipe_service.get(pk=recipe_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="Recipes not found")


@router.put("/{recipe_id}", response_model=RecipeRead)
async def update_recipe(recipe_id: int, recipe: RecipeCreate):
    recipe_db = await recipe_service.get(pk=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    try:
        return await recipe_service.update(pk=recipe_id, model=recipe)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
