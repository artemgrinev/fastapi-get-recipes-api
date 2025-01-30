from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from models.mixins import IntIdPkMixin

class IdNameMixin(IntIdPkMixin):
    name: Mapped[str] = mapped_column(String(30), nullable=False)