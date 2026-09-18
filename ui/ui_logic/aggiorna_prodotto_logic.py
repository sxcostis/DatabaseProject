from db.crud.prodottiCrud import get_prodotti
from db.services.prodottoSerice import aggiorna_prodotto

def aggiorna_lista(text_box):
    listaProdotti = get_prodotti()
    text_box.configure(state="normal")
    text_box.delete("1.0", "end")

    for p in listaProdotti:
        text_box.insert("end", f"{p}\n\n")
    text_box.configure(state="disabled")

def aggiorna_prodotto_esistente(entry_id,
                            entry_nome,
                            entry_category,
                            entry_prezzo,
                            entry_quantity,
                            text_box):
    pid = entry_id.get()
    nome = entry_nome.get()
    category = entry_category.get()
    prezzo = entry_prezzo.get()
    quantity = entry_quantity.get()

    try:
        pid = int(pid)
    except ValueError as e:
        print(e)
        return
    dict_prodotto = {}

    if nome:
        dict_prodotto["nome"] = nome.strip().capitalize()
        print(dict_prodotto["nome"])

    if category:
        dict_prodotto["category"] = category.strip().capitalize()

    if prezzo:
        dict_prodotto["prezzo"] = float(prezzo)

    if quantity:
        dict_prodotto["quantity"] = int(quantity)

    entry_id.delete(0, "end")
    entry_nome.delete(0, "end")
    entry_category.delete(0, "end")
    entry_prezzo.delete(0, "end")
    entry_quantity.delete(0, "end")

    entry_id.configure(placeholder_text="0")
    entry_nome.configure(placeholder_text="es. Mouse Wireless")
    entry_category.configure(placeholder_text="es. Elettronica")
    entry_prezzo.configure(placeholder_text="0.00")
    entry_quantity.configure(placeholder_text="0")

    try:
        aggiorna_prodotto(pid, dict_prodotto)
    except Exception as e:
        print(e)
        return
    aggiorna_lista(text_box)
