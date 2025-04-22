from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
import uuid

from app.schemas.post_schema import PostSchema, PostCreateSchema
import app.crud.post_crud as post_crud
from app.database.database import get_db

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[PostSchema])
async def read_posts(db: Session = Depends(get_db)):
    return post_crud.get_all_posts(db)

@router.post("/", response_model=PostSchema)
async def create_new_post(post: PostCreateSchema, user_id: uuid.UUID, db: Session = Depends(get_db)):
    try:
        return post_crud.create_post(db, post, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{post_id}", response_model=PostSchema)
async def update_existing_post(post_id: uuid.UUID, content: str, db: Session = Depends(get_db)):
    updated_post = post_crud.update_post(db, post_id, content)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/{post_id}", response_model=dict)
async def delete_existing_post(post_id: uuid.UUID, db: Session = Depends(get_db)):
    deleted = post_crud.delete_post(db, post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}

@router.get("/{post_id}", response_model=PostSchema)
async def get_post(post_id: uuid.UUID, db: Session = Depends(get_db)):
    post = post_crud.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/user/{user_id}", response_model=List[PostSchema])
async def get_user_posts(user_id: uuid.UUID, db: Session = Depends(get_db)):
    return post_crud.get_user_posts(db, user_id)
