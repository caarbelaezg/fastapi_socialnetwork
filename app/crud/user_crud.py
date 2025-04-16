from typing import List, Optional
from app.schemas.user_schema import UserSchema
from app.database.database import users_db

def get_all_users() -> List[UserSchema]:
    return users_db

def create_user(user: UserSchema) -> UserSchema:
    if any(existing_user.id == user.id for existing_user in users_db):
        raise ValueError("The user already exists")
    users_db.append(user)
    return user

def get_user_by_id(user_id: int) -> Optional[UserSchema]:
    for user in users_db:
        if user.id == user_id:
            return user
    return None

def update_user(user_id: int, updated_user: UserSchema) -> UserSchema:
    for index, user in enumerate(users_db):
        if user.id == user_id:
            users_db[index] = updated_user
            return updated_user
    raise ValueError("User not found")

def delete_user(user_id: int) -> bool:
    global users_db
    for user in users_db:
        if user.id == user_id:
            users_db.remove(user)
            return True
    raise ValueError("User not found")

def add_friend(user_id: int, friend_id: int) -> UserSchema:
    user = get_user_by_id(user_id)
    if user is None:
        raise ValueError("User not found")
    
    friend = get_user_by_id(friend_id)
    if friend is None:
        raise ValueError("Friend not found")
    
    if friend_id not in user.friends:
        user.friends.append(friend_id)
    
    return user
    