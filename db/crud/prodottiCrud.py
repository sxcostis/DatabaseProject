from db.models import Prodotti
from db.databaseConnector import get_session

def create_prodotto(nome, category, prezzo, quantity):
    with get_session() as session:
        prodotto = Prodotti(nome=nome,
                            category=category,
                            prezzo=prezzo,
                            quantity=quantity)
        session.add(prodotto)

def get_prodotto(pid):
    with get_session() as session:
        prodotto = session.query(Prodotti).filter(Prodotti.id == pid).first()
        return prodotto

def get_prodotti():
    with get_session() as session:
        return session.query(Prodotti).all()

def update_prodotto(pid, dict):
    with get_session() as session:
        prodotto = session.query(Prodotti).filter(Prodotti.id == pid).first()
        for key, value in dict.items():
            setattr(prodotto, key, value)

def delete_prodotto(pid):
    with get_session() as session:
        prodotto = session.query(Prodotti).filter(Prodotti.id == pid).first()
        session.delete(prodotto)

