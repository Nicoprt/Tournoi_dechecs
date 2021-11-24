class Match:

    def __init__(self, j1=None, j2=None, j1score=0, j2score=0):
        self.j1 = j1
        self.j2 = j2
        self.j1score = j1score
        self.j2score = j2score
"""
    def ajouter_des_points(self):
        j1score = int((input("Entez le nombre de points du Joueur1 ")))
        j2score = int((input("Entez le nombre de points du Joueur2 ")))
        message = f"Erreur le nombre de points doit être un 0, 0.5 ou 1"
        try:
            if j1score == 0 or j1score == 1 or j1score == 0.5:
                j1score = int((input("Entez le nombre de points du Joueur1 ")))
            else: raise ValueError(message)
            if j2score == 0 or j2score == 1 or j2score == 0.5:
                j2score = int((input("Entez le nombre de points du Joueur2 ")))
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