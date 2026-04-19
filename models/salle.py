class Salle:
    def __init__(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite
 def afficher_infos(self):
        return (
            f"Code: {self.code}",
            f"Description: {self.description}",
            f"Categorie: {self.categorie}",
            f"Capacite: {self.capacite}",
        )
