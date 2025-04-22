from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import uuid

from app.schemas.user_schema import UserSchema, UserCreateSchema, UserUpdateSchema
import app.crud.user_crud as user_crud
from app.database.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserSchema])
async def get_all_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)

@router.put("/{user_id}", response_model=UserSchema)
async def update_existing_user(user_id: uuid.UUID, user_data: UserUpdateSchema, db: Session = Depends(get_db)):
    updated_user = user_crud.update_user(db, user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}", response_model=dict)
async def delete_existing_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    deleted = user_crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.post("/", response_model=UserSchema)
async def create_new_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    # Check if user with this email already exists
    existing_user = user_crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db, user)

@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/{user_id}/friends/{friend_id}", response_model=UserSchema)
async def add_user_friend(user_id: uuid.UUID, friend_id: uuid.UUID, db: Session = Depends(get_db)):
    user = user_crud.add_friend(db, user_id, friend_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or friend not found")
    return user