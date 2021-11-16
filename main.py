from typing import List
from uuid import uuid4
from tinydb import TinyDB

JOUEURS_PAR_TOURNOI = 8

class Joueur:

    def __init__(self, nom_de_famille=None, prenom=None, date_de_naissance=None, sexe=None,
                 nb_de_points=0, ranking=None):

        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.nb_de_points = nb_de_points
        self.ranking = ranking
        self.id = uuid4()


    def changer_classement(self, ajustement_points: float):
        self.nb_de_points += ajustement_points

    def __repr__(self):
        return f" {self.id}"

    def __str__(self):
        return f" {self.nom_de_famille}, {self.prenom}"

    def afficher_joueur(self):
        return f"Joueur: {self.nom_de_famille}, {self.prenom}, {self.date_de_naissance}, {self.sexe}, {self.ranking}, {self.nb_de_points}"

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

    def generate_pairs(self):
        length = len(self.joueurs)
        diviser_liste = length // 2
        first_half = self.joueurs[:diviser_liste]
        second_half = self.joueurs[diviser_liste:]
        liste_paires1 = []
        liste_paires2 = []
        liste_paires3 = []
        liste_paires4 = []
        for i in range(JOUEURS_PAR_TOURNOI // 2):
            print(f"{(Joueur.__str__(first_half[i]))} joue contre {(Joueur.__str__(second_half[i]))}")

            if len(liste_paires1) <= 1:
                liste_paires1.append((Joueur.__str__(first_half[i])))
                liste_paires1.append((Joueur.__str__(second_half[i])))

            elif len(liste_paires2) <= 1:
                liste_paires2.append((Joueur.__str__(first_half[i])))
                liste_paires2.append((Joueur.__str__(second_half[i])))

            elif len(liste_paires3) <= 1:
                liste_paires3.append((Joueur.__str__(first_half[i])))
                liste_paires3.append((Joueur.__str__(second_half[i])))
            else:
                liste_paires4.append((Joueur.__str__(first_half[i])))
                liste_paires4.append((Joueur.__str__(second_half[i])))

        print(liste_paires1)
        print(liste_paires2)
        print(liste_paires3)
        print(liste_paires4)






    def enter_results(self):
        pass

    def afficher_tournoi(self):
        return print(f"Tournoi: {self.nom}, {self.lieu}, {self.date}, {self.description}, {self.time}, {self.nb_de_tours}")

    def afficher_liste_joueurs(self):
        return print(f" Liste des joueurs :{self.joueurs}")

    def creer_les_joueurs(self):
        self.joueurs = []
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur: ", i + 1)
            joueur = Joueur(nom_de_famille=input("nom_de_famille: "),
                            prenom=input("prenom: "),
                            date_de_naissance=input("date_de_naissance: "),
                            sexe=input("sexe: "))
            self.joueurs.append(joueur)

    def get_joueurs_id(self):
       return [j.id for j in self.joueurs]

t = Tournoi()
t.creer_tournoi()
#print(t.__dict__)
t.creer_les_joueurs()
t.ajouter_controle_du_temps()
#Joueurs = t.get_joueurs_id()
t.afficher_tournoi()
t.afficher_liste_joueurs()
t.generate_pairs()
#print(Joueur.__str__(t.joueurs[1]))


class Match:

    def __init__(self, adversaires: list):
        self.adversaires = adversaires
        self.resultats_joueurs = []

    def ajouter_des_points(self):
        add1 = int((input("Entez le nombre de points du Joueur1 ")))
        add2 = int((input("Entez le nombre de points du Joueur2 ")))
        message = f"Erreur le nombre de points doit être un 0, 0.5 ou 1"
        try:
            if add1 == 0 or add1 == 1 or add1 == 0.5:
                self.resultats_joueurs.append(add1)
            else: raise ValueError(message)

            if add2 == 0 or add2 == 1 or add2 == 0.5:
                self.resultats_joueurs.append(add2)
            else :raise ValueError(message)

        except: print(message)


    def definir_le_gagant(self):
        self.gagnant = 0
        if self.resultj1 > self.resultj2:
            self.gagnant = 1
            return f": {self.j1} a gagné"

        elif self.resultj2 > self.resultj1:
            self.gagnant = 2
            return f": {self.j2} a gagné"

        elif self.resultj1 == self.resultj2:
            return f": Draw"

    def jouer_le_match(self):
        return print(f"{self.adversaires[0]} joue contre {self.adversaires[1]}")

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
"""
m = Match(t.joueurs)
m.jouer_le_match()
m.ajouter_des_points()
m.afficher_result()
#print(match1.afficher_result())
#match1 = Match(tournoi1.players[0], tournoi1.players[1])
#match1.resultj1 = input("Entrez le score pour le joueur1:")
#match1.resultj2 = input("Entrez le score pour le joueur2:")
#match1.attribuer_points(1,0)
#print(match1.resultj2)
#print(match1.afficher_result())
"""
class Tour:
    def __init__(self, nom, date, heure_de_debut, heure_de_fin):
        self.nom = nom
        self.date = date
        self.heure_de_debut = heure_de_debut
        self.heure_de_fin = heure_de_fin

    def afficher_tour(self):
        return f"Joueur: {self.nom}, {self.date}, {self.heure_de_debut}, {self.heure_de_fin}"



