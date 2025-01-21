# post_content_router.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.schemas import PostContentSchema
from database.db import SessionLocal
from CRUD import contents
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create post content
@router.post("/post-content")
def create_post_content(content: PostContentSchema, db: Session = Depends(get_db)):
    return contents.create_post_content(db, content)

# Endpoint to fetch content by post ID
@router.get("/post-content/{post_id}")
def fetch_content_by_post_id(post_id: int, db: Session = Depends(get_db)):
    contentsp = contents.get_content_by_post_id(db, post_id)
    if not contentsp:
        raise HTTPException(status_code=404, detail="Content not found for the given post ID")
    return contentsp
