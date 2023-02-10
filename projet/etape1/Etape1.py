"""
module pour l'etape 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverSAT import SolverSAT

from projet.outils.Tester import Tester

import sys

class Variable :

    @staticmethod
    def encode(sommet, couleur, is_not=False) -> int: 
        """
        encode un couple (sommet, couleur) en un entier
        
        :param sommet: le sommet a encoder
        :param couleur: la couleur a encoder
        
        :return: l'entier correspondant au couple (sommet, couleur)
        
        :note: l'entier est negatif si is_not est vrai
        """
        sign = -1 if is_not else 1
        return sign * (((sommet+1) << 8) + (couleur+1))

    @staticmethod
    def decode(number) -> tuple[int, int, bool]:
        """
        decode un entier en un couple (sommet, couleur)

        :param number: l'entier a decoder

        :return: le couple (sommet, couleur) correspondant a l'entier

        :note: le booleen est vrai si l'entier est negatif
        """
        is_not = number < 0
        number = abs(number)

        sommet = (number >> 8)
        couleur = (number & 0b11111111)

        return (sommet, couleur, is_not)

    

class Etape1 :
    """
    classe pour realiser l'etape 1 du projet (tache 1) 
    """
    # attributs
    # //////////////////////////////////////////////
    g : GrapheDeLieux 
    """
    le graphe representant le monde 
    """
    base : list
    """
    la base de clauses representant le probleme. 
    C'est une liste de listes d'entiers, un entier par variable, 
    (positif si literal positif, negatif sinon). 
    Attention le 0 n'est pas autorise pour represente une variable
    maj par majBase
    """
    nbVariables : int 
    """
    le nb de variables utilisees pour representer le probleme 
    maj par majBase
    """
    
    # constructeur
    # //////////////////////////////////////////////
    def __init__ (self, fn : str, form : bool) :
        """
        constructeur
        
        :param fn: le nom du fichier dans lequel sont donnes les sommets et les aretes
        
        :param form: permet de distinguer entre les differents types de fichier 
         (pour ceux contenant des poids et des coordonnees, form est True ;
          pour les autres, form est False)   
        """
        self.g = GrapheDeLieux.loadGraph(fn,form)
        self.base = [] 
        self.nbVariables = 0        
    
    # methodes
    # //////////////////////////////////////////////
    def majBase(self, nb_couleurs : int) :
        """
        methode de maj de la base de clauses et du nb de variables en fonction du pb traite 
        
        :param x: parametre servant pour definir la base qui representera le probleme
        """
        # A ECRIRE par les etudiants en utilisant le contenu de g
        # ajout possible de parametre => modifier aussi l'appel ds le main

        def clauses_sommet(sommet):
            clauses = []
            clauses.append([Variable.encode(sommet, couleur) for couleur in range(nb_couleurs)])

            for couleur in range(nb_couleurs):
                next_couleur = (couleur + 1) % nb_couleurs
                clauses.append([
                    Variable.encode(sommet, couleur, is_not=True),
                    Variable.encode(sommet, next_couleur, is_not=True)
                ])
            
            return clauses

        def clauses_adjacents(sommet):
            clauses = []
            for couleur in range(nb_couleurs):
                for neighbour in self.g.getAdjacents(sommet):
                    clauses.append([
                        Variable.encode(sommet, couleur, is_not=True),
                        Variable.encode(neighbour, couleur, is_not=True)
                        ])
            return clauses

        self.base = []
        for sommet in self.g.getSommets():
            self.base += clauses_sommet(sommet)
            self.base += clauses_adjacents(sommet)

        self.nbVariables = self.g.getNbSommets() * nb_couleurs
    
    def execSolver(self) : 
        """
        methode d'appel du solver sur la base de clauses representant le pb traite
        
        :return True si la base de clauses representant le probleme est satisfiable, 
                False sinon
        """
        return SolverSAT.solve(self.base)     
    
    def affBase(self) :
        """
        affichage de la base de clauses representant le probleme 
        """

        def _decode_one(number):
            sommet, couleur, is_not = Variable.decode(number)

            str = f"({sommet}, {couleur})"
            if is_not:
                str = f"-{str}"

            return str

        _decode = lambda clause: ", ".join([_decode_one(x) for x in clause])


        print('Base de clause utilise ',self.nbVariables,' variables et contient les clauses suivantes : ') 
        for cl in self.base :
            print(_decode(cl)) 
    

class __testEtape1__ : 
    """  
    methode principale de test
    """
    # TESTS
    # //////////////////////////////////////////////
    def main_new():
        tester = Tester()

        e = Etape1("Data/town10.txt", True)

        e.majBase(3)
        tester.test("Fichier town10.txt avec 3 couleurs", e.execSolver(), True)

        e.majBase(2)
        tester.test("Fichier town10.txt avec 2 couleurs", e.execSolver(), False)

        e.majBase(4)
        tester.test("Fichier town10.txt avec 4 couleurs", e.execSolver(), True)

        print("")

        e = Etape1("Data/pb-etape1/flat20_3_0.col",False) ;
        e.majBase(4)
        tester.test("Fichier flat20_3_0.col avec 4 couleurs", e.execSolver(), True)
        
        e.majBase(3)
        tester.test("Fichier flat20_3_0.col avec 3 couleurs", e.execSolver(), True)
        
        e.majBase(2)
        tester.test("Fichier flat20_3_0.col avec 2 couleurs", e.execSolver(), False)
        
        print("")

        e = Etape1("Data/pb-etape1/jean.col",False)
        e.majBase(10)
        tester.test("Fichier jean.col avec 10 couleurs", e.execSolver(), True)

        e.majBase(9)
        tester.test("Fichier jean.col avec 9 couleurs", e.execSolver(), False)

        e.majBase(3)
        tester.test("Fichier jean.col avec 3 couleurs", e.execSolver(), False)

        print("")
        tester.summary()


    def main():
        # TEST 1 : town10.txt avec 3 couleurs
        print("Test sur fichier town10.txt avec 3 couleurs") ;
        e = Etape1("Data/town10.txt",True) ;
        e.majBase(3) ;
        e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver()) ;
        
        
        # TEST 2 : town10.txt avec 2 couleurs
        print("Test sur fichier town10.txt avec 2 couleurs") ;
        e.majBase(2) ;
        e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver()) ;
        
        
        # TEST 3 : town10.txt avec 4 couleurs
        print("Test sur fichier town10.txt avec 4 couleurs") ;
        e.majBase(4) ;
        e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver()) ;
        
        
        # TEST 4 : flat20_3_0.col avec 4 couleurs
        print("Test sur fichier flat20_3_0.col avec 4 couleurs") ;
        e = Etape1("Data/pb-etape1/flat20_3_0.col",False) ;
        e.majBase(4) ;
        # e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver()) ;
        
        # TEST 5 : flat20_3_0.col avec 3 couleurs
        print("Test sur fichier flat20_3_0.col avec 3 couleurs") ;
        e.majBase(3) ;
        # e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver()) ;
        
        # TEST 6 : flat20_3_0.col avec 2 couleurs
        print("Test sur fichier flat20_3_0.col avec 2 couleurs") ;
        e.majBase(2) ;
        # e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver()) ;
        
            
        
        # TEST 7 : jean.col avec 10 couleurs
        print("Test sur fichier jean.col avec 10 couleurs") ;
        e = Etape1("Data/pb-etape1/jean.col",False) ;
        e.majBase(10) ;
        # e.affBase() ;
        print("Resultat obtenu (on attend True) :",e.execSolver()) ;
        
        # TEST 9 : jean.col avec 9 couleurs
        print("Test sur fichier jean.col avec 9 couleurs") ;
        e.majBase(9) ;
        # e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver()) ;
        
        # TEST 8 : jean.col avec 3 couleurs
        print("Test sur fichier jean.col avec 3 couleurs") ;
        e.majBase(3) ;
        # e.affBase() ;
        print("Resultat obtenu (on attend False) :",e.execSolver()) ;
        

if __name__ == '__main__' :
    if len(sys.argv) > 1 and sys.argv[1] == "new":
        __testEtape1__.main_new()
    else:
        __testEtape1__.main()
