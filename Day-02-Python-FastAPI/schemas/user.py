from pydantic import BaseModel, Field


class User(BaseModel):
    name: str
    email: str
    age: int = Field(ge=18)