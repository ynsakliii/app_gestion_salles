from models.salle import Salle
from services.service_salle import ServiceSalle

service = ServiceSalle()

s1 = Salle("B201", "Salle de reunion", "Bureau", 15)

succes, message = service.ajouter_salle(s1)
print(message)

salles = service.recuperer_salles()
for salle in salles:
    print(salle.afficher_infos())

s1.description = "Salle de reunion principale"
succes, message = service.modifier_salle(s1)
print(message)

salle = service.rechercher_salle("B201")
if salle:
    print("Recherche :", salle.afficher_infos())

service.supprimer_salle("B201")
print("Salle supprimee")