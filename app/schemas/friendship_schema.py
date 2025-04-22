from pydantic import BaseModel, ConfigDict
import uuid

class FriendshipSchema(BaseModel):
    user_id: uuid.UUID
    friend_id: uuid.UUID
    
    model_config = ConfigDict(from_attributes=True)

class FriendshipCreateSchema(BaseModel):
    friend_id: uuid.UUID
