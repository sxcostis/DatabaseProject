import customtkinter as ctk

from elimina_prodotto import EliminaProdotto
from trova_prodotto import TrovaProdotto
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
            "EliminaProdotto": EliminaProdotto(parent=self, controller=self),
            "TrovaProdotto": TrovaProdotto(parent=self, controller=self)
                          }

        # Mostra la schermata Aggiungi Prodotto
        self.mostra_schermata("AggiungiProdotto")

    def mostra_schermata(self, nome_schermata):
        for schermata in self.schermate.values():
            schermata.pack_forget()

        schermata_corrente = self.schermate[nome_schermata]
        schermata_corrente.pack(fill="both", expand=True)

        if hasattr(schermata_corrente, "aggiorna_lista_prodotto"):  #hasattr se trova un metodo "..." esegue qualcosa a mia scelta
            schermata_corrente.aggiorna_lista_prodotto()