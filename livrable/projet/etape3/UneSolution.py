"""  module pour la classe UneSolution """ 

from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape3.Solution import Solution

from random import Random

class UneSolution(Solution) :
    
    def lesVoisins(self) :
        voisinage = []
        chm_modifiable = self.chemin[1:-1]

        for i in range(1, len(chm_modifiable)):
            chm_modifiable[i-1], chm_modifiable[i] = chm_modifiable[i], chm_modifiable[i-1]
            nouveau_chemin = [0] + chm_modifiable + [0]
            voisinage.append( UneSolution(self.tg, nouveau_chemin) )

        return voisinage

    def unVoisin(self) :
        voisinage = self.lesVoisins()
        random_index = self.rd.randint(0, len(voisinage) - 1)
        return [ voisinage[random_index] ]
    

    def eval(self) :    
        return sum([ GrapheDeLieux.dist(self.chemin[i-1], self.chemin[i], self.tg) for i in range(1, len(self.chemin)) ])
    
    
    def nelleSolution(self) :
        chemin = list(range(1, self.tg.getNbSommets()))
        self.rd.shuffle(chemin)
        chemin = [0] + chemin + [0]

        return UneSolution(self.tg, chemin)
    
    
    def displayPath(self) :
        print("la meilleure solution est : ", self.path_str(" -> "))
    

    #######################################################################################

    def path_str(self, sep="") :
        return sep.join([str(num) for num in self.chemin])


    def __init__(self, tg : GrapheDeLieux, chemin : list = []):
        self.tg = tg
        self.chemin = chemin
        self.rd = Random()

        if len(chemin) == 0:
            self.chemin = self.nelleSolution().chemin


    def __hash__(self) :
        return self.path_str().__hash__()
    
    
    def __eq__(self,o) :
        if not isinstance(o, UneSolution):
            return False

        e: UneSolution = o
        return self.chemin == e.chemin
    

    def __str__(self) :
        return f"Solution [ chemin={self.chemin}, cout={self.eval()} ]\n"
    


