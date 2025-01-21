from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.schemas import CollectionCreateSchema, CollectionResponseSchema
from database.db import SessionLocal
from CRUD import collections
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new collection
@router.post("/collections/", response_model=CollectionResponseSchema)
def create_collection(collection: CollectionCreateSchema, db: Session = Depends(get_db)):
    db_collection = collections.create_collection(db=db, collection=collection)
    return db_collection

# Endpoint to get a collection by its ID
@router.get("/collections/{collection_id}", response_model=CollectionResponseSchema)
def get_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = collections.get_collection(db=db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return db_collection

# Endpoint to get all collections with pagination
@router.get("/collections/", response_model=List[CollectionResponseSchema])
def get_collections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    collectionsp = collections.get_collections(db=db, skip=skip, limit=limit)
    return collectionsp
