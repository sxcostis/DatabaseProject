from db.database import Base
from sqlalchemy import Column, Integer, String, Float

class Prodotto(Base):
    __tablename__ = 'Prodotti'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    categoria = Column(String(50), nullable=False)
    prezzo = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    def __str__(self):
        return f"Nome: {self.nome} - Categoria: {self.categoria} - \nPrezzo: {self.prezzo} - Quantitá: {self.quantity}"