import datetime
from typing import Optional
from pydantic import BaseModel


class ProfileRead(BaseModel):
    id: int
    user_pk: int
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]


class ProfileCreate(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]


class ProfileUpdate(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]


class ProfileDelete(BaseModel):
    id: int
    user_id: int
    is_active: Optional[bool] = False
