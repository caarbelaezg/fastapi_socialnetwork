from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.post_schema import PostSchema
from app.crud.post_crud import get_all_posts, create_post, like_post, update_post, delete_post

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[PostSchema])
async def read_posts():
    return get_all_posts()

@router.post("/", response_model=PostSchema)
async def create_new_post(post: PostSchema):
    try:
        return create_post(post)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{post_id}", response_model=PostSchema)
async def update_existing_post(post_id: int, updated_post: PostSchema):
    try:
        return update_post(post_id, updated_post)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{post_id}", response_model=dict)
async def delete_existing_post(post_id: int):
    try:
        delete_post(post_id)
        return {"mensaje": "Post eliminado correctamente"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{post_id}/like", response_model=PostSchema)
async def like_a_post(post_id: int):
    try:
        return like_post(post_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
