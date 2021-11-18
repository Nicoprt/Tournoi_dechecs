from uuid import uuid4
from tinydb import TinyDB
import sys
from typing import List

import player_model
from models.player_model import Joueur, JOUEURS_PAR_TOURNOI
from models.tournoi_model import Tournoi
from view.view import *
#from models.player_model import *
#from models.match_model import *
#from sys import modules


class Controller:

    def __init__(self):
        self.players = []
        self.tournoi = Tournoi()

    def demander_nom(self):
        conforme = False
        while not conforme:
            nom = input("Nom:")
            if nom != "":
                conforme = True
                #self.players.append(nom)
            else:
                print("Entrez un nom valide")
        return nom
    def demander_prenom(self):
        conforme = False
        while not conforme:
            prenom = input("Prenom:")
            if prenom != "":
                conforme = True
                #self.players.append(prenom)
            else:
                print("Entrez un prenom valide")
        return prenom
    def demander_date_de_naissance(self):
        jour_conforme = False
        mois_conforme = False
        annee_conforme = False
        date_de_naissance = []
        while not jour_conforme:
            jour = input("Jour de naissance:")
            if jour.isdigit() and 0 < int(jour) < 32:
                jour_conforme = True
                date_de_naissance.append(jour)
            else:
                print("Entrez un jour valide")
        
        while not mois_conforme:
            mois = input("Mois de naissance:")
            if mois.isdigit() and 0 < int(mois) < 13:
                mois_conforme = True
                date_de_naissance.append(mois)
            else:
                print("Entrez un mois valide")
        
        while not annee_conforme:
            annee = input("Annee de naissance:")
            if annee.isdigit() and 1900 < int(annee) < 2023:
                annee_conforme = True
                date_de_naissance.append(annee)
            else:
                print("Entrez une année valide")

        return f"{date_de_naissance[0]}/{date_de_naissance[1]}/{date_de_naissance[2]}"

    def demander_sexe(self):
        conforme = False
        while not conforme:
            sexe = input("Sexe:")
            if sexe != "":
                conforme = True
                #self.players.append(sexe)
            else:
                print("Entrez un genre valide")
        return sexe
    def demander_elo(self):
        conforme = False
        while not conforme:
            elo = input("Elo:")
            if elo.isdigit() and int(elo) >= 0:
                conforme = True
                #self.players.append(elo)
            else:
                print("Entrez Elo valide")
        return elo


    def get_players(self):
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur:", i + 1)
            nom_de_famille = self.view.demander_nom_de_famille(),
            prenom = self.view.demander_prenom(),
            date_de_naissance = self.view.demander_date_de_naissance(),
            sexe = self.view.demander_sexe()
            elo = self.view.demander_elo()
            player = Joueur(nom_de_famille, prenom, date_de_naissance, sexe, elo)
            self.players.append(player)



controller = Controller()
controller.demander_nom()
controller.demander_prenom()
controller.demander_date_de_naissance()
controller.demander_sexe()
controller.demander_elo()
print(controller.players)

