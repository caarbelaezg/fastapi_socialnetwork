from pydantic import BaseModel, ConfigDict
from typing import List, Optional
import uuid

class UserSchema(BaseModel):
    id: uuid.UUID
    name: str
    email: str
    friends: List[uuid.UUID] = []

    model_config = ConfigDict(from_attributes=True)

class UserCreateSchema(BaseModel):
    name: str
    email: str

class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
