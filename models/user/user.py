from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase
)
from sqlalchemy.orm import (
    Mapped,
    relationship
)

from models import Base
from models.mixins import IntIdPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from models import Profile


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
