from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

# Database credentials
username = "postgres"
password = quote_plus("Dileep@2020")  # Encodes special characters
host = "localhost"
port = "5432"
database = "palcode"

# Database URL
DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

# Create engine and sessionmaker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare base
Base = declarative_base()
