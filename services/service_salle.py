from data.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs sont obligatoires"

        if int(salle.capacite) < 1:
            return False, "La capacite doit etre superieure ou egale a 1"

        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutee avec succes"

