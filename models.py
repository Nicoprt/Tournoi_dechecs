
class Tournoi:
    def __init__(self, nom, lieu, date, joueurs, description, nb_de_tours=4):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.joueurs = joueurs
        self.description = description
        self.nb_de_tours = nb_de_tours
        #  self.tournees = tournees

    def afficher_tournoi(self):
        return f"Tournoi: {self.nom}, {self.lieu}, {self.date}, {self.joueurs},{self.description}, {self.nb_de_tours}"


class Tournees:
    def __init__(self):
        self.tournees = []

class Joueur:
    def __init__(self, nom_de_famille, prenom, date_de_naissance, sexe, classement=0):
        self.nom_de_famille = nom_de_famille
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement

    def afficher_joueur(self):
        return f"Joueur: {self.nom_de_famille}, {self.prenom}, {self.date_de_naissance}, {self.sexe}, {self.classement}"


class Tour:
    def __init__(self, nom, date, heure_de_debut, heure_de_fin):
        self.nom = nom
        self.date = date
        self.heure_de_debut = heure_de_debut
        self.heure_de_fin = heure_de_fin

    def afficher_tour(self):
        return f"Joueur: {self.nom}, {self.date}, {self.heure_de_debut}, {self.heure_de_fin}"

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2


tournoi_1 = Tournoi("1","paris","01/01/01","zzzz")
print(tournoi_1.__dict__)



