from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

database_URL = "mysql+pymysql://root:@localhost:3306/database"

engine = create_engine(database_URL, echo=True)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()