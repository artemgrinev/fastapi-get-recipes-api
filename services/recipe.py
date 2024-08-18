from services.base_services import BaseServices
from repositories.recipes import recipe_repositories


class RecipeServices(BaseServices):
    pass


recipe_service = RecipeServices(repository=recipe_repositories)
