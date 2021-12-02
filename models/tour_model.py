from tournoi_model import Tournoi
from match_model import Match
from typing import List

class Tour:
    def __init__(self, nom=None, date=None, heure_de_debut=None, heure_de_fin=None, matchs=List):
        self.nom = nom
        self.date = date
        self.heure_de_debut = heure_de_debut
        self.heure_de_fin = heure_de_fin
        self.matchs = matchs #LISTE DES MATCHS DU TOUR

    def start_tour(self, nbdetours):
        self.nom = f"Round {nbdetours}"
        self.date = input("Entrez la date du début du tour: ")
        self.heure_de_debut = input("Entrez l'heure du début du tour: ")
        self.heure_de_fin = input("Entrez l'heure de fin du tour: ")


    def afficher_matchs(self):
        return f"{self.matchs}"

    def afficher_tour(self):
        return f"Tour: {self.nom}, {self.date}, {self.heure_de_debut}, {self.heure_de_fin}, {self.matchs}"
"""
    def afficher_resultats_tour(self):
        for adversaire, resultat_joueur in zip(m.adversaires, m.resultats_joueurs):
            print(f"{adversaire}, a {resultat_joueur} point(s)")
"""
tour = Tour()