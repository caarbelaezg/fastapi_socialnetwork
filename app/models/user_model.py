import uuid
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from sqlalchemy import String, Uuid

class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    
    friends: Mapped[List["User"]] = relationship(
        "User",
        secondary="friendships",
        primaryjoin="User.id==Friendship.user_id",
        secondaryjoin="User.id==Friendship.friend_id",
        backref="friend_of"
    )
