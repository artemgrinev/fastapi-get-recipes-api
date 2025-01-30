from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from models.mixins import IntIdPkMixin

class IdTitleMixin(IntIdPkMixin):
    title: Mapped[str] = mapped_column(String, nullable=False)