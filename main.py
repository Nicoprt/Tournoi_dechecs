from typing import List
from uuid import uuid4
from tinydb import TinyDB
import numpy as np

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

    def creer_les_joueurs(self):
        self.joueurs = []
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur: ", i + 1)
            joueur = Joueur(nom_de_famille=input("Nom_de_famille: "),
                            prenom=input("Prenom: "),
                            date_de_naissance=input("Date_de_naissance: "),
                            sexe=input("Sexe: "),
                            elo=input("Elo: "))
            self.joueurs.append(joueur)

    def get_joueurs_id(self):
       return [j.id for j in self.joueurs]

    def get_joueurs_infos(self):
        return [vars(k) for k in self.joueurs]

t = Tournoi()
t.creer_tournoi()
t.creer_les_joueurs()
t.ajouter_controle_du_temps()
#Joueurs = t.get_joueurs_id()
t.afficher_tournoi()
#t.afficher_liste_joueurs()
#print(t.generate_pairs())
#print(Joueur.__str__(t.joueurs[1]))
#x = t.get_joueurs_infos().__dict__
#table_joueurs = db.table("joueurs")
#table_joueurs.truncate()
#table_joueurs.insert(x)

class Tour:
    def __init__(self, nom=None, date=None, heure_de_debut=None, heure_de_fin=None):
        self.nom = nom
        self.date = date
        self.heure_de_debut = heure_de_debut
        self.heure_de_fin = heure_de_fin
        self.matchs = t.generate_pairs()

    def creer_tour(self):
        self.nom = "Round 1"
        self.date = input("Entrez la date du début du tour: ")
        self.heure_de_debut = input("Entrez l'heure du début du tour: ")
        self.heure_de_fin = input("Entrez l'heure de fin du tour: ")

    def start_tour(self):
        print(self.creer_tour())
        print(self.matchs)
        pass

    def afficher_matchs(self):
        return f"{self.matchs}"

    def afficher_tour(self):
        return f"Tour: {self.nom}, {self.date}, {self.heure_de_debut}, {self.heure_de_fin}, {self.matchs}"

    def afficher_resultats_tour(self):
        for adversaire, resultat_joueur in zip(m.adversaires, m.resultats_joueurs):
            print(f"{adversaire}, a {resultat_joueur} point(s)")

tour = Tour()

class Match:

    def __init__(self):
        self.adversaires = [] #np.array_split(tour.matchs, 1)
        self.resultats_joueurs = []

    def ajouter_des_points(self):
        result1 = int((input("Entez le nombre de points du Joueur1 ")))
        result2 = int((input("Entez le nombre de points du Joueur2 ")))
        message = f"Erreur le nombre de points doit être un 0, 0.5 ou 1"
        try:
            if result1 == 0 or result1 == 1 or result1 == 0.5:
                self.resultats_joueurs.append(result1)
            else: raise ValueError(message)

            if result2 == 0 or result2 == 1 or result2 == 0.5:
                self.resultats_joueurs.append(result2)
            else :raise ValueError(message)

        except: print(message)


    def definir_le_gagnant(self):
        self.gagnant = 0
        if self.resultj1 > self.resultj2:
            self.gagnant = 1
            return f": {self.j1} a gagné"

        elif self.resultj2 > self.resultj1:
            self.gagnant = 2
            return f": {self.j2} a gagné"

        elif self.resultj1 == self.resultj2:
            return f": Draw"

    def split_liste(self):
        pass

    def jouer_les_match(self):
        self.adversaires = tour.matchs
        i = 0
        print(self.adversaires)
        while i <= (len(self.adversaires) // 2):
            print(f"{self.adversaires[i]} joue contre {self.adversaires[i + 1]}")
            result1 = input(f"Entez le nombre de points de {self.adversaires[i]} ")
            result2 = input(f"Entez le nombre de points de {self.adversaires[i + 1]} ")
            message = f"Erreur le nombre de points doit être un 0, 0.5 ou 1"
            try:
                if result1 == "0" or result1 == "1" or result1 == "0.5":
                    self.resultats_joueurs.append(result1)
                else:
                    raise ValueError(message)
                if result2 == "0" or result2 == "1" or result2 == "0.5":
                    self.resultats_joueurs.append(result2)
                else:
                    raise ValueError(message)
            except:
                print(message)
            i += 2

    def afficher_result(self):
        return print(f"Résultat du match: \n{self.adversaires[0]} : {self.resultats_joueurs[0]}, {self.adversaires[1]} : {self.resultats_joueurs[1]}")

    def attribuer_points(self, resultat1=0, resultat2=0):
        self.resultat1 = resultat1
        self.resultat2 = resultat2

        self.resultat1 = input("Entrez le score pour le joueur1:")
        self.resultat2 = input("Entrez le score pour le joueur2:")

        if self.resultat1 > self.resultat2:
            self.resultj1 += resultat1

        elif self.resultat2 > self.resultat1:
            self.resultj2 += resultat2

        elif self.resultat1 == self.resultat2:
            self.resultj1 += resultat1
            self.resultj2 += resultat2

m = Match()
m.jouer_les_match()
tour.afficher_resultats_tour()
#print(m.adversaires)
#print(m.__dict__)
#m.ajouter_des_points()
#m.afficher_result()

"""
for x in m.adversaires:
    print(list(x))
"""

