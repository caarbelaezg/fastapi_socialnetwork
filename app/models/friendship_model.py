import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Friendship(Base):
    __tablename__ = "friendships"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    friend_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)