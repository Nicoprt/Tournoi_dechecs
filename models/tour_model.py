from tournoi_model import Tournoi
from match_model import Match
from typing import List
from datetime import datetime


class Tour:
    def __init__(self, nom: str = None, date: str = None, debut: datetime = None, fin: datetime = None,
                 matchs=List[Match]):
        self.nom = nom
        self.date = date
        self.debut = debut
        self.fin = fin
        self.matchs = matchs # LISTE DES MATCHS DU TOUR
        self.resultats = []

    def play(self):
        for match in self.matchs: #expected type 'collections.iterable' got 'type[list[Match]] ' instead
            match.play()
            self.resultats.append(match.get_result)

    def start_tour(self, nbdetours):
        self.nom = f"Round {nbdetours}"
        self.date = self.date  #input("Entrez la date du début du tour: ")
        self.debut = self.debut #input("Entrez l'heure du début du tour: ")
        self.fin = self.fin #input("Entrez l'heure de fin du tour: ")

    def afficher_matchs(self):
        return f"{self.matchs}"

    def afficher_tour(self):
        return f"Tour: {self.nom}, {self.date}, {self.debut}, {self.fin}, {self.matchs}"


"""
    def afficher_resultats_tour(self):
        for adversaire, resultat_joueur in zip(m.adversaires, m.resultats_joueurs):
            print(f"{adversaire}, a {resultat_joueur} point(s)")
"""
my_turn = Tour()
my_turn.play()
