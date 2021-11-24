from operator import attrgetter
from uuid import uuid4
from tinydb import TinyDB
import sys
from typing import List
from models.player_model import Joueur, JOUEURS_PAR_TOURNOI
from models.tournoi_model import Tournoi

class MenuManager:
    pass

class UserManager:

    def __init__(self):
        self.players = []
        self.players_id = []

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
        message = "Entrez Elo valide"
        while not conforme:
            try:
                elo = int(input("Elo:"))
                if elo >= 0:
                    conforme = True
            except: print(message)
        return elo

    def get_players(self):
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur:", i + 1)
            nom_de_famille = self.demander_nom()
            prenom = self.demander_prenom()
            date_de_naissance = self.demander_date_de_naissance()
            sexe = self.demander_sexe()
            elo = self.demander_elo()
            j_id = str(i)
            nb_de_points = 0
            player = Joueur(nom_de_famille, prenom, date_de_naissance, sexe, elo, j_id, nb_de_points)
            self.players.append(player)

    def get_id(self):
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            j_id = i
            self.players_id.append(Joueur.getid(Joueur(j_id=j_id)))
        return f"{self.players_id}"

    def __repr__(self):
        return f"{self.players}"
    #TRIER LES JOURS EN FONCTION DE LEUR ELO
    def get_elo(self):
        #sorted_elos = sorted(self.players, key=attrgetter("elo"))
        sorted_elos = sorted(self.players, key=lambda x: x.elo)
        #sorted_elos = sorted(self.players, key=lambda x: getattr(x, "elo"))
        #sorted_elos = sorted(self.players, key=lambda x: x[5])
        #return self.players.sort(key=lambda x: x.elo)
        return sorted_elos

    def sort_tour_1(self):
        #sort1 = list.sort(self.players, key=lambda: )
        pass

class TournamentManager:

    def __init__(self):
        self.tournoi_infos = []

    def nom_tournoi(self):
        conforme = False
        while not conforme:
            nom = input("Nom du tournoi:")
            if nom != "":
                conforme = True
            else:
                print("Entrez un nom de tournoi")
        return nom

    def lieu_tournoi(self):
        conforme = False
        while not conforme:
            lieu = input("Lieu du tournoi:")
            if lieu != "":
                conforme = True
            else:
                print("Entrez un lieu de tournoi")
        return lieu

    def date_du_tournoi(self):
        jour_conforme = False
        mois_conforme = False
        annee_conforme = False
        date_du_tournoi = []
        while not jour_conforme:
            jour = input("Jour du tournoi:")
            if jour.isdigit() and 0 < int(jour) < 32:
                jour_conforme = True
                date_du_tournoi.append(jour)
            else:
                print("Entrez un jour valide")

        while not mois_conforme:
            mois = input("Mois du tournoi:")
            if mois.isdigit() and 0 < int(mois) < 13:
                mois_conforme = True
                date_du_tournoi.append(mois)
            else:
                print("Entrez un mois valide")

        while not annee_conforme:
            annee = input("Annee du tournoi:")
            if annee.isdigit() and 2000 < int(annee) < 3000:
                annee_conforme = True
                date_du_tournoi.append(annee)
            else:
                print("Entrez une année valide")

        return f"{date_du_tournoi[0]}/{date_du_tournoi[1]}/{date_du_tournoi[2]}"

    def description_tournoi(self):
        conforme = False
        while not conforme:
            description = input("Description du tournoi:")
            if description != "":
                conforme = True
            else:
                print("Entrez une description du tournoi")
        return description

    def nb_tours_tournoi(self):
        conforme = False
        while not conforme:
            nb_tours = input("nombre de tours du tournoi:")
            if nb_tours.isdigit() and 1 <= int(nb_tours) <= 4:
                conforme = True
            else:
                print("Entrez un nombre de tours valide")
        return nb_tours

    def controle_du_temps_tournoi(self):
        conforme = False
        while not conforme:
            control = input("Choisir le contrôle du temps : écrire: 1 pour bullet , 2 pour blitz, 3 pour coup rapide: ")
            if control == "1":
                control = "Bullet"
                conforme=True
            elif control == "2":
                control = "Blitz"
                conforme = True
            elif control == "3":
                control = "Coup rapide"
                conforme = True
            else:
                print("Entrez 1, 2 ou 3 pour le contrôle du temps du tournoi")
        return control

    def __repr__(self):
        return f"{self.tournoi_infos}"

    def get_tournoi(self):
        nom = self.nom_tournoi()
        lieu = self.lieu_tournoi()
        date = self.date_du_tournoi()
        description = self.description_tournoi()
        nb_de_tours = self.nb_tours_tournoi()
        controle_du_temps = self.controle_du_temps_tournoi()
        joueurs_id = UserManager.get_id(UserManager())
        tournament = Tournoi(nom, lieu, date, description, controle_du_temps, int(nb_de_tours), joueurs_id)
        self.tournoi_infos.append(tournament)

    def generate_pairs(self):
        length = len(UserManager.get_elo(UserManager))
        diviser_liste = length // 2
        first_half = self.tournament[:diviser_liste]
        second_half = self.tournament[diviser_liste:]
        liste_matchs = []
        for i in range(JOUEURS_PAR_TOURNOI // 2):
            # print(f"{(Joueur.__str__(first_half[i]))} joue contre {(Joueur.__str__(second_half[i]))}")
            liste_matchs.append((Joueur.getid(first_half[i])))
            liste_matchs.append((Joueur.getid(second_half[i])))
        return liste_matchs


class RunTournament:

    def __init__(self, tournament):
        self.tournament = tournament


j = UserManager()
j.get_players()
print("-----")
print(j)
print(Joueur())
j.get_elo()
print(j)




"""
t = TournamentManager()
t.get_tournoi()
print(t.tournoi_infos)
t.generate_pairs()
print(t.generate_pairs())
"""


