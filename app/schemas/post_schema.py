from pydantic import BaseModel

class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    likes: int

    class Config:
        orm_mode = True