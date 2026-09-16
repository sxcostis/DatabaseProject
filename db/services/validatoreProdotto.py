def valida_nome(nome):
    if not isinstance(nome, str) or nome.strip() == "":
        raise ValueError("Nome deve essere una stringa e contenere almeno un carattere")
    if len(nome) > 50:
        raise ValueError("Nome non deve essere maggiore di 50 carattere")

def valida_category(category):
    if not isinstance(category, str) or category.strip() == "":
        raise ValueError("Categoria deve essere una stringa e contenere almeno un carattere")
    if len(category) > 50:
        raise ValueError("Categoria non deve essere maggiore di 50 carattere")

def valida_prezzo(prezzo):
    if not isinstance(prezzo, (int,float)) or prezzo <= 0:
        raise ValueError("Prezzo deve essere un numero valido")

def valida_quantity(quantity):
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError("Quantitá deve essere un numero valido")

def valida_id(pid):
    if not isinstance(pid, int) or pid < 0:
        raise ValueError("ID deve essere valido")