from pydantic import BaseModel
from typing import List

class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    friends: List[int] = []

    class Config:
        orm_mode = True
