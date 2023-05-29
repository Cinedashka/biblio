import sqlite3


class Livre:
    def __init__(self, id, titre, annee, exemplaires, nom_auteur, prenom_auteur):
        self.id = id
        self.titre = titre
        self.annee = annee
        self.exemplaires = exemplaires
        self.nom_auteur = nom_auteur
        self.prenom_auteur= prenom_auteur



class Database:
    def __init__(self, db_livre):
        self.connexion = sqlite3.connect(db_livre)
        self.cursor = self.connexion.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS livres (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT, annee INTEGER, exemplaires INTEGER, nom_auteur TEXT, prenom_auteur TEXT)")

        self.connexion.commit()

    def ajouter_livres(self, titre, annee, exemplaires, nom_auteur, prenom_auteur):
            self.cursor.execute("INSERT INTO livres (titre, annee, exemplaires, nom_auteur, prenom_auteur) VALUES (?, ?, ?, ?, ?)",
                   (titre, annee, exemplaires, nom_auteur, prenom_auteur))

            self.connexion.commit()
            
    def recuperer_livres(self):
        self.cursor.execute('''
            SELECT * FROM livres
        ''')
        rows = self.cursor.fetchall()
        livres = []
        for row in rows:
            livre = Livre(*row)  # Constructing the Personne object
            livres.append(livre)
        return livres

    def fermer_connexion(self):
        self.connexion.close()
