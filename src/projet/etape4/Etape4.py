"""
module principal pour l'etape 4
"""

from projet.outils.GrapheDeLieux import GrapheDeLieux
from solutions.etape4 import etape4

# rajouter ensuite le import permettant d'utiliser le solver (l'algo) choisi
# from solvers.... import ...

class Etape4 :
    """
    classe de test pour l'etape 4
    """
    
    if __name__ == '__main__':
   
        print("\n========== TEST  ==========") 
        print("=============================") 
        
        #    TEST 1 : town10.txt avec 3 couleurs
        tg : GrapheDeLieux = GrapheDeLieux.loadGraph("Data/town10.txt",True) 
        print("\nTest sur town10 avec 3 couleurs (on attend OK) :") 
        etape4(tg, 3)
                
        #    TEST 2 : town10.txt avec 2 couleurs
        print("\nTest sur town10 avec 2 couleurs (on attend NOK) :") 
        etape4(tg, 2)

        #    TEST 3 : town10.txt avec 4 couleurs
        print("\nTest sur town10 avec 4 couleurs (on attend OK) :") 
        etape4(tg, 4)

                   
        #    TEST 4 : flat20_3_0.col avec 4 couleurs
        tg = GrapheDeLieux.loadGraph("Data/pb-etape1/flat20_3_0.col",False) 
        print("Test sur flat20_3_0.col avec 4 couleurs (on attend OK) :") 
        etape4(tg, 4)
    
        #    TEST 5 : flat20_3_0.col avec 3 couleurs
        print("Test sur flat20_3_0.col avec 3 couleurs (on attend OK) :") 
        etape4(tg, 3)
    
        #    TEST 6 : flat20_3_0.col avec 2 couleurs
        print("Test sur flat20_3_0.col avec 2 couleurs (on attend NOK) :") 
        etape4(tg, 2)


    
        #    TEST 7 : jean.col avec 10 couleurs
        tg = GrapheDeLieux.loadGraph("Data/pb-etape1/jean.col",False) 
        print("Test sur jean.col avec 10 couleurs (on attend OK) :") 
        etape4(tg, 10)
    
        #    TEST 9 : jean.col avec 3 couleurs
        print("Test sur jean.col avec 3 couleurs (on attend NOK) :") 
        etape4(tg, 3)
    
        #    TEST 8 : jean.col avec 9 couleurs
        print("Test sur jean.col avec 9 couleurs (on attend NOK) :") 
        etape4(tg, 9)
                
                
        


