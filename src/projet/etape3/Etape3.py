"""
module principal pour l'etape 3
"""

from projet.outils.GrapheDeLieux import GrapheDeLieux
from solutions.etape3 import SolEtape3 as UneSolution

# rajouter ensuite le import permettant d'utiliser les solvers choisis
# from solvers.... import ...
from projet.solvers.SolverHC import SolverHC
from projet.solvers.SolverTabou import SolverTabou


class Etape3 :
    """  classe pour realiser les tests de l'etape 3 du projet (suite tache 2) """ 


    #    tests
    #    ////////////////////////////////////////////
    """  methode de TESTS pour Etape3
    """ 
    if __name__ == '__main__':
    
                                   
        #    tests sur Etape 3
        #    ///////////////////
        #    cas 1 : 10 villes de 0 à 9
        tg : GrapheDeLieux = GrapheDeLieux.loadGraph("Data/town10.txt",True) 
        tsp : UneSolution = UneSolution(tg) 
        print("======== Solver 1 pour 10 villes de 0 a 9 : \n")
        SolverHC.hilClimbing(tsp)
                         
        print("======== Solver 2 pour 10 villes de 0 a 9 : \n")
        SolverTabou.tabou(tsp)

                                   
        #    ///////////////////
        #    cas 2 : 26 villes de 0 à 25
        tg = GrapheDeLieux.loadGraph("Data/town30.txt",True) 
        tsp = UneSolution(tg) 
        print("======== Solver 1 pour 26 villes de 0 a 25 : \n")
        SolverHC.hilClimbing(tsp)

        print("======== Solver 2 pour 26 villes de 0 a 25 : \n")
        SolverTabou.tabou(tsp)

                                   
                                   
        #    ///////////////////
        #    cas 3 : 150 villes 
        tg = GrapheDeLieux.loadGraph("Data/town150.txt",True) 
        tsp = UneSolution(tg) 
        print("======== Solver 1 pour 150 villes : \n")
        SolverHC.hilClimbing(tsp)

        print("======== Solver 2 pour 150 villes : \n")
        SolverTabou.tabou(tsp)

                                   
                                   
        #    ///////////////////
        #    cas 4 : 1000 villes 
        tg = GrapheDeLieux.loadGraph("Data/town1000.txt",True) 
        tsp = UneSolution(tg) 
        print("======== Solver 1 pour 1000 villes : \n")
        SolverHC.hilClimbing(tsp)

        print("======== Solver 2 pour 1000 villes : \n")
        SolverTabou.tabou(tsp)
                                        
    

