import customtkinter as ctk



class AggiornaProdotto(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="transparent")
        self.controller = controller

        # Configurazione Layout
        self.grid_columnconfigure(0, weight=0, minsize=220)
        self.grid_columnconfigure(1, weight=0, minsize=530)
        self.grid_columnconfigure(2, weight=0, minsize=530)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # COLONNA 1
        # ==========================================
        self.sidebar_frame = ctk.CTkFrame(self, fg_color="#181825", corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame,
            text="MAGAZZINO",
            font=("Bahnschrift", 26, "bold"),
            text_color="#89B4FA"
        )
        self.logo_label.pack(pady=(30, 40), padx=20)

        self.btn_nav_aggiungi_prodotto = ctk.CTkButton(
            self.sidebar_frame,
            text="Aggiungi Prodotto",
            font=("Bahnschrift", 18, "bold"),
            fg_color="transparent",
            text_color="#A6ADC8",
            hover_color="#45475A",
            height=45,
            anchor="w",
            command=lambda: self.controller.mostra_schermata("AggiungiProdotto")
        )
        self.btn_nav_aggiungi_prodotto.pack(fill="x", padx=15, pady=8)

        self.btn_nav_aggiorna_prodotto = ctk.CTkButton(
            self.sidebar_frame,
            text="Aggiorna Prodotto",
            font=("Bahnschrift", 18, "bold"),
            fg_color="#45475A",
            text_color="#A6ADC8",
            hover_color="#45475A",
            height=45,
            anchor="w",
        )
        self.btn_nav_aggiorna_prodotto.pack(fill="x", padx=15, pady=8)

        self.btn_nav_elimina_prodotto = ctk.CTkButton(
            self.sidebar_frame,
            text="Elimina Prodotto",
            font=("Bahnschrift", 18, "bold"),
            fg_color="transparent",
            text_color="#A6ADC8",
            hover_color="#313244",
            height=45,
            anchor="w"
        )
        self.btn_nav_elimina_prodotto.pack(fill="x", padx=15, pady=8)

        self.btn_nav_trova_prodotto = ctk.CTkButton(
            self.sidebar_frame,
            text="Trova Prodotto",
            font=("Bahnschrift", 18, "bold"),
            fg_color="transparent",
            text_color="#A6ADC8",
            hover_color="#313244",
            height=45,
            anchor="w"
        )
        self.btn_nav_trova_prodotto.pack(fill="x", padx=15, pady=8)

        # ==========================================
        # COLONNA 2
        # ==========================================
        self.center_frame = ctk.CTkFrame(self, fg_color="#2B2B3B", corner_radius=15)
        self.center_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.titolo_center = ctk.CTkLabel(
            self.center_frame,
            text="Aggiorna Prodotto",
            font=("Bahnschrift", 24, "bold"),
            text_color="#CDD6F4"
        )
        self.titolo_center.pack(pady=(25, 20), padx=20, anchor="w")

        self.lbl_nome = ctk.CTkLabel(
            self.center_frame,
            text="Nome Prodotto",
            font=("Bahnschrift", 14),
            text_color="#A6ADC8"
        )
        self.lbl_nome.pack(anchor="w", padx=25, pady=(10, 2))

        self.entry_nome = ctk.CTkEntry(
            self.center_frame,
            placeholder_text="es. Mouse Wireless",
            height=40,
            fg_color="#181825",
            border_color="#45475A",
            text_color="#CDD6F4"
        )
        self.entry_nome.pack(fill="x", padx=25, pady=(0, 15))

        self.lbl_categoria = ctk.CTkLabel(
            self.center_frame,
            text="Categoria",
            font=("Bahnschrift", 14),
            text_color="#A6ADC8"
        )
        self.lbl_categoria.pack(anchor="w", padx=25, pady=(10, 2))

        self.entry_categoria = ctk.CTkEntry(
            self.center_frame,
            placeholder_text="es. Elettronica",
            height=40,
            fg_color="#181825",
            border_color="#45475A",
            text_color="#CDD6F4"
        )
        self.entry_categoria.pack(fill="x", padx=25, pady=(0, 15))

        self.lbl_prezzo = ctk.CTkLabel(
            self.center_frame,
            text="Prezzo (€)",
            font=("Bahnschrift", 14),
            text_color="#A6ADC8"
        )
        self.lbl_prezzo.pack(anchor="w", padx=25, pady=(10, 2))

        self.entry_prezzo = ctk.CTkEntry(
            self.center_frame,
            placeholder_text="0.00",
            height=40,
            fg_color="#181825",
            border_color="#45475A",
            text_color="#CDD6F4"
        )
        self.entry_prezzo.pack(fill="x", padx=25, pady=(0, 25))

        self.lbl_quantity = ctk.CTkLabel(
            self.center_frame,
            text="Quantitá",
            font=("Bahnschrift", 14),
            text_color="#A6ADC8"
        )
        self.lbl_quantity.pack(anchor="w", padx=25, pady=(10, 2))

        self.entry_quantity = ctk.CTkEntry(
            self.center_frame,
            placeholder_text="0",
            height=40,
            fg_color="#181825",
            border_color="#45475A",
            text_color="#CDD6F4"
        )
        self.entry_quantity.pack(fill="x", padx=25, pady=(0, 25))

        self.btn_salva = ctk.CTkButton(
            self.center_frame,
            text="Salva Prodotto",
            font=("Bahnschrift", 16, "bold"),
            fg_color="#89B4FA",
            text_color="#11111B",
            hover_color="#74C7EC",
            height=45,
            corner_radius=10
        )
        self.btn_salva.pack(fill="x", padx=25, pady=10)

        # ==========================================
        # COLONNA 3
        # ==========================================
        self.right_frame = ctk.CTkFrame(self, fg_color="#2B2B3B", corner_radius=15)
        self.right_frame.grid(row=0, column=2, padx=(0, 20), pady=20, sticky="nsew")

        self.titolo_right = ctk.CTkLabel(
            self.right_frame,
            text="Registro / Lista",
            font=("Bahnschrift", 24, "bold"),
            text_color="#CDD6F4"
        )
        self.titolo_right.pack(pady=(25, 15), padx=20, anchor="w")

        # Textbox Stilizzata
        self.output_textbox = ctk.CTkTextbox(
            self.right_frame,
            fg_color="#181825",
            text_color="#CDD6F4",
            border_color="#45475A",
            border_width=1,
            corner_radius=10,
            font=("Consolas", 14),
            state="disabled"
        )
        self.output_textbox.pack(fill="both", expand=True, padx=20, pady=(0, 20))