from sqlalchemy import Column, Integer, String, ForeignKey, Text, JSON, Float
from sqlalchemy.orm import relationship
from database.db import Base

class EngagementPost(Base):
    __tablename__ = "engagement_post"
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=False)  # Differentiates companies
    title = Column(String, nullable=False)  # Post title
    description = Column(String, nullable=True)  # Optional description
    thumbnail_url = Column(String, nullable=True)

    # Relationship to EngagementPostProduct via the mapping table
    products = relationship("EngagementPostProduct", secondary="engagement_post_product_mapping", back_populates="posts")

    # Relationship to EngagementPostContent via post_id
    content = relationship("EngagementPostContent", back_populates="post")

    # Relationship to EngagementPostProductMapping
    product_mappings = relationship("EngagementPostProductMapping", back_populates="post")

    # Relationship to EngagementPostCollection
    collections = relationship("EngagementPostCollection", back_populates="engagement_post")


class EngagementPostContent(Base):
    __tablename__ = "engagement_post_content"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("engagement_post.id"), nullable=False)
    content_url = Column(Text, nullable=False)

    # Relationship back to EngagementPost
    post = relationship("EngagementPost", back_populates="content")


class EngagementPostProductMapping(Base):
    __tablename__ = "engagement_post_product_mapping"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("engagement_post.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("engagement_post_product.id"), nullable=False)

    post = relationship("EngagementPost", back_populates="product_mappings")
    product = relationship("EngagementPostProduct", back_populates="post_mappings")


class EngagementPostProduct(Base):
    __tablename__ = "engagement_post_product"
    
    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    product_image = Column(String, nullable=True)
    sku = Column(String, nullable=False, unique=True)

    # Relationships with EngagementPostProductMapping
    post_mappings = relationship("EngagementPostProductMapping", back_populates="product")
    posts = relationship("EngagementPost", secondary="engagement_post_product_mapping", back_populates="products")


class Collection(Base):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True, index=True)
    collection_name = Column(String, index=True)
    post_ids = Column(JSON)  # Storing post IDs as a JSON array

    # Relationship to EngagementPostCollection
    engagement_posts = relationship("EngagementPostCollection", back_populates="collection")

    def __repr__(self):
        return f"<Collection(id={self.id}, collection_name={self.collection_name})>"


class EngagementPostCollection(Base):
    __tablename__ = "engagement_post_collection"

    id = Column(Integer, primary_key=True, index=True)
    engagement_post_id = Column(Integer, ForeignKey("engagement_post.id"))
    collection_id = Column(Integer, ForeignKey("collections.id"))
    duration_in_seconds = Column(Float)  # Duration of video in seconds

    # Relationships
    engagement_post = relationship("EngagementPost", back_populates="collections")
    collection = relationship("Collection", back_populates="engagement_posts")
