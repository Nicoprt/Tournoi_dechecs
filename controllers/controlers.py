from operator import attrgetter
from uuid import uuid4
from tinydb import TinyDB
import sys
#from typing import List, get_args
from models.player_model import Joueur
from models.tournoi_model import Tournoi, JOUEURS_PAR_TOURNOI
from models.tour_model import Tour
from models.match_model import Match

class MenuManager:
    pass

class UserManager:
    """interface utilisateur du tournoi pour stocker les données entrantes des joueurs"""
    def __init__(self, nb_de_joueurs=JOUEURS_PAR_TOURNOI):
        self.nb_de_joueurs = nb_de_joueurs
        self.players = []
        """
        if players:
            self.players = players
        else:
            self.create_players()
        """
        #self.players_id = []


    def demander_nom(self):
        conforme = False
        while not conforme:
            nom = input("Nom:")
            if nom != "":
                conforme = True
            else:
                print("Entrez un nom valide")
        return nom

    def demander_prenom(self):
        conforme = False
        while not conforme:
            prenom = input("Prenom:")
            if prenom != "":
                conforme = True
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
                return elo
            except: print(message)


    def get_players(self):
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            print("Joueur:", i + 1)
            nom_de_famille = self.demander_nom()
            prenom = self.demander_prenom()
            date_de_naissance = self.demander_date_de_naissance()
            sexe = self.demander_sexe()
            elo = self.demander_elo()
            j_id = int(i)
            nb_de_points = 0
            player = Joueur(nom_de_famille=nom_de_famille, prenom=prenom, date_de_naissance=date_de_naissance,
                            sexe=sexe, nb_de_points=nb_de_points, elo=elo, j_id=j_id)
            self.players.append(player)

    def get_id(self):
        nb_de_joueurs = JOUEURS_PAR_TOURNOI
        for i in range(nb_de_joueurs):
            j_id = i
            self.players_id.append(Joueur.get_id(Joueur(j_id=j_id)))
        return f"{self.players_id}"

    def afficher_joueurs(self):
        return f"{self.players}"

    def joueurs_id(self):
        liste_id = []
        for joueur in self.players:
            liste_id.append(joueur.get_id())
        return liste_id

    def get_players(self):
        return self.players

class TournamentManager:
    """interface utilisateur du tournoi pour stocker les données entrantes du tournoi"""
    def __init__(self, user_manager):
        self.tournoi_infos = []
        self.players_in_tournament = players_in_tournament
        #self.players_in_tournament_sorted = []

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
            if annee.isdigit() and 1999 < int(annee) < 3001:
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

    def afficher_tournoi(self):
        return print(f"{self.tournoi_infos} Joueurs du tournoi: {self.players_in_tournament}")

    def create_tournoi(self):
        nom = self.nom_tournoi()
        lieu = self.lieu_tournoi()
        date = self.date_du_tournoi()
        description = self.description_tournoi()
        nb_de_tours = self.nb_tours_tournoi()
        controle_du_temps = self.controle_du_temps_tournoi()
        tours = Tour
        joueurs_id = []
        for joueur in self.players_in_tournament:
            joueurs_id.append(joueur.get_id())
        tournament = Tournoi(nom=nom, lieu=lieu, date=date, description=description,
                             controle_du_temps=controle_du_temps,
                             nb_de_tours=int(nb_de_tours), tours=tours, joueurs_id=joueurs_id) # RAJOUTER "RONDES": Liste des instances rondes
        self.tournoi_infos.append(tournament)

    def sort_elo(self):
        """tri des joueurs en fonction de leur elo"""
        sorted_players = []
        sorted_elos = sorted(self.players_in_tournament, key=lambda x: x.elo, reverse=True)
        #sorted_players.append(sorted_elos)
        return sorted_elos

    def generate_pairs_tour1(self):
        players_sorted = self.sort_elo()
        diviser_liste = len(players_sorted) // 2
        first_half = self.sort_elo()[:diviser_liste]
        second_half = self.sort_elo()[diviser_liste:]
        liste_matchs = []
        for joueur in range(JOUEURS_PAR_TOURNOI // 2):
            liste_matchs.append(first_half[joueur])
            liste_matchs.append(second_half[joueur])
            print(f"{first_half[joueur]} joue contre {second_half[joueur]}")
        return liste_matchs

    # TRIER LES JOURS EN FONCTION DE LEURS POINTS
    def tri_en_fonction_des_points(self):
        pass

    """
    def start_tournoi(self):
        self.create_tournoi()
        UserManager.get_players(UserManager())
        self.sort_elo()
        self.generate_pairs_tour1()
        for i in range(int(TournamentManager().nb_tours_tournoi())):
            Tour.start_tour(Tour(), i)
            "Joue les matchs puis return results"
        pass
    """

j = UserManager(JOUEURS_PAR_TOURNOI)
j.create_players()
t = TournamentManager(j)
t.create_tournoi()
print(t.players_in_tournament)
print(t.sort_elo())
print(t.players_in_tournament)
print(t.tournoi_infos)
print()
t.generate_pairs_tour1()






