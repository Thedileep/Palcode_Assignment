# routes/product_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal  
from database import models, schemas
from CRUD import contents, crud  

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to map product to post
@router.post("/map-product-to-post")
def map_product_to_post(mapping: schemas.ProductPostMappingSchema, db: Session = Depends(get_db)):
    # Check if the post and product exist
    post = db.query(models.EngagementPost).filter(models.EngagementPost.id == mapping.post_id).first()
    product = db.query(models.EngagementPostProduct).filter(models.EngagementPostProduct.id == mapping.product_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Map product to post
    return contents.map_product_to_post(db, mapping)

# Endpoint to create a product
@router.post("/create-product")
def create_product(product: schemas.ProductCreateSchema, db: Session = Depends(get_db)):
    # Check if product with the same SKU already exists
    existing_product = db.query(models.EngagementPostProduct).filter(models.EngagementPostProduct.sku == product.sku).first()
    
    if existing_product:
        raise HTTPException(status_code=400, detail="Product with this SKU already exists.")
    
    # Call CRUD function to create the product
    return crud.create_product(db, product)
