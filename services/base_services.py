from typing import List

from schemas.base_schemas import PyModel
from repositories.base_repository import AbstractRepository
from repositories.sqlalchemy_repository import ModelType


class BaseServices:
    def __init__(self, repository: AbstractRepository) -> None:
        self.repository: AbstractRepository = repository

    async def create(self, model: PyModel) -> ModelType:
        return await self.repository.create(data=model.model_dump())

    async def get(self, pk: int) -> ModelType:
        return await self.repository.get_single(id=pk)

    async def update(self, pk: int, model: PyModel) -> ModelType:
        return await self.repository.update(data=model.model_dump(), id=pk)

    async def delete(self, pk: int) -> None:
        await self.repository.delete(id=pk)

    async def get_multi(
            self,
            order: str,
            limit: int,
            offset: int
    ) -> list[ModelType]:
        await self.repository.get_multi(order=order, limit=limit, offset=offset)
