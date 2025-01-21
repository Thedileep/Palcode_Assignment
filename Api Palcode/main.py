from fastapi import FastAPI
from database.db import  engine
from database import models
from routes import engagement_post, engagement_post_content,collectionRoute,engcollRoute,productRoute

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Routes for all path

app.include_router(engagement_post.router, prefix="/api", tags=["Posts"])
app.include_router(engagement_post_content.router, prefix="/api", tags=["Post Content"])
app.include_router(collectionRoute.router, prefix="/api", tags=["Collections"])
app.include_router(engcollRoute.router, prefix="/api", tags=["Engagement Post Collections"])
app.include_router(productRoute.router, prefix="/api", tags=["Product"])
