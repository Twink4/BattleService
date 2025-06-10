from pydantic import (BaseModel)


class SchemaUser(BaseModel):
    name: str
    power: int
    