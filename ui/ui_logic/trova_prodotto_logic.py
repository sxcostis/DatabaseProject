from db.crud.prodottiCrud import get_prodotti
from db.services.prodottoSerice import trova_prodotto

def aggiorna_lista(text_box):
    lista_prodotti = get_prodotti()

    text_box.configure(state="normal")
    text_box.delete("1.0", "end")

    for p in lista_prodotti:
        text_box.insert("end", f"{p}\n\n")

    text_box.configure(state="disabled")


def trova_prodotto_ui(entry_id, text_box):
    try:
        pid = int(entry_id.get())
        prodotto = trova_prodotto(pid)
    except ValueError as e:
        print(e)

    text_box.configure(state="normal")
    text_box.delete("1.0", "end")

    text_box.insert("end", f"{prodotto}\n\n")

    text_box.configure(state="disabled")
