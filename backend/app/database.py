from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_USER = os.environ["MYSQLUSER"]
DATABASE_PASSWORD = os.environ["MYSQLPASSWORD"]
DATABASE_HOST = os.environ["MYSQLHOST"]
DATABASE_PORT = os.environ.get("MYSQLPORT", "3306")
DATABASE_NAME = os.environ["MYSQLDATABASE"]

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
