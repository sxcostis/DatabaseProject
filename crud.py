from db.database import get_session
from db.schemas import Prodotto


def create_prodotto(nome, categoria, prezzo, quantity):
    with get_session() as session:
        prodotto = Prodotto(nome=nome, categoria=categoria, prezzo=prezzo, quantity=quantity)
        session.add(prodotto)

def update_prodotto(id, nome, categoria, prezzo, quantity):
    with get_session() as session:
        prodotto = session.query(Prodotto).filter_by(id=id).first()
        prodotto.nome = nome
        prodotto.categoria = categoria
        prodotto.prezzo = prezzo
        prodotto.quantity = quantity

def delete_prodotto(id):
    with get_session() as session:
        prodotto = session.query(Prodotto).filter_by(id=id).first()
        session.delete(prodotto)

def lista_prodotti():
    with get_session() as session:
        return session.query(Prodotto).all()