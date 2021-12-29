from typing import List
from uuid import uuid4
from tinydb import TinyDB
from player_model import Joueur

JOUEURS_PAR_TOURNOI = 4
db = TinyDB("db.json")


class Tournoi:
    def __init__(self, nom=None, lieu=None, date=None
                 , description=None, controle_du_temps=None, nb_de_tours: int = 4, tours=list, joueurs_id=list):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.description = description
        self.nb_de_tours = nb_de_tours
        self.controle_du_temps = controle_du_temps
        self.tours = tours
        self.joueurs_id = joueurs_id
        #self.joueurs = joueurs

    def tournoi_id(self):
        return f"{self.joueurs_id}"

    def __str__(self):
        return f"Tournoi: {self.nom}, {self.lieu}, {self.date}, {self.description}, {self.controle_du_temps}," \
               f"{self.nb_de_tours}," + '\n'.join(map(str, self.tours))+ f", {self.joueurs_id}"

    def afficher_liste_joueurs(self):
        return print(f" Liste des joueurs(id) :{self.joueurs_id}")



