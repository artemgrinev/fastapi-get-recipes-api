from typing import NewType

from pydantic import BaseModel, Field

PyModel = NewType("PyModel", BaseModel)


class Base(BaseModel):
    class ConfigDict:
        from_attributes = True
