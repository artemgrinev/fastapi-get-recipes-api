from pydantic import BaseModel


class Autor(BaseModel):
    profile_id: int
    first_name: str
    last_name: str
