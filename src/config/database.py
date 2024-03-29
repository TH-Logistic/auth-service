from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import settings
import pymongo
from src.models.indexes import createIndex
from src.config.settings import Settings

settings = Settings()

engine = create_engine(settings.get_postgres_database_url())
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


mongo_client = pymongo.MongoClient(settings.get_mongo_database_url())

mongo_db = mongo_client[settings.mongo_initdb_database]

createIndex(mongo_db)
