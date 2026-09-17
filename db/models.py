from sqlalchemy import Column, Integer, String, Float
from db.databaseConnector import Base

class Prodotti(Base):
    __tablename__ = 'prodotto'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    prezzo = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __str__(self):
        return f"ID: {self.id}\nNome: {self.nome}\nCategoria: {self.category}\nPrezzo: {self.prezzo}\nQuantitá: {self.quantity}"