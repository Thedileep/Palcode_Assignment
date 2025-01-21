from sqlalchemy.orm import Session
from database import models, schemas

# Create an engagement post collection
def create_engagement_post_collection(db: Session, engagement_post_collection: schemas.EngagementPostCollectionCreate):
    db_engagement_post_collection = models.EngagementPostCollection(
        engagement_post_id=engagement_post_collection.engagement_post_id,
        collection_id=engagement_post_collection.collection_id,
        duration_in_seconds=engagement_post_collection.duration_in_seconds
    )
    db.add(db_engagement_post_collection)
    db.commit()
    db.refresh(db_engagement_post_collection)
    return db_engagement_post_collection

# Get all engagement post collections
def get_engagement_post_collections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.EngagementPostCollection).offset(skip).limit(limit).all()

# Get a specific engagement post collection by ID
def get_engagement_post_collection_by_id(db: Session, collection_id: int):
    return db.query(models.EngagementPostCollection).filter(models.EngagementPostCollection.id == collection_id).first()
