from db.crud.prodottiCrud import get_prodotti
from db.services.prodottoSerice import elimina_prodotto

def aggiorna_lista(text_box):
    lista_prodotti = get_prodotti()

    text_box.configure(state="normal")
    text_box.delete("1.0", "end")

    for p in lista_prodotti:
        text_box.insert("end", f"{p}\n\n")

    text_box.configure(state="disabled")

def elimina_prodotto_per_id(entry_pid,text_box):
    pid = entry_pid.get()
    elimina_prodotto(int(pid))
    aggiorna_lista(text_box)

    entry_pid.delete(0, "end")

