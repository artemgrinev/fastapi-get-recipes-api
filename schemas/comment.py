from pydantic import BaseModel


class CommentBase(BaseModel):
    pass


class CommentRead(BaseModel):
    id: int

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    pass


class CommentUpdate(BaseModel):
    pass


class CommentDelete(BaseModel):
    id: int


