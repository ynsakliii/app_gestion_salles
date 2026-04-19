from models.salle import Salle
from data.dao_salle import DataSalle

dao = DataSalle()

# Test connexion
try:
    conn = dao.get_connection()
    print("Connexion MySQL reussie")
    conn.close()
except Exception as e:
    print("Erreur connexion :", e)

# Ajouter une salle
s1 = Salle("A101", "Salle informatique", "Laboratoire", 25)
dao.insert_salle(s1)
print("Salle ajoutee")

# Modifier la salle
s1.description = "Salle informatique principale"
s1.capacite = 30
dao.update_salle(s1)
print("Salle modifiee")

# Rechercher une salle
salle_trouvee = dao.get_salle("A101")
if salle_trouvee:
    print("Salle trouvee :", salle_trouvee.afficher_infos())

# Afficher toutes les salles
print("Liste des salles :")
for salle in dao.get_salles():
    print(salle.afficher_infos())

# Supprimer une salle
dao.delete_salle("A101")
print("Salle supprimee")