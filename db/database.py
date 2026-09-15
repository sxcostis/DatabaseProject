from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"mysql+pymysql://{os.getenv('DB_USER')}"
    f"@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL,echo=True,pool_recycle=3600)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def get_session():
    session = SessionLocal()
    
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()