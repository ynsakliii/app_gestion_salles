import customtkinter as ctk
from tkinter import ttk, messagebox

from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")
        self.geometry("750x500")

        self.service_salle = ServiceSalle()

        self.creer_widgets()
        self.lister_salles()


def creer_widgets(self):
    # Cadre informations
    self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
    self.cadreInfo.pack(padx=10, pady=10, fill="x")

    ctk.CTkLabel(self.cadreInfo, text="Code :").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    self.entry_code = ctk.CTkEntry(self.cadreInfo)
    self.entry_code.grid(row=0, column=1, padx=10, pady=5)

    ctk.CTkLabel(self.cadreInfo, text="Description :").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    self.entry_description = ctk.CTkEntry(self.cadreInfo)
    self.entry_description.grid(row=1, column=1, padx=10, pady=5)

    ctk.CTkLabel(self.cadreInfo, text="Categorie :").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    self.entry_categorie = ctk.CTkEntry(self.cadreInfo)
    self.entry_categorie.grid(row=2, column=1, padx=10, pady=5)

    ctk.CTkLabel(self.cadreInfo, text="Capacite :").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
    self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)


