from sqlalchemy.orm import Session
from database.models import EngagementPostContent,EngagementPost
from database.schemas import PostContentSchema
from database.models import EngagementPostProductMapping
from database.schemas import ProductPostMappingSchema

def create_post_content(db: Session, content: PostContentSchema):
    # Check if the post_id exists in the engagement_post table
    post_exists = db.query(EngagementPost).filter(EngagementPost.id == content.post_id).first()
    
    if not post_exists:
        raise ValueError(f"Post with id {content.post_id} does not exist.")

    # If post exists, proceed with inserting into engagement_post_content
    db_content = EngagementPostContent(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

def get_content_by_post_id(db: Session, post_id: int):
    return db.query(EngagementPostContent).filter(EngagementPostContent.post_id == post_id).all()

def map_product_to_post(db: Session, mapping):
    # Check if the mapping already exists
    existing_mapping = db.query(EngagementPostProductMapping).filter(
        EngagementPostProductMapping.post_id == mapping.post_id,
        EngagementPostProductMapping.product_id == mapping.product_id
    ).first()

    if existing_mapping:
        return {"detail": "Product already mapped to the post"}

    # Create new product-post mapping
    new_mapping =EngagementPostProductMapping(
        post_id=mapping.post_id,
        product_id=mapping.product_id
    )
    
    db.add(new_mapping)
    db.commit()
    db.refresh(new_mapping)
    
    return {"detail": "Product mapped to post successfully", "mapping": new_mapping}