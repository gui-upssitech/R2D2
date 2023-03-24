"""
module pour l'état de l'etape 2 ds le cas 1
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas1(Etat) :
    def estSolution(self) :
        return self.etat_courant == self.etat_fin
    
    def successeurs(self) :
        create_etat = lambda sommet: EtatCas1(self.tg, sommet, self.etat_fin)
        return [ create_etat(sommet) for sommet in self.tg.getAdjacents(self.etat_courant) ]
    
    def h(self) :
        return GrapheDeLieux.dist(self.etat_courant, self.etat_fin, self.tg)
    
    def k(self, e) :
        return self.tg.getCoutArete(self.etat_courant, e.etat_courant)
    
    def displayPath(self, pere) :
        chemin = []
        cur = self
        while cur != None:
            chemin.append(cur.etat_courant)
            cur = pere[cur]

        print("resultat trouve :", chemin)

    #######################################################################################

    def __init__(self, tg : GrapheDeLieux, etat_courant: int = 0, etat_fin: int = None) :
        self.tg = tg

        self.etat_courant = etat_courant
        self.etat_fin = etat_fin if (etat_fin is not None) else tg.getNbSommets() - 1

    def __hash__(self) :
        summary_num = self.etat_fin * 1000 + self.etat_courant
        return summary_num.__hash__() 
    
    def __eq__(self, o) :
        if not isinstance(o, EtatCas1):
            return False

        e: EtatCas1 = o
        return (
            self.etat_courant == e.etat_courant and 
            self.etat_fin == e.etat_fin
        )   
    
    def __str__(self) :
        return f"Etat[etat_courant={self.etat_courant}, etat_fin={self.etat_fin}]"