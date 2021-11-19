from uuid import uuid4
from tinydb import TinyDB, Query

JOUEURS_PAR_TOURNOI = 4
db = TinyDB("joueurs.json")

class Joueur:

    def __init__(self, nom_de_famille=None, prenom=None, date_de_naissance=None, sexe=None,
                 nb_de_points=0, elo=None):

        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.nb_de_points = nb_de_points
        self.elo = elo
        self.j_id = uuid4()

    def changer_classement(self, ajustement_points: float):
        self.nb_de_points += ajustement_points

    def __str__(self):
        return f" {self.nom_de_famille}, {self.prenom}"

    def afficher_joueur(self):
        return f"Joueur: {self.nom_de_famille}, {self.prenom}, {self.date_de_naissance}, {self.sexe}, {self.elo}," \
               f"{self.nb_de_points}"

    def serialize(self):
        serialized_joueur = {
            "nom_de_famille": self.nom_de_famille,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "nb_de_points": self.nb_de_points,
            "elo": self.elo,
            "j_id": str(self.j_id)
        }
        return serialized_joueur

"""
    def unserialize(self, serialized_joueur):
        nom_de_famille = serialized_joueur["nom_de_famille"]
        prenom = serialized_joueur["prenom"]
        date_de_naissance = serialized_joueur["date_de_naissance"]
        sexe = serialized_joueur["sexe"]
        nb_de_points = serialized_joueur["nb_de_points"]
        elo = serialized_joueur["elo"]
        j_id = serialized_joueur["j_id"]
        x = Joueur(nom_de_famille=nom_de_famille, prenom=prenom, date_de_naissance=date_de_naissance,
                   sexe=sexe, nb_de_points=nb_de_points,
                   elo=elo)
        return x

j1 = Joueur("Parent", "Nicolas", "18/08/92", "Homme")
j1.serialize()
players_table = db.table("joueurs")
players_table.truncate()	# clear the table first
players_table.insert(j1.serialize())
"""
#players_table.all()


