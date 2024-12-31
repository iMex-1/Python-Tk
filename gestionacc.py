from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

class Compte(ABC):
    def __init__(self, numero, proprietaire, solde_initial):
        self.numero = numero
        self.proprietaire = proprietaire
        self.solde_initial = solde_initial

    @abstractmethod
    def obtenir_informations(self):
        pass

class CompteCourant(Compte):
    def __init__(self, numero, proprietaire, solde_initial, montant_decouvert):
        super().__init__(numero, proprietaire, solde_initial)
        self.montant_decouvert = montant_decouvert

    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial, "Courant", "-", self.montant_decouvert)

class CompteEpargne(Compte):
    def __init__(self, numero, proprietaire, solde_initial, taux_interet):
        super().__init__(numero, proprietaire, solde_initial)
        self.taux_interet = taux_interet

    def obtenir_informations(self):
        return (self.numero, self.proprietaire, self.solde_initial, "Épargne", self.taux_interet, "-")

class GestionComptesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des Comptes Bancaires")
        self.geometry("1000x500")
        
        self.numero = 1
        self.type_var = tk.StringVar(value="Courant")
        self.proprietaire_var = tk.StringVar()
        self.solde_var = tk.DoubleVar()
        self.taux_interet_var = tk.DoubleVar()
        self.montant_decouvert_var = tk.DoubleVar()

        self.comptes = []
        self.creer_widgets()

    def creer_widgets(self):
        tk.Label(self, text="Numéro:", font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Label(self, textvariable=tk.StringVar(value=str(self.numero)), font=("Arial", 12)).grid(row=0, column=1, sticky="w", padx=10, pady=5)
        tk.Label(self, text="Propriétaire:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self, textvariable=self.proprietaire_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self, text="Solde Initial:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self, textvariable=self.solde_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)
        tk.Label(self, text="Euro", font=("Arial", 12)).grid(row=2, column=2, sticky="w", padx=10, pady=5)
        tk.Label(self, text="Type:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=10, pady=5)

        tk.Radiobutton(self, text="Courant", variable=self.type_var, value="Courant", font=("Arial", 12), command=self.toggle_fields).grid(row=3, column=1, padx=10, pady=5, sticky="w")
        tk.Radiobutton(self, text="Épargne", variable=self.type_var, value="Épargne", font=("Arial", 12), command=self.toggle_fields).grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        tk.Label(self, text="Taux Intérêt:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=10, pady=5)
        self.taux_interet_entry = tk.Entry(self, textvariable=self.taux_interet_var, font=("Arial", 12), state="disabled")
        self.taux_interet_entry.grid(row=5, column=1, padx=10, pady=5)
        tk.Label(self, text="M. Découvert:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=10, pady=5)
        self.montant_decouvert_entry = tk.Entry(self, textvariable=self.montant_decouvert_var, font=("Arial", 12))
        self.montant_decouvert_entry.grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self, text="Création Compte", font=("Arial", 12), command=self.creer_compte).grid(row=7, column=1, padx=10, pady=10)

        self.tree = ttk.Treeview(self, columns=("Numéro", "Propriétaire", "Solde", "Type", "Taux Intérêt", "M. Découvert"), show="headings", height=10)
        self.tree.grid(row=0, column=2, rowspan=7, padx=10, pady=10, sticky="nsew")
        
        self.tree.column("Numéro", anchor="center", width=80)
        self.tree.column("Propriétaire", anchor="center", width=150)
        self.tree.column("Solde", anchor="center", width=100)
        self.tree.column("Type", anchor="center", width=80)
        self.tree.column("Taux Intérêt", anchor="center", width=120)
        self.tree.column("M. Découvert", anchor="center", width=120)

        self.tree.heading("Numéro", text="Numéro")
        self.tree.heading("Propriétaire", text="Propriétaire")
        self.tree.heading("Solde", text="Solde")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Taux Intérêt", text="Taux Intérêt")
        self.tree.heading("M. Découvert", text="M. Découvert")

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=0)


        for i in range(7):
            self.grid_rowconfigure(i, weight=0)

    def toggle_fields(self):
        if self.type_var.get() == "Courant":
            self.taux_interet_entry.config(state="disabled")
            self.montant_decouvert_entry.config(state="normal")
        else:
            self.taux_interet_entry.config(state="normal")
            self.montant_decouvert_entry.config(state="disabled")

    def creer_compte(self):
        proprietaire = self.proprietaire_var.get()
        solde = self.solde_var.get()

        if self.type_var.get() == "Courant":
            montant_decouvert = self.montant_decouvert_var.get()
            compte = CompteCourant(self.numero, proprietaire, solde, montant_decouvert)
        else:
            taux_interet = self.taux_interet_var.get()
            compte = CompteEpargne(self.numero, proprietaire, solde, taux_interet)

        self.comptes.append(compte)
        self.numero += 1
        self.rafraichir_tableau()

        self.proprietaire_var.set("")
        self.solde_var.set(0)
        self.taux_interet_var.set(0)
        self.montant_decouvert_var.set(0)

    def rafraichir_tableau(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for compte in self.comptes:
            self.tree.insert("", "end", values=compte.obtenir_informations())

if __name__ == "__main__":
    app = GestionComptesApp()
    app.mainloop()
