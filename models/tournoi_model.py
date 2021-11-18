from typing import List
from uuid import uuid4
from tinydb import TinyDB
from player_model import Joueur

JOUEURS_PAR_TOURNOI = 4
db = TinyDB("db.json")


class Tournoi:
    def __init__(self, nom=None, lieu=None, date=None
                 , description=None, nb_de_tours: int = 4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.description = description
        self.nb_de_tours = nb_de_tours

    def creer_tournoi(self):
        self.nom = input("Entrez le nom du tournoi: ")
        self.lieu = input("Entrez le lieu du tournoi: ")
        self.date = input("Entrez la date du tournoi: ")
        self.description = input("Entrez la description du tournoi: ")
        self.nb_de_tours = input("Entrez le nombre de tours du tournoi: ")

    def ajouter_controle_du_temps(self):
        self.time = input("Choisir le contrôle du temps : écrire: 1 pour bullet , 2 pour blitz, 3 pour coup rapide ")
        erreur = "Vous devez choisir un nombre entre 1 , 2 ou 3"
        if self.time == "1":
            self.time = "Bullet"
        elif self.time == "2":
            self.time = "Blitz"
        elif self.time == "3":
            self.time = "Coup rapide"

        else: print(erreur)

    def tri_joueurs(self):
        pass

    def generate_pairs(self):
        length = len(self.joueurs)
        diviser_liste = length // 2
        first_half = self.joueurs[:diviser_liste]
        second_half = self.joueurs[diviser_liste:]
        liste_matchs = []
        for i in range(JOUEURS_PAR_TOURNOI // 2):
            #print(f"{(Joueur.__str__(first_half[i]))} joue contre {(Joueur.__str__(second_half[i]))}")
            liste_matchs.append((Joueur.__str__(first_half[i])))
            liste_matchs.append((Joueur.__str__(second_half[i])))
        return liste_matchs

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
