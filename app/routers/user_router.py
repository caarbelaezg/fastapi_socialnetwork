from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user_schema import UserSchema
import app.crud.user_crud as user_crud

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserSchema])
async def get_all_users():
    return user_crud.get_all_users()

@router.put("/{user_id}", response_model=UserSchema)
async def update_existing_user(user_id: int, updated_user: UserSchema):
    try:
        return user_crud.update_user(user_id, updated_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{user_id}", response_model=dict)
async def delete_existing_user(user_id: int):
    try:
        user_crud.delete_user(user_id)
        return {"mensaje": "Usuario eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=UserSchema)
async def create_new_user(user: UserSchema):
    try:
        return user_crud.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 

@router.get("/{user_id}", response_model=UserSchema)
async def read_user(user_id: int):
    user = user_crud.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("{user_id}/friends/{friend_id}", response_model=UserSchema)
async def add_user_friend(user_id: int, friend_id: int):
    try:
        return user_crud.add_friend(user_id, friend_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        