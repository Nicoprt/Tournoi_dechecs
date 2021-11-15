from typing import List
from uuid import uuid4
from tinydb import TinyDB

JOUEURS_PAR_TOURNOI = 2
#testt
class Joueur:

    def __init__(self, nom_de_famille=None, prenom=None, date_de_naissance=None, sexe=None,
                 classement=0):

        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        self.id = uuid4()


    def changer_classement(self, ajustement_points: float):
        self.classement += ajustement_points

    def __repr__(self):
        return f" {self.id}"

    def afficher_joueur(self):
        return f"Joueur: {self.nom_de_famille}, {self.prenom}, {self.date_de_naissance}, {self.sexe}, {self.classement}"


#joueur1 = Joueur("Parent", "Nicolas", "18/08/92", "Homme")
#joueur2 = Joueur("zzzz", "zzzz", "zzzz", "zzz")

class Tournoi:
    def __init__(self, nom: str, lieu: str, date: str,
                 description: str, nb_de_tours: int = 4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        #self.players = players
        self.description = description
        self.nb_de_tours = nb_de_tours
        #  self.tournees = tournees

    def creer_tournoi(self):
        pass

    def generate_pairs(self):
        pass

    def enter_results(self):
        pass

    def afficher_tournoi(self):
        return f"Tournoi: {self.nom}, {self.lieu}, {self.date}, {self.players}, {self.description}, {self.nb_de_tours}"

    def creer_les_joueurs(self):
        self.joueurs = []
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur :", i + 1)
            nom_de_famille = input("nom_de_famille:")
            prenom = input("prenom:")
            date_de_naissance = input("date_de_naissance:")
            sexe = input("sexe:")
            joueur = Joueur(nom_de_famille, prenom, date_de_naissance, sexe)
            self.joueurs.append(joueur)

    def get_joueurs_id(self):
        return [j.id for j in self.joueurs]

        """
        for j in range(JOUEURS_PAR_TOURNOI):
            print(joueurs[j].generate_dict())
        """

tournoi1 = Tournoi("Tournoi1", "Paris", "01/01/01", "Tournoi de Paris")
#Joueurs = tournoi1.get_joueurs_id()
#print(tournoi1.afficher_tournoi())
#tournoi1.ajouter_des_joueurs()


if __name__ == "__main__":
    t = Tournoi("Tournoi1", "Paris", "01/01/01", "Tournoi de Paris")
    t.creer_les_joueurs()
    Joueurs = tournoi1.get_joueurs_id()


