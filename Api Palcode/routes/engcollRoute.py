from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import schemas  
from database.db import SessionLocal
from CRUD import postCollection

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new engagement post collection
@router.post("/engagement-post-collections/", response_model=schemas.EngagementPostCollectionResponse)
def create_engagement_post_collection(
    engagement_post_collection: schemas.EngagementPostCollectionCreate, db: Session = Depends(get_db)
):
    db_engagement_post_collection = postCollection.create_engagement_post_collection(db=db, engagement_post_collection=engagement_post_collection)
    return db_engagement_post_collection

# Get all engagement post collections with pagination
@router.get("/engagement-post-collections/", response_model=List[schemas.EngagementPostCollectionResponse])
def get_engagement_post_collections(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    engagement_post_collections = postCollection.get_engagement_post_collections(db=db, skip=skip, limit=limit)
    return engagement_post_collections

# Get a specific engagement post collection by ID
@router.get("/engagement-post-collections/{collection_id}", response_model=schemas.EngagementPostCollectionResponse)
def get_engagement_post_collection_by_id(collection_id: int, db: Session = Depends(get_db)):
    db_engagement_post_collection = postCollection.get_engagement_post_collection_by_id(db=db, collection_id=collection_id)
    if db_engagement_post_collection is None:
        raise HTTPException(status_code=404, detail="Engagement post collection not found")
    return db_engagement_post_collection
