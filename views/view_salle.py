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

    # Cadre actions
    self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
    self.cadreActions.pack(padx=10, pady=10, fill="x")

    self.btn_ajouter = ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle)
    self.btn_ajouter.pack(side="left", padx=10, pady=10)

    self.btn_modifier = ctk.CTkButton(self.cadreActions, text="Modifier", command=self.modifier_salle)
    self.btn_modifier.pack(side="left", padx=10, pady=10)

    self.btn_supprimer = ctk.CTkButton(self.cadreActions, text="Supprimer", command=self.supprimer_salle)
    self.btn_supprimer.pack(side="left", padx=10, pady=10)

    self.btn_rechercher = ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle)
    self.btn_rechercher.pack(side="left", padx=10, pady=10)

# Cadre Liste des salles
self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
self.cadreList.pack(padx=10, pady=10)

self.treeList = ttk.Treeview(
    self.cadreList,
    columns=("code", "description", "categorie", "capacite"),
    show="headings"
)

self.treeList.heading("code", text="CODE")
self.treeList.heading("description", text="Description")
self.treeList.heading("categorie", text="Catégorie")
self.treeList.heading("capacite", text="Capacité")

self.treeList.column("code", width=50)
self.treeList.column("description", width=150)
self.treeList.column("categorie", width=100)
self.treeList.column("capacite", width=100)

self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

self.lister_salles()
