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


if __name__ == "__main__":

    elif len(liste_paires2) <= 1:
    liste_paires2.append((Joueur.__str__(first_half[i])))
    liste_paires2.append((Joueur.__str__(second_half[i])))

elif len(liste_paires3) <= 1:
    liste_paires3.append((Joueur.__str__(first_half[i])))
    liste_paires3.append((Joueur.__str__(second_half[i])))
else:
    liste_paires4.append((Joueur.__str__(first_half[i])))
    liste_paires4.append((Joueur.__str__(second_half[i])))

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