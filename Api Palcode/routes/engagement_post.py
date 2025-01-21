# posts_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database.schemas import PostCreateSchema, PostSchema  
from database.db import SessionLocal, engine
from CRUD import crud  

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fetch all posts for a tenant
@router.get("/posts/{tenant_id}", response_model=List[PostSchema])
def fetch_posts(tenant_id: int, db: Session = Depends(get_db)):
    posts = crud.get_posts_by_tenant(db, tenant_id)
    if not posts:
        raise HTTPException(status_code=404, detail="No posts found for the given tenant_id")
    return posts

# Create a new post
@router.post("/posts", response_model=PostSchema)
def create_post(post: PostCreateSchema, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

# Update an existing post
@router.put("/posts/{post_id}", response_model=PostSchema)
def update_post(post_id: int, post: PostCreateSchema, db: Session = Depends(get_db)):
    updated_post = crud.update_post(db, post_id, post)
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

# Delete a post
@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    success = crud.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"detail": "Post deleted successfully"}
