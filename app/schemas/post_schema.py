from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class PostSchema(BaseModel):
    id: uuid.UUID
    content: str
    timestamp: datetime
    user_id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)

class PostCreateSchema(BaseModel):
    content: str
