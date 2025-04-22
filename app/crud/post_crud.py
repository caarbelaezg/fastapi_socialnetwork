from typing import List, Optional
from sqlalchemy.orm import Session
import uuid

from app.models.post_model import Post
from app.models.user_model import User
from app.schemas.post_schema import PostCreateSchema

def get_all_posts(db: Session) -> List[Post]:
    return db.query(Post).all()

def create_post(db: Session, post: PostCreateSchema, user_id: uuid.UUID) -> Post:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    
    db_post = Post(
        content=post.content,
        user_id=user_id
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post_by_id(db: Session, post_id: uuid.UUID) -> Optional[Post]:
    return db.query(Post).filter(Post.id == post_id).first()

def update_post(db: Session, post_id: uuid.UUID, content: str) -> Optional[Post]:
    db_post = get_post_by_id(db, post_id)
    if not db_post:
        return None
    
    db_post.content = content
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: uuid.UUID) -> bool:
    db_post = get_post_by_id(db, post_id)
    if not db_post:
        return False
    
    db.delete(db_post)
    db.commit()
    return True

def get_user_posts(db: Session, user_id: uuid.UUID) -> List[Post]:
    return db.query(Post).filter(Post.user_id == user_id).all()