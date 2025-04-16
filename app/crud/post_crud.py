from typing import List, Optional
from app.schemas.post_schema import PostSchema
from app.database.database import posts_db, users_db

def get_all_posts() -> List[PostSchema]:
    return posts_db

def create_post(post: PostSchema) -> PostSchema:
    if not any(user.id == post.user_id for user in users_db):
        raise ValueError("El usuario autor no existe")
    posts_db.append(post)
    return post

def update_post(post_id: int, updated_post: PostSchema) -> PostSchema:
    for index, post in enumerate(posts_db):
        if post.id == post_id:
            posts_db[index] = updated_post
            return updated_post
    raise ValueError("Post no encontrado")

def delete_post(post_id: int) -> None:
    global posts_db
    for post in posts_db:
        if post.id == post_id:
            posts_db.remove(post)
            return
    raise ValueError("Post no encontrado")

def get_post_by_id(post_id: int) -> Optional[PostSchema]:
    for post in posts_db:
        if post.id == post_id:
            return post
    return None

def like_post(post_id: int) -> PostSchema:
    post = get_post_by_id(post_id)
    if post is None:
        raise ValueError("Post no encontrado")
    post.likes += 1
    return post