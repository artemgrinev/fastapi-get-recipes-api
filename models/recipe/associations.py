from sqlalchemy import Table, Column, Integer, ForeignKey
from models import Base

recipe_subcategory_associations = Table(
    "recipe_subcategory_associations", 
    Base.metadata, 
    Column("recipe_id", Integer, ForeignKey("recipes.id")),
    Column("subcategory_id", Integer, ForeignKey("recipe_subcategories.id"))
    )

recipe_tag_associations = Table(
    "recipe_tag_associations", 
    Base.metadata, 
    Column("recipe_id", Integer, ForeignKey("recipes.id")),
    Column("tag_id", Integer, ForeignKey("recipe_tags.id"))
    )

ingredient_product_assiociations = Table(
    "ingredient_product_assiociations",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id")),
    Column("ingredients_id", Integer, ForeignKey("recipe_ingredients.id"))
)