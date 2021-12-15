import random
from player_model import Joueur


class Match:

    def __init__(self, j1: Joueur, j2: Joueur):
        self.j1 = j1
        self.j2 = j2
        self.winner = None
        self.result = ()

    def __repr__(self):
        return print(f"Resultat du match : {self.j1},{self.j2}: {self.result} ")

    def play(self):
        score_1 = 0
        score_2 = 0
        random_result = random.randint(1, 3)
        if random_result == 1:
            self.winner = self.j1
            self.j1.nb_de_points += 1
            score_1, score_2 = 1, 0
        elif random_result == 2:
            self.winner = self.j2
            self.j2.nb_de_points += 1
            score_1, score_2 = 0, 1
        elif random_result == 3:
            self.winner = None
            self.j1.nb_de_points += 0.5
            self.j2.nb_de_points += 0.5
            score_1, score_2 = 0.5, 0.5
        self.result = (score_1, score_2)
        #self.result.append(score_2)

    @property
    def get_winner(self):
        return self.winner

    @property
    def get_result(self):
        return self.result

    def adversaires(self):
        return f"Ce match se joue entre {self.j1} et {self.j2}"



if __name__ == "__main__":
    nicolas = Joueur(
        **{"nom_de_famille": "Parent", "prenom": "Nicolas", "date_de_naissance": "18/08/92", "sexe": "Homme",
           "nb_de_points": 0, "elo": None, "j_id": "1"})
    abdelaziz = Joueur(
        **{"nom_de_famille": "Marjane", "prenom": "abdelaziz", "date_de_naissance": "18/08/92", "sexe": "Homme",
           "nb_de_points": 0, "elo": None, "j_id": "2"}
    )

    my_match = Match(nicolas, abdelaziz)
    my_match.play()
    my_match.__repr__()


# m = Match("a", "b")
# m.play_match()
# m.__repr__()

"""
    def ajouter_des_points(self):
        j1_score = int((input("Entez le nombre de points du Joueur1 ")))
        j2_score = int((input("Entez le nombre de points du Joueur2 ")))
        message = f"Erreur le nombre de points doit être un 0, 0.5 ou 1"
        try:
            if j1_score == 0 or j1_score == 1 or j1_score == 0.5:
                j1_score = int((input("Entez le nombre de points du Joueur1 ")))
            else: raise ValueError(message)
            if j2_score == 0 or j2_score == 1 or j2_score == 0.5:
                j2_score = int((input("Entez le nombre de points du Joueur2 ")))
            else:raise ValueError(message)

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


for x in m.adversaires:
    print(list(x))
"""
