from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

raw_url = os.environ.get("DATABASE_URL")

if raw_url:
    SQLALCHEMY_DATABASE_URL = raw_url.replace("mysql://", "mysql+pymysql://")
else:
    # Modo local
    DATABASE_USER = os.environ.get("MYSQLUSER", "root")
    DATABASE_PASSWORD = os.environ.get("MYSQLPASSWORD", "")
    DATABASE_HOST = os.environ.get("MYSQLHOST", "maglev.proxy.rlwy.net")
    DATABASE_PORT = int(os.environ.get("MYSQLPORT", 3306))
    DATABASE_NAME = os.environ.get("MYSQLDATABASE", "railway")

    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
    )

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