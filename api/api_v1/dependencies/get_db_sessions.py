from sqlalchemy.ext.asyncio import AsyncSession

from core.db.db_helper import db_helper


async def get_session() -> AsyncSession:
    async with db_helper.session_getter() as session:
        yield session
