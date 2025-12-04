from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_USER = os.getenv("MYSQLUSER") or os.getenv("MYSQL_USER")
DATABASE_PASSWORD = os.getenv("MYSQLPASSWORD") or os.getenv("MYSQL_PASSWORD")
DATABASE_HOST = os.getenv("MYSQLHOST") or os.getenv("MYSQL_HOST")
DATABASE_PORT = int(os.getenv("MYSQLPORT") or os.getenv("MYSQL_PORT") or 3306)
DATABASE_NAME = os.getenv("MYSQLDATABASE") or os.getenv("MYSQL_DATABASE")
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()