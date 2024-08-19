from pydantic import BaseModel


class CommentBase(BaseModel):
    pass


class CommentRead(BaseModel):
    id: int


class CommentCreate(BaseModel):
    pass


class CommentUpdate(BaseModel):
    pass


class CommentDelete(BaseModel):
    id: int


