from pydantic import BaseModel


class RecipeCategory(BaseModel):
    id: int
    title: str
