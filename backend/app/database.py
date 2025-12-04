from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_USER = os.getenv("MYSQLUSER")
DATABASE_PASSWORD = os.getenv("MYSQLPASSWORD")
DATABASE_HOST = os.getenv("MYSQLHOST")
DATABASE_PORT = int(os.getenv("MYSQLPORT"))
DATABASE_NAME = os.getenv("MYSQLDATABASE")

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()