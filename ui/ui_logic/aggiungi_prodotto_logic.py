from db.services.prodottoSerice import aggiungi_prodotto

def aggiungi_prodotto_to_db(entry_nome, entry_categoria, entry_prezzo, entry_quantity):
    nome = entry_nome.get()
    categoria = entry_categoria.get()
    prezzo = entry_prezzo.get()
    quantity = entry_quantity.get()

    prezzo = float(prezzo)
    quantity = int(quantity)


    print(f"Dati letti -> Nome: {nome}, Categoria: {categoria}, Prezzo: {prezzo}, Qtà: {quantity}", flush=True)

    # Svuotiamo i campi dopo la lettura
    entry_nome.delete(0, "end")
    entry_categoria.delete(0, "end")
    entry_prezzo.delete(0, "end")
    entry_quantity.delete(0, "end")

    aggiungi_prodotto(nome, categoria, prezzo, quantity)