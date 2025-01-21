from pydantic import BaseModel
from typing import List

class PostCreateSchema(BaseModel):
    tenant_id: int
    title: str
    description: str | None = None
    thumbnail_url: str | None = None

class PostSchema(PostCreateSchema):
    id: int

    class Config:
        orm_mode = True

class PostContentSchema(BaseModel):
    post_id: int
    content_url: str

    class Config:
        orm_mode = True

class ProductPostMappingSchema(BaseModel):
    post_id: int
    product_id: int

    class Config:
        orm_mode = True

class ProductCreateSchema(BaseModel):
    product_name: str
    product_image: str | None = None
    sku: str

    class Config:
        orm_mode = True

class CollectionCreateSchema(BaseModel):
    collection_name: str
    post_ids: List[int]  
    class Config:
        orm_mode = True

class CollectionResponseSchema(CollectionCreateSchema):
    id: int  

    class Config:
        orm_mode = True

class EngagementPostCollectionBase(BaseModel):
    engagement_post_id: int
    collection_id: int
    duration_in_seconds: float

    class Config:
        orm_mode = True

class EngagementPostCollectionCreate(EngagementPostCollectionBase):
    pass

class EngagementPostCollectionResponse(EngagementPostCollectionBase):
    id: int

    class Config:
        orm_mode = True