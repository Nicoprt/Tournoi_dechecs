from tournoi_model import Tournoi
from match_model import Match
from typing import List, get_args
from models.tournoi_model import Tournoi
from datetime import datetime


class Tour:
    def __init__(self, nom: str = None, debut: datetime = None, fin: datetime = None,
                 matchs=list[Match]):
        self.nom = nom
        self.debut = debut
        self.fin = fin
        self.matchs = matchs # LISTE DES MATCHS DU TOUR
        self.resultats = []

    def get_matchs(self):
            pass

    def play_tour(self):
        for match in get_args(self.matchs):
            match.play()
            self.resultats.append(match.get_result)

    def start_tour(self, nbdetours):
        self.nom = f"Round {nbdetours}"
        self.debut = datetime.now() #input("Entrez l'heure du début du tour: ")
        self.fin = datetime.now() #input("Entrez l'heure de fin du tour: ")

    def afficher_matchs(self):
        return f"{self.matchs}"

    def __repr__(self):
        return f"Tour: {self.nom}, {self.debut}, {self.fin}, {self.matchs}"


"""
    def afficher_resultats_tour(self):
        for adversaire, resultat_joueur in zip(m.adversaires, m.resultats_joueurs):
            print(f"{adversaire}, a {resultat_joueur} point(s)")

my_turn = Tour()
my_turn.play_tour()
print(type(List[Match]))
"""