from db.database import Base, engine
from db.schemas import Prodotto

def create_tables():
    Base.metadata.create_all(engine)
