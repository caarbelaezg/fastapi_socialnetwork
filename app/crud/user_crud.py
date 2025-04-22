from typing import List, Optional
from sqlalchemy.orm import Session
import uuid

from app.models.user_model import User
from app.schemas.user_schema import UserSchema, UserCreateSchema, UserUpdateSchema

def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()

def create_user(db: Session, user: UserCreateSchema) -> User:
    db_user = User(
        name=user.name, 
        email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: uuid.UUID) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: uuid.UUID, user_data: UserUpdateSchema) -> Optional[User]:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return None
    
    user_data_dict = user_data.model_dump(exclude_unset=True)
    for key, value in user_data_dict.items():
        setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: uuid.UUID) -> bool:
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        return False
    
    db.delete(db_user)
    db.commit()
    return True

def add_friend(db: Session, user_id: uuid.UUID, friend_id: uuid.UUID) -> Optional[User]:
    user = get_user_by_id(db, user_id)
    friend = get_user_by_id(db, friend_id)
    
    if not user or not friend:
        return None
    
    user.friends.append(friend)
    db.commit()
    db.refresh(user)
    return user