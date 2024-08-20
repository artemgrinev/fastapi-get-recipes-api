import datetime
from typing import Optional
from pydantic import BaseModel


class ProfileBase(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]
    is_active: bool = True


class ProfileRead(ProfileBase):
    id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]


class ProfileCreate(ProfileBase):
    user_pk: Optional[int]
    created_at: Optional[datetime.datetime] = datetime.datetime.utcnow
    updated_at: Optional[datetime.datetime] = datetime.datetime.utcnow


class ProfileUpdate(ProfileBase):
    pass


class ProfileDelete(BaseModel):
    id: int


