"""
module pour l'etape 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.solvers.SolverSAT import SolverSAT

########################################################################################

Base = list[list[int]]

class SolEtape1:

    def mise_a_jour_base(g: GrapheDeLieux, nb_couleurs: int) -> tuple[Base, int]:
        base = []
        for sommet in g.getSommets():
            base += clauses_sommet(sommet, nb_couleurs)
            base += clauses_adjacents(sommet, g, nb_couleurs)

        nbVariables = g.getNbSommets() * nb_couleurs

        return base, nbVariables

    def fmt_clause(clause: list[int]) -> str:
        def fmt_variable(variable: int) -> str:
            sommet, couleur, is_not = Variable.decode(variable)
            not_str = "¬" if is_not else ""
            return f"{not_str}s{sommet}_c{couleur}"
        
        return ' v '.join([fmt_variable(variable) for variable in clause])



def clauses_sommet(sommet, nb_couleurs: int):
    clauses = []
    clauses.append([Variable.encode(sommet, couleur) for couleur in range(nb_couleurs)])

    for couleur in range(nb_couleurs):
        next_couleur = (couleur + 1) % nb_couleurs
        clauses.append([
            Variable.encode(sommet, couleur, is_not=True),
            Variable.encode(sommet, next_couleur, is_not=True)
        ])
    
    return clauses

def clauses_adjacents(sommet, g, nb_couleurs: int):
    clauses = []
    for couleur in range(nb_couleurs):
        for neighbour in g.getAdjacents(sommet):
            clauses.append([
                Variable.encode(sommet, couleur, is_not=True),
                Variable.encode(neighbour, couleur, is_not=True)
                ])
    return clauses

class Variable :

    @staticmethod
    def encode(sommet, couleur, is_not=False) -> int:
        sign = -1 if is_not else 1
        return sign * (((sommet+1) << 8) + (couleur+1))

    @staticmethod
    def decode(number) -> tuple[int, int, bool]:
        is_not = number < 0
        number = abs(number)

        sommet = (number >> 8)
        couleur = (number & 0b11111111)

        return (sommet, couleur, is_not)
    
########################################################################################

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
    def majBase(self, x : int) :
        """
        methode de maj de la base de clauses et du nb de variables en fonction du pb traite 
        
        :param x: parametre servant pour definir la base qui representera le probleme 
        """
        # A ECRIRE par les etudiants en utilisant le contenu de g
        # ajout possible de parametre => modifier aussi l'appel ds le main
        self.base, self.nbVariables = SolEtape1.mise_a_jour_base(self.g, x)
    
    
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
        print('Base de clause utilise ',self.nbVariables,' variables et contient les clauses suivantes : ') 
        for cl in self.base :
            print(SolEtape1.fmt_clause(cl)) 
    

class __testEtape1__ : 
    """  
    methode principale de test
    """
    # TESTS
    # //////////////////////////////////////////////
    if __name__ == '__main__':
        
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
        

