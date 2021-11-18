

class View:

    def demander_nom_de_famille(self):
        nom_conforme = False
        while not nom_conforme:
            nom_de_famille = input("Nom_de_famille: "),
            if nom_de_famille != "":
                nom_conforme = True
            else:
                print("Entrez un nom valide")
        return nom_de_famille

    def demander_prenom(self):
        prenom = input("Prenom: ")
        if not prenom:
            return None
        return prenom

    def demander_date_de_naissance(self):
        date_de_naissance = input("Date_de_naissance: "),
        if not date_de_naissance:
            return None
        return date_de_naissance

    def demander_sexe(self):
        sexe = input("Sexe: ")
        if not sexe:
            return None
        return sexe

    def demander_elo(self):
        elo = input("Elo: ")
        if not elo:
            return None
        return elo

class TournoiView:


    def creer_tournoi(self):
        nom = input("Entrez le nom du tournoi: ")
        lieu = input("Entrez le lieu du tournoi: ")
        date = input("Entrez la date du tournoi: ")
        description = input("Entrez la description du tournoi: ")
        nb_de_tours = input("Entrez le nombre de tours du tournoi: ")
        return nom, lieu, date, date, description, nb_de_tours

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





