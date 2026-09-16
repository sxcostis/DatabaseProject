from db.crud.prodottiCrud import (
    create_prodotto,
    update_prodotto,
    delete_prodotto,
    get_prodotto,
)

from db.services.validatoreProdotto import (
    valida_nome,
    valida_category,
    valida_prezzo,
    valida_quantity,
    valida_id
)

def aggiungi_prodotto(nome, category, prezzo, quantity):

    valida_nome(nome)
    valida_category(category)
    valida_prezzo(prezzo)
    valida_quantity(quantity)

    return create_prodotto(nome, category, prezzo, quantity)

def aggiorna_prodotto(pid, **kwargs):
    key_valide = ["nome", "category", "prezzo", "quantity"]

    for key in kwargs:
        if key not in key_valide:
            raise ValueError("Key deve essere valido")

        if key == "nome":
            valida_nome(kwargs["nome"])

        if key == "category":
            valida_category(kwargs["category"])

        if key == "prezzo":
            valida_prezzo(kwargs["prezzo"])

        if key == "quantity":
            valida_quantity(kwargs["quantity"])


    return update_prodotto(pid, **kwargs)

def elimina_prodotto(pid):
    valida_id(pid)
    return delete_prodotto(pid)

def trova_prodotto(pid):
    valida_id(pid)
    return get_prodotto(pid)



