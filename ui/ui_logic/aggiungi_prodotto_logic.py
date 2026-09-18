from db.services.prodottoSerice import aggiungi_prodotto
from db.crud.prodottiCrud import get_prodotti

def aggiungi_prodotto_to_db(entry_nome, entry_categoria, entry_prezzo, entry_quantity, text_box):
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    prezzo = entry_prezzo.get()
    quantity = entry_quantity.get()

    nome = nome.strip().capitalize()
    categoria = categoria.strip().capitalize()
    prezzo = float(prezzo)
    quantity = int(quantity)


    print(f"Dati letti -> Nome: {nome}, Categoria: {categoria}, Prezzo: {prezzo}, Qtà: {quantity}", flush=True)


    entry_nome.delete(0, "end")
    entry_categoria.delete(0, "end")
    entry_prezzo.delete(0, "end")
    entry_quantity.delete(0, "end")
    aggiungi_prodotto(nome, categoria, prezzo, quantity)
    aggiorna_lista(text_box)

def aggiorna_lista(text_box):
    listaProdotti = get_prodotti()
    text_box.configure(state="normal")
    text_box.delete("1.0", "end")

    for p in listaProdotti:
        text_box.insert("end", f"{p}\n\n")
    text_box.configure(state="disabled")