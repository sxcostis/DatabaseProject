from crud import create_prodotto
from db.models import create_tables

create_tables()

for i in range(2):
    try:
        nome  = input("Email: ")
        categoria = input("Cattegoria: ")
        prezzo = float(input("Prezzo: "))
        quantity = int(input("Quantity: "))
        create_prodotto(nome, categoria, prezzo, quantity)
    except Exception as e:
        print(e)