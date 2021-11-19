from typing import List
from uuid import uuid4
from tinydb import TinyDB
from player_model import Joueur

JOUEURS_PAR_TOURNOI = 4
db = TinyDB("db.json")


class Tournoi:
    def __init__(self, nom=None, lieu=None, date=None
                 , description=None, controle_du_temps=None, nb_de_tours: int = 4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.description = description
        self.nb_de_tours = nb_de_tours
        self.controle_du_temps = controle_du_temps

    def tri_joueurs(self):
        pass

    def enter_results(self):
        pass

    def afficher_tournoi(self):
        return print(f"Tournoi: {self.nom}, {self.lieu}, {self.date}, {self.description}, {self.time}, {self.nb_de_tours}")

    def afficher_liste_joueurs(self):
        return print(f" Liste des joueurs(id) :{self.joueurs}")

    def get_joueurs_id(self):
       return [j.id for j in self.joueurs]

    def get_joueurs_infos(self):
        return [vars(k) for k in self.joueurs]

t = Tournoi()
#t.creer_tournoi()
#t.creer_les_joueurs()
#t.ajouter_controle_du_temps()
#Joueurs = t.get_joueurs_id()
#t.afficher_tournoi()
#t.afficher_liste_joueurs()
#print(t.generate_pairs())
#print(Joueur.__str__(t.joueurs[1]))
#x = t.get_joueurs_infos().__dict__
#table_joueurs = db.table("joueurs")
#table_joueurs.truncate()
#table_joueurs.insert(x)
