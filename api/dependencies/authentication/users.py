from typing import (
    TYPE_CHECKING,
    Annotated
)

from fastapi import Depends

from api.routers.fastapi_users_routers import fastapi_users
from core.db.db_helper import db_helper
from models import (
    User
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter)
    ],
):
    yield User.get_db(session=session)

current_user = fastapi_users.current_user()
