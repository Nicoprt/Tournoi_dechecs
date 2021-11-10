from typing import List
from uuid import uuid4

JOUEURS_PAR_TOURNOI = 2

class Joueur:

    def __init__(self, nom_de_famille=None, prenom=None, date_de_naissance=None, sexe=None,
                 classement=0):

        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement
        self.id = uuid4()

    def liste_id(self):
        liste_joueurs_id = []
        liste_joueurs_id.append(self.id)
        return liste_joueurs_id

    def changer_classement(self, ajustement_points: float):
        self.ajustement_points = ajustement_points
        self.classement += self.ajustement_points
        return abs(self.classement)

    def __repr__(self):
        return f" {self.id}"

    def afficher_joueur(self):
        return f"Joueur: {self.nom_de_famille}, {self.prenom}, {self.date_de_naissance}, {self.sexe}, {self.classement}"

    def generate_dict(self):
        dict_de_joueurs = self.__dict__
        return dict_de_joueurs


liste_joueurs_id = []
for i in range(JOUEURS_PAR_TOURNOI):
    joueur = Joueur()
    liste_joueurs_id.append(joueur)

#joueur1 = Joueur("Parent", "Nicolas", "18/08/92", "Homme")
#joueur2 = Joueur("zzzz", "zzzz", "zzzz", "zzz")

class Tournoi:
    def __init__(self, nom: str, lieu: str, date: str, players,
                 description: str, nb_de_tours: int = 4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.players = players
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

    def ajouter_des_joueurs(self):
        joueurs = []
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur :", i + 1)
            nom_de_famille = input("nom_de_famille:")
            prenom = input("prenom:")
            date_de_naissance = input("date_de_naissance:")
            sexe = input("sexe:")
            joueurs.append(Joueur(nom_de_famille, prenom, date_de_naissance, sexe))
        """
        for j in range(JOUEURS_PAR_TOURNOI):
            print(joueurs[j].generate_dict())
        """

tournoi1 = Tournoi("Tournoi1", "Paris", "01/01/01", liste_joueurs_id, "Tournoi de Paris")
#print(tournoi1.afficher_tournoi())
#tournoi1.ajouter_des_joueurs()


class Match:

    def __init__(self, adversaires: list, resultats_joueurs: list):
        self.adversaires = adversaires
        self.resultats_joueurs = resultats_joueurs
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
        return f"{self.adversaires[0]} va jouer contre {self.adversaires[1]}"

    def afficher_result(self):
        return f"Résultat du match: \n{self.adversaires[0]} :{self.resultats_joueurs[0]}, {self.adversaires[1]} :{self.resultats_joueurs[1]}"

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

match1 = Match(liste_joueurs_id, [])
print(match1.resultats_joueurs)
print(match1.afficher_result())
#match1 = Match(tournoi1.players[0], tournoi1.players[1])
#match1.resultj1 = input("Entrez le score pour le joueur1:")
#match1.resultj2 = input("Entrez le score pour le joueur2:")
#match1.attribuer_points(1,0)
#print(match1.resultj2)
#print(match1.afficher_result())

class Tournees:
    def __init__(self):
        self.tournees = []


class Tour:
    def __init__(self, nom, date, heure_de_debut, heure_de_fin):
        self.nom = nom
        self.date = date
        self.heure_de_debut = heure_de_debut
        self.heure_de_fin = heure_de_fin

    def afficher_tour(self):
        return f"Joueur: {self.nom}, {self.date}, {self.heure_de_debut}, {self.heure_de_fin}"





