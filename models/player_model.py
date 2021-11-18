from uuid import uuid4
from tinydb import TinyDB

JOUEURS_PAR_TOURNOI = 4
db = TinyDB("db.json")

class Joueur:

    def __init__(self, nom_de_famille=None, prenom=None, date_de_naissance=None, sexe=None,
                 nb_de_points=0, elo=None):

        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.nb_de_points = nb_de_points
        self.elo = elo
        self.id = uuid4()

    def changer_classement(self, ajustement_points: float):
        self.nb_de_points += ajustement_points

    def __repr__(self):
        return f" {self.id}"

    def __str__(self):
        return f" {self.nom_de_famille}, {self.prenom}"

    def afficher_joueur(self):
        return f"Joueur: {self.nom_de_famille}, {self.prenom}, {self.date_de_naissance}, {self.sexe}, {self.elo}, {self.nb_de_points}"

    def serialize(self):
        serialized_joueur = {
            "nom_de_famille": self.nom_de_famille,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "nb_de_points": self.nb_de_points,
            "elo": self.elo,
            "id" : str(self.id)
        }
        return serialized_joueur

#j1 = Joueur("Parent", "Nicolas", "18/08/92", "Homme")
#j2 = Joueur("Parent", "Nicolas", "18/08/92", "Homme")
