from datetime import datetime

from pydantic import BaseModel


class Review(BaseModel):
    rating: int
    comment: str
    date: datetime
    reviewerName: str
