from sqlalchemy.orm import Session
from database.models import EngagementPost, EngagementPostContent,EngagementPostProduct
from database.schemas import PostCreateSchema,ProductCreateSchema

# Fetch posts by tenant_id
def get_posts_by_tenant(db: Session, tenant_id: int):
    return db.query(EngagementPost).filter(EngagementPost.tenant_id == tenant_id).all()

# Create a new post
def create_post(db: Session, post: PostCreateSchema):
    db_post = EngagementPost(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# Update a post
def update_post(db: Session, post_id: int, post_data: PostCreateSchema):
    post = db.query(EngagementPost).filter(EngagementPost.id == post_id).first()
    if post:
        for key, value in post_data.dict().items():
            setattr(post, key, value)
        db.commit()
        db.refresh(post)
        return post
    return None

# Delete a post
def delete_post(db: Session, post_id: int):
    post = db.query(EngagementPost).filter(EngagementPost.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False

def create_product(db: Session, product: ProductCreateSchema):
    db_product = EngagementPostProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

