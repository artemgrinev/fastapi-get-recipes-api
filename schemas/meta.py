import datetime
from pydantic import BaseModel


class Meta(BaseModel):
    createdAt: datetime.datetime
    updatedAt: datetime.datetime
