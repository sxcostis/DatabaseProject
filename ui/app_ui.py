import customtkinter as ctk
from ui.aggiungi_prodotto import AggiungiProdotto
from ui.aggiorna_prodotto import AggiornaProdotto


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("Dark")

        self.geometry("1280x820")
        self.title("Gestione Magazzino")
        self.resizable(False, False)

        self.configure(fg_color="#1E1E2E")

        # Gestione Schermate
        self.schermate = {
            "AggiungiProdotto": AggiungiProdotto(parent=self, controller=self),
            "AggiornaProdotto": AggiornaProdotto(parent=self, controller=self),
                          }

        # Mostra la schermata Aggiungi Prodotto
        self.mostra_schermata("AggiungiProdotto")

    def mostra_schermata(self, nome_schermata):
        for schermata in self.schermate.values():
            schermata.pack_forget()

        self.schermate[nome_schermata].pack(fill="both", expand=True)