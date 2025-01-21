from sqlalchemy.orm import Session
from database.models import Collection
from database.schemas import CollectionCreateSchema

# Create a new collection
def create_collection(db: Session, collection: CollectionCreateSchema):
    db_collection = Collection(collection_name=collection.collection_name, post_ids=collection.post_ids)
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection

# Get a collection by ID
def get_collection(db: Session, collection_id: int):
    return db.query(Collection).filter(Collection.id == collection_id).first()

# Get all collections
def get_collections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Collection).offset(skip).limit(limit).all()
